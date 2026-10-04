#!/usr/bin/env python3

from pathlib import Path
import argparse
import re
import textwrap

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Helpers
# ============================================================

def clean_sp_title(s):
    """Extract a readable Swiss-Prot protein name."""
    if pd.isna(s):
        return ""

    s = str(s).strip()

    # Remove accession at beginning.
    s = re.sub(r"^\S+\s+", "", s)

    # Prefer Swiss-Prot RecName Full=...
    m = re.search(r"RecName:\s*Full=([^;\[]+)", s)
    if m:
        return m.group(1).strip()

    # Otherwise generic Full=
    m = re.search(r"Full=([^;\[]+)", s)
    if m:
        return m.group(1).strip()

    # Remove organism suffix.
    s = re.sub(r"\s*\[[^\]]+\]\s*$", "", s)

    return s.strip()


def clean_nr_title(s):
    if pd.isna(s):
        return ""

    s = str(s).strip()
    s = re.sub(r"^\S+\s+", "", s)
    s = re.sub(r"\s*\[[^\]]+\]\s*$", "", s)

    # NR loves this word. It adds no useful information.
    s = re.sub(r"^PREDICTED:\s*", "", s, flags=re.I)

    return s.strip()


def safe_text(x):
    if pd.isna(x):
        return ""
    x = str(x).strip()
    if x in {"-", "nan", "None"}:
        return ""
    return x


# ============================================================
# Annotation readers
# ============================================================

def read_diamond(path, prefix):
    df = pd.read_csv(path, sep="\t")

    numeric = [
        "evalue",
        "bitscore",
        "pident"
    ]

    for c in numeric:
        if c in df.columns:
            df[c] = pd.to_numeric(
                df[c],
                errors="coerce"
            )

    # Pick strongest hit per query.
    sort_cols = []
    ascending = []

    if "evalue" in df.columns:
        sort_cols.append("evalue")
        ascending.append(True)

    if "bitscore" in df.columns:
        sort_cols.append("bitscore")
        ascending.append(False)

    if "pident" in df.columns:
        sort_cols.append("pident")
        ascending.append(False)

    if sort_cols:
        df = df.sort_values(
            sort_cols,
            ascending=ascending
        )

    df = df.drop_duplicates(
        "qseqid",
        keep="first"
    )

    keep = [
        c for c in [
            "qseqid",
            "sseqid",
            "evalue",
            "bitscore",
            "pident",
            "stitle",
            "sscinames"
        ]
        if c in df.columns
    ]

    df = df[keep].copy()

    rename = {
        c: f"{prefix}_{c}"
        for c in df.columns
        if c != "qseqid"
    }

    return df.rename(
        columns=rename
    )


def read_eggnog(path):
    # eggNOG output contains ## metadata before the real #query header.
    header_line = None

    with open(
        path,
        "r",
        encoding="utf-8",
        errors="replace"
    ) as fh:

        for i, line in enumerate(fh):

            if line.startswith("#query\t"):
                header_line = i
                break

    if header_line is None:
        raise RuntimeError(
            f"Could not find #query header in {path}"
        )

    df = pd.read_csv(
        path,
        sep="\t",
        skiprows=header_line
    )

    df = df.rename(
        columns={
            df.columns[0]:
            df.columns[0].lstrip("#")
        }
    )

    keep = [
        c for c in [
            "query",
            "seed_ortholog",
            "Description",
            "Preferred_name",
            "eggNOG_OGs",
            "GOs",
            "KEGG_ko",
            "PFAMs"
        ]
        if c in df.columns
    ]

    return df[keep].copy()


def read_orthogroups(path):
    df = pd.read_csv(
        path,
        sep="\t"
    )

    guo_col = [
        c for c in df.columns
        if c.startswith("Guo.")
    ][0]

    rep_cols = [
        c for c in df.columns
        if c != "Orthogroup"
    ]

    mapping = []

    for _, row in df.iterrows():

        guo = safe_text(
            row[guo_col]
        )

        if not guo:
            continue

        n_representations = sum(
            bool(safe_text(row[c]))
            for c in rep_cols
        )

        guo_members = [
            x.strip()
            for x in guo.split(",")
            if x.strip()
        ]

        for transcript in guo_members:

            mapping.append(
                {
                    "transcript_id":
                        transcript,

                    "orthogroup":
                        row["Orthogroup"],

                    "orthogroup_representations":
                        n_representations,

                    "guo_members_in_orthogroup":
                        len(guo_members)
                }
            )

    return pd.DataFrame(mapping)


# ============================================================
# Optional InterProScan reader
# ============================================================

def read_interpro(path):
    """
    Works with common InterProScan Excel layouts.
    If parsing fails, the script continues without it.
    """

    try:
        df = pd.read_excel(path)
    except Exception:
        return pd.DataFrame()

    # Standard Galaxy/InterProScan names where available.
    id_candidates = [
        "Protein accession",
        "Protein Accession",
        "protein_accession",
        "Sequence ID"
    ]

    id_col = next(
        (
            c for c in id_candidates
            if c in df.columns
        ),
        None
    )

    # If exported without standard header, assume first column = protein ID.
    if id_col is None and len(df.columns):
        id_col = df.columns[0]

    if id_col is None:
        return pd.DataFrame()

    desc_candidates = [
        "InterPro annotations - description",
        "InterPro description",
        "Signature description",
        "Description"
    ]

    desc_cols = [
        c for c in desc_candidates
        if c in df.columns
    ]

    if not desc_cols:
        return pd.DataFrame()

    rows = []

    for protein, sub in df.groupby(id_col):

        descriptions = []

        for c in desc_cols:

            for value in sub[c].dropna():

                value = safe_text(value)

                if value and value not in descriptions:
                    descriptions.append(value)

        rows.append(
            {
                "query":
                    str(protein),

                "interpro_description":
                    "; ".join(
                        descriptions[:8]
                    )
            }
        )

    return pd.DataFrame(rows)


# ============================================================
# Functional label hierarchy
# ============================================================

def choose_label(row):

    sp = clean_sp_title(
        row.get(
            "sp_stitle",
            ""
        )
    )

    egg = safe_text(
        row.get(
            "Description",
            ""
        )
    )

    preferred = safe_text(
        row.get(
            "Preferred_name",
            ""
        )
    )

    nr = clean_nr_title(
        row.get(
            "nr_stitle",
            ""
        )
    )

    ipr = safe_text(
        row.get(
            "interpro_description",
            ""
        )
    )

    # Priority:
    # curated Swiss-Prot > informative eggNOG > NR > InterPro.
    if sp:
        return sp, "Swiss-Prot"

    if egg:
        return egg, "eggNOG"

    if preferred:
        return preferred, "eggNOG preferred name"

    if nr:
        return nr, "NR"

    if ipr:
        return ipr, "InterPro"

    return "Uncharacterized protein", "No informative hit"


# ============================================================
# Build annotation master
# ============================================================

def annotate_table(
    structural,
    swissprot,
    nr,
    eggnog,
    orthogroups,
    interpro=None
):

    df = structural.copy()

    df = df.merge(
        swissprot,
        left_on="transcript_id",
        right_on="qseqid",
        how="left"
    ).drop(
        columns=["qseqid"],
        errors="ignore"
    )

    df = df.merge(
        nr,
        left_on="transcript_id",
        right_on="qseqid",
        how="left"
    ).drop(
        columns=["qseqid"],
        errors="ignore"
    )

    df = df.merge(
        eggnog,
        left_on="transcript_id",
        right_on="query",
        how="left"
    ).drop(
        columns=["query"],
        errors="ignore"
    )

    if (
        interpro is not None and
        not interpro.empty
    ):

        df = df.merge(
            interpro,
            left_on="transcript_id",
            right_on="query",
            how="left"
        ).drop(
            columns=["query"],
            errors="ignore"
        )

    df = df.merge(
        orthogroups,
        on="transcript_id",
        how="left"
    )

    labels = df.apply(
        choose_label,
        axis=1
    )

    df["functional_label"] = [
        x[0] for x in labels
    ]

    df["label_source"] = [
        x[1] for x in labels
    ]

    return df


# ============================================================
# Render publication-style compact table
# ============================================================

def wrap(s, width=34):
    return "\n".join(
        textwrap.wrap(
            str(s),
            width=width
        )
    )


def render_table(
    df,
    columns,
    headers,
    output,
    title,
    figsize=(15, 7)
):

    show = df[
        columns
    ].copy()

    show.columns = headers

    for col in show.columns:

        show[col] = show[col].map(
            lambda x:
            wrap(x)
            if isinstance(x, str)
            else x
        )

    fig, ax = plt.subplots(
        figsize=figsize
    )

    ax.axis("off")

    table = ax.table(
        cellText=show.values,
        colLabels=show.columns,
        loc="center",
        cellLoc="left",
        colLoc="left"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8.5)

    table.scale(
        1,
        1.55
    )

    ax.set_title(
        title,
        pad=18,
        fontsize=12,
        fontweight="bold"
    )

    fig.tight_layout()

    fig.savefig(
        output.with_suffix(".png"),
        dpi=300,
        bbox_inches="tight"
    )

    fig.savefig(
        output.with_suffix(".pdf"),
        bbox_inches="tight"
    )

    fig.savefig(
        output.with_suffix(".svg"),
        bbox_inches="tight"
    )

    plt.close(fig)


# ============================================================
# Main
# ============================================================

parser = argparse.ArgumentParser()

parser.add_argument(
    "--repeat-heavy",
    required=True
)

parser.add_argument(
    "--largest-introns",
    required=True
)

parser.add_argument(
    "--swissprot",
    required=True
)

parser.add_argument(
    "--nr",
    required=True
)

parser.add_argument(
    "--eggnog",
    required=True
)

parser.add_argument(
    "--orthogroups",
    required=True
)

parser.add_argument(
    "--interpro",
    default=None
)

parser.add_argument(
    "--tables",
    default="../tables"
)

parser.add_argument(
    "--figures",
    default="../figures"
)

args = parser.parse_args()


TAB = Path(
    args.tables
).resolve()

FIG = Path(
    args.figures
).resolve()

TAB.mkdir(
    parents=True,
    exist_ok=True
)

FIG.mkdir(
    parents=True,
    exist_ok=True
)


# ------------------------------------------------------------
# Load inputs
# ------------------------------------------------------------

repeat = pd.read_csv(
    args.repeat_heavy,
    sep="\t"
)

giant = pd.read_csv(
    args.largest_introns,
    sep="\t"
)

sp = read_diamond(
    args.swissprot,
    "sp"
)

nr = read_diamond(
    args.nr,
    "nr"
)

egg = read_eggnog(
    args.eggnog
)

og = read_orthogroups(
    args.orthogroups
)

ipr = (
    read_interpro(
        args.interpro
    )
    if args.interpro
    else pd.DataFrame()
)


# ------------------------------------------------------------
# Annotate
# ------------------------------------------------------------

repeat = annotate_table(
    repeat,
    sp,
    nr,
    egg,
    og,
    ipr
)

giant = annotate_table(
    giant,
    sp,
    nr,
    egg,
    og,
    ipr
)


# ------------------------------------------------------------
# Add ranks and convenient units
# ------------------------------------------------------------

for df in [
    repeat,
    giant
]:

    df.insert(
        0,
        "rank",
        range(
            1,
            len(df) + 1
        )
    )

    df[
        "intronic_repeat_kb"
    ] = (
        df[
            "intron_repeat_bp"
        ] / 1000
    )

    df[
        "longest_intron_kb"
    ] = (
        df[
            "longest_intron_bp"
        ] / 1000
    )


# ------------------------------------------------------------
# Find overlap between the two Top-20 lists
# ------------------------------------------------------------

repeat_ids = set(
    repeat["gene_id"]
)

giant_ids = set(
    giant["gene_id"]
)

overlap = (
    repeat_ids &
    giant_ids
)

repeat[
    "also_top20_largest_intron"
] = repeat[
    "gene_id"
].isin(
    overlap
)

giant[
    "also_top20_repeat_heavy"
] = giant[
    "gene_id"
].isin(
    overlap
)


# ------------------------------------------------------------
# Full source tables
# ------------------------------------------------------------

repeat.to_csv(
    TAB /
    "phase7_top20_repeat_heavy_genes_annotated.tsv",
    sep="\t",
    index=False
)

giant.to_csv(
    TAB /
    "phase7_top20_largest_intron_genes_annotated.tsv",
    sep="\t",
    index=False
)


# ------------------------------------------------------------
# Compact manuscript/supplement tables
# ------------------------------------------------------------

common = [
    "rank",
    "gene_id",
    "transcript_id",
    "functional_label",
    "label_source",
    "orthogroup",
    "orthogroup_representations",
    "PFAMs"
]


repeat_compact = repeat[
    common +
    [
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "cds_repeat_pct",
        "also_top20_largest_intron"
    ]
].copy()


giant_compact = giant[
    common +
    [
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "cds_repeat_pct",
        "also_top20_repeat_heavy"
    ]
].copy()


repeat_compact.to_csv(
    TAB /
    "Table_S_repeat_heavy_genes.tsv",
    sep="\t",
    index=False
)

giant_compact.to_csv(
    TAB /
    "Table_S_largest_intron_genes.tsv",
    sep="\t",
    index=False
)


# ------------------------------------------------------------
# Combined union table
# ------------------------------------------------------------

union = pd.concat(
    [
        repeat.assign(
            architecture_set=
            "repeat-heavy"
        ),
        giant.assign(
            architecture_set=
            "largest-intron"
        )
    ],
    ignore_index=True
)

union = union.sort_values(
    [
        "gene_id",
        "architecture_set"
    ]
)

union.to_csv(
    TAB /
    "phase7_extreme_gene_master.tsv",
    sep="\t",
    index=False
)


# ------------------------------------------------------------
# Render Top-10 main-text tables
# ------------------------------------------------------------

repeat10 = repeat.head(
    10
).copy()

giant10 = giant.head(
    10
).copy()


render_table(

    repeat10,

    columns=[
        "rank",
        "gene_id",
        "functional_label",
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "cds_repeat_pct"
    ],

    headers=[
        "Rank",
        "Gene",
        "Homology-supported functional label",
        "Intronic repeat\n(kb)",
        "Intronic repeat\n(%)",
        "Longest intron\n(kb)",
        "Longest intron\nrepeat (%)",
        "CDS repeat\n(%)"
    ],

    output=
        FIG /
        "Table_repeat_heavy_genes",

    title=
        "Top repeat-heavy Guo gene models"
)


render_table(

    giant10,

    columns=[
        "rank",
        "gene_id",
        "functional_label",
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "cds_repeat_pct"
    ],

    headers=[
        "Rank",
        "Gene",
        "Homology-supported functional label",
        "Longest intron\n(kb)",
        "Longest intron\nrepeat (%)",
        "Total intronic\nrepeat (kb)",
        "Intronic repeat\n(%)",
        "CDS repeat\n(%)"
    ],

    output=
        FIG /
        "Table_largest_intron_genes",

    title=
        "Guo gene models with the largest introns"
)


# ------------------------------------------------------------
# README-ready Markdown
# ------------------------------------------------------------

md_repeat = repeat10[
    [
        "gene_id",
        "functional_label",
        "intronic_repeat_kb",
        "longest_intron_kb",
        "longest_intron_repeat_pct"
    ]
].copy()

md_repeat.columns = [
    "Gene",
    "Functional label",
    "Intronic repeat (kb)",
    "Longest intron (kb)",
    "Longest-intron repeat (%)"
]


md_giant = giant10[
    [
        "gene_id",
        "functional_label",
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "cds_repeat_pct"
    ]
].copy()

md_giant.columns = [
    "Gene",
    "Functional label",
    "Longest intron (kb)",
    "Longest-intron repeat (%)",
    "CDS repeat (%)"
]


for df in [
    md_repeat,
    md_giant
]:

    for c in df.columns:

        if (
            "(kb)" in c or
            "(%)" in c
        ):

            df[c] = df[c].map(
                lambda x:
                f"{x:.1f}"
            )


markdown = (
    "## Top repeat-heavy Guo genes\n\n"
    +
    md_repeat.to_markdown(
        index=False
    )
    +
    "\n\n"
    +
    "## Guo genes with the largest introns\n\n"
    +
    md_giant.to_markdown(
        index=False
    )
    +
    "\n"
)


(
    TAB /
    "phase7_extreme_gene_README_tables.md"
).write_text(
    markdown,
    encoding="utf-8"
)


print()
print("Phase 7 extreme-gene tables complete.")
print()
print("Tables:")
print(
    TAB /
    "phase7_top20_repeat_heavy_genes_annotated.tsv"
)
print(
    TAB /
    "phase7_top20_largest_intron_genes_annotated.tsv"
)
print(
    TAB /
    "phase7_extreme_gene_master.tsv"
)
print()
print("Rendered tables:")
print(
    FIG /
    "Table_repeat_heavy_genes.png"
)
print(
    FIG /
    "Table_largest_intron_genes.png"
)