#!/usr/bin/env python3

"""
RE-SAPRIA Phase 7
Cross-representation support for extreme repeat-expanded gene architecture.

Purpose
-------
Use Guo BRAKER models only as anchor identifiers, then ask whether members
of the same cross-representation OrthoFinder group are recovered in:

    - Cai fixed-on-Guo
    - Cai min1250
    - Cai Flye-HyPo

and whether those members independently enter the corresponding Top-20
extreme-gene set in those representations.

Important
---------
These are multiple representations/accessions of Sapria himalayana,
NOT four species.

OrthoFinder groups are therefore interpreted as cross-representation
gene-model groups, not species-level orthologues.

No unique "counterpart" is forced when an orthogroup contains multiple
models in one representation.
"""

from pathlib import Path
import argparse
import pandas as pd


# ============================================================
# Helpers
# ============================================================

def split_members(x):
    if pd.isna(x):
        return []

    x = str(x).strip()

    if not x:
        return []

    return [
        y.strip()
        for y in x.split(",")
        if y.strip()
    ]


def join_members(xs):
    xs = sorted(set(xs))
    return "; ".join(xs)


def detect_orthofinder_columns(df):
    cols = list(df.columns)

    out = {}

    for c in cols:

        if c == "Orthogroup":
            continue

        if c.startswith("Guo."):
            out["Guo"] = c

        elif c.startswith("Cai_fixed."):
            out["Fixed"] = c

        elif c.startswith("Cai_min1250."):
            out["Min1250"] = c

        elif c.startswith("Cai_FlyeHyPo."):
            out["FlyeHyPo"] = c

    required = {
        "Guo",
        "Fixed",
        "Min1250",
        "FlyeHyPo"
    }

    missing = required - set(out)

    if missing:
        raise RuntimeError(
            f"Could not identify OrthoFinder columns: {missing}"
        )

    return out


# ============================================================
# Load cross-representation Top-20 table
# ============================================================

def extreme_sets(path):
    """
    Returns transcript-ID sets for each representation.
    """

    df = pd.read_csv(
        path,
        sep="\t"
    )

    labels = {
        "Guo published":
            "Guo",

        "Cai fixed-on-Guo":
            "Fixed",

        "Cai min1250":
            "Min1250",

        "Cai Flye–HyPo":
            "FlyeHyPo",

        # tolerate plain hyphen version
        "Cai Flye-HyPo":
            "FlyeHyPo",
    }

    result = {
        "Guo": set(),
        "Fixed": set(),
        "Min1250": set(),
        "FlyeHyPo": set()
    }

    for _, row in df.iterrows():

        rep = labels.get(
            row["representation"]
        )

        if rep is None:
            continue

        result[rep].add(
            str(row["transcript_id"])
        )

    return result


# ============================================================
# Build transcript -> orthogroup lookup
# ============================================================

def build_orthogroup_lookup(
    orthogroups,
    columns
):

    lookup = {}

    for _, row in orthogroups.iterrows():

        og = row["Orthogroup"]

        members = {
            rep:
                split_members(
                    row[col]
                )

            for rep, col
            in columns.items()
        }

        for guo_tx in members["Guo"]:

            lookup[guo_tx] = {
                "orthogroup":
                    og,

                "members":
                    members
            }

    return lookup


# ============================================================
# Annotate one Guo-anchored extreme table
# ============================================================

def add_crossrep_support(
    anchor_df,
    og_lookup,
    top20_sets,
    architecture_name
):

    rows = []

    for _, row in anchor_df.iterrows():

        out = row.to_dict()

        tx = str(
            row["transcript_id"]
        )

        og = og_lookup.get(tx)

        # ----------------------------------------------------
        # No OrthoFinder group
        # ----------------------------------------------------

        if og is None:

            out.update(
                {
                    "orthogroup":
                        "",

                    "fixed_orthogroup_members":
                        "",

                    "min1250_orthogroup_members":
                        "",

                    "flyehypo_orthogroup_members":
                        "",

                    "fixed_extreme_members":
                        "",

                    "min1250_extreme_members":
                        "",

                    "flyehypo_extreme_members":
                        "",

                    "representations_present_n":
                        1,

                    "alternative_representations_present_n":
                        0,

                    "alternative_extreme_support_n":
                        0,

                    "total_extreme_support_n":
                        1,

                    "crossrepresentation_support":
                        "Guo anchor only"
                }
            )

            rows.append(out)
            continue


        members = og["members"]

        # ----------------------------------------------------
        # Members present in corresponding extreme Top-20
        # ----------------------------------------------------

        fixed_extreme = (
            set(members["Fixed"])
            &
            top20_sets["Fixed"]
        )

        min_extreme = (
            set(members["Min1250"])
            &
            top20_sets["Min1250"]
        )

        hypo_extreme = (
            set(members["FlyeHyPo"])
            &
            top20_sets["FlyeHyPo"]
        )


        # ----------------------------------------------------
        # Representation presence
        # ----------------------------------------------------

        presence = {
            rep:
                len(members[rep]) > 0

            for rep in [
                "Guo",
                "Fixed",
                "Min1250",
                "FlyeHyPo"
            ]
        }

        total_present = sum(
            presence.values()
        )

        alternative_present = sum(
            presence[x]
            for x in [
                "Fixed",
                "Min1250",
                "FlyeHyPo"
            ]
        )


        # ----------------------------------------------------
        # Independent extreme-set recurrence
        # ----------------------------------------------------

        alt_extreme_n = sum(
            [
                bool(fixed_extreme),
                bool(min_extreme),
                bool(hypo_extreme)
            ]
        )

        total_extreme_n = (
            1 + alt_extreme_n
        )


        # ----------------------------------------------------
        # Human-readable support
        # ----------------------------------------------------

        support = (
            f"{total_present}/4 representations present; "
            f"{alt_extreme_n}/3 alternative representations "
            f"also Top-20 {architecture_name}"
        )


        out.update(
            {
                "orthogroup":
                    og["orthogroup"],

                "fixed_orthogroup_members":
                    join_members(
                        members["Fixed"]
                    ),

                "min1250_orthogroup_members":
                    join_members(
                        members["Min1250"]
                    ),

                "flyehypo_orthogroup_members":
                    join_members(
                        members["FlyeHyPo"]
                    ),

                "fixed_extreme_members":
                    join_members(
                        fixed_extreme
                    ),

                "min1250_extreme_members":
                    join_members(
                        min_extreme
                    ),

                "flyehypo_extreme_members":
                    join_members(
                        hypo_extreme
                    ),

                "representations_present_n":
                    total_present,

                "alternative_representations_present_n":
                    alternative_present,

                "alternative_extreme_support_n":
                    alt_extreme_n,

                "total_extreme_support_n":
                    total_extreme_n,

                "crossrepresentation_support":
                    support
            }
        )

        rows.append(out)

    return pd.DataFrame(rows)


# ============================================================
# Compact manuscript table
# ============================================================

def compact_repeat(df):

    cols = [
        "rank",
        "gene_id",
        "transcript_id",
        "functional_label",
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "longest_intron_kb",
        "longest_intron_repeat_pct",

        "orthogroup",

        "fixed_extreme_members",
        "min1250_extreme_members",
        "flyehypo_extreme_members",

        "alternative_representations_present_n",
        "alternative_extreme_support_n"
    ]

    return df[
        [
            c for c in cols
            if c in df.columns
        ]
    ]


def compact_giant(df):

    cols = [
        "rank",
        "gene_id",
        "transcript_id",
        "functional_label",
        "longest_intron_kb",
        "longest_intron_repeat_pct",
        "intronic_repeat_kb",
        "intron_repeat_pct",
        "cds_repeat_pct",

        "orthogroup",

        "fixed_extreme_members",
        "min1250_extreme_members",
        "flyehypo_extreme_members",

        "alternative_representations_present_n",
        "alternative_extreme_support_n"
    ]

    return df[
        [
            c for c in cols
            if c in df.columns
        ]
    ]


# ============================================================
# Summary
# ============================================================

def make_summary(
    repeat_df,
    giant_df
):

    rows = []

    for name, df in [
        (
            "repeat-heavy",
            repeat_df
        ),
        (
            "largest-intron",
            giant_df
        )
    ]:

        n = len(df)

        rows.append(
            {
                "architecture":
                    name,

                "n_Guo_anchor_loci":
                    n,

                "present_all_4_representations":
                    int(
                        (
                            df[
                                "representations_present_n"
                            ]
                            == 4
                        ).sum()
                    ),

                "present_at_least_3_representations":
                    int(
                        (
                            df[
                                "representations_present_n"
                            ]
                            >= 3
                        ).sum()
                    ),

                "alternative_top20_support_3_of_3":
                    int(
                        (
                            df[
                                "alternative_extreme_support_n"
                            ]
                            == 3
                        ).sum()
                    ),

                "alternative_top20_support_at_least_2":
                    int(
                        (
                            df[
                                "alternative_extreme_support_n"
                            ]
                            >= 2
                        ).sum()
                    ),

                "alternative_top20_support_at_least_1":
                    int(
                        (
                            df[
                                "alternative_extreme_support_n"
                            ]
                            >= 1
                        ).sum()
                    )
            }
        )

    return pd.DataFrame(rows)


# ============================================================
# CLI
# ============================================================

parser = argparse.ArgumentParser()

parser.add_argument(
    "--repeat-heavy-annotated",
    required=True,
    help="Guo annotated Top-20 repeat-heavy table"
)

parser.add_argument(
    "--largest-introns-annotated",
    required=True,
    help="Guo annotated Top-20 largest-intron table"
)

parser.add_argument(
    "--repeat-heavy-by-representation",
    required=True
)

parser.add_argument(
    "--largest-introns-by-representation",
    required=True
)

parser.add_argument(
    "--orthogroups",
    required=True
)

parser.add_argument(
    "--outdir",
    default="../tables"
)

args = parser.parse_args()


OUT = Path(
    args.outdir
).resolve()

OUT.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# Read inputs
# ============================================================

repeat_anchor = pd.read_csv(
    args.repeat_heavy_annotated,
    sep="\t"
)

giant_anchor = pd.read_csv(
    args.largest_introns_annotated,
    sep="\t"
)

orthogroups = pd.read_csv(
    args.orthogroups,
    sep="\t"
)


og_cols = detect_orthofinder_columns(
    orthogroups
)

og_lookup = build_orthogroup_lookup(
    orthogroups,
    og_cols
)


repeat_sets = extreme_sets(
    args.repeat_heavy_by_representation
)

giant_sets = extreme_sets(
    args.largest_introns_by_representation
)


# ============================================================
# Cross-representation integration
# ============================================================

repeat_final = add_crossrep_support(
    repeat_anchor,
    og_lookup,
    repeat_sets,
    architecture_name="repeat-heavy"
)

giant_final = add_crossrep_support(
    giant_anchor,
    og_lookup,
    giant_sets,
    architecture_name="largest-intron"
)


# ============================================================
# Write full source tables
# ============================================================

repeat_final.to_csv(
    OUT /
    "phase7_Sapria_repeat_heavy_crossrepresentation.tsv",
    sep="\t",
    index=False
)

giant_final.to_csv(
    OUT /
    "phase7_Sapria_largest_introns_crossrepresentation.tsv",
    sep="\t",
    index=False
)


# ============================================================
# Compact manuscript / supplementary versions
# ============================================================

compact_repeat(
    repeat_final
).to_csv(
    OUT /
    "Table_S_Sapria_repeat_heavy_crossrepresentation.tsv",
    sep="\t",
    index=False
)

compact_giant(
    giant_final
).to_csv(
    OUT /
    "Table_S_Sapria_largest_introns_crossrepresentation.tsv",
    sep="\t",
    index=False
)


# ============================================================
# Summary table
# ============================================================

summary = make_summary(
    repeat_final,
    giant_final
)

summary.to_csv(
    OUT /
    "phase7_Sapria_extreme_gene_crossrepresentation_summary.tsv",
    sep="\t",
    index=False
)


# ============================================================
# Shared-locus overlap between architectures
# ============================================================

repeat_ids = set(
    repeat_final["gene_id"]
)

giant_ids = set(
    giant_final["gene_id"]
)

shared = sorted(
    repeat_ids &
    giant_ids
)

pd.DataFrame(
    {
        "Guo_anchor_gene_id":
            shared
    }
).to_csv(
    OUT /
    "phase7_Sapria_shared_extreme_loci.tsv",
    sep="\t",
    index=False
)


# ============================================================
# Finish
# ============================================================

print()
print(
    "RE-SAPRIA extreme-gene "
    "cross-representation integration complete."
)

print()

print(
    "Biological unit: Sapria himalayana"
)

print(
    "Anchor identifiers: Guo BRAKER models"
)

print()

print(
    "Outputs written to:"
)

print(
    OUT
)

print()

print(
    summary.to_string(
        index=False
    )
)

print()

print(
    "Shared repeat-heavy / giant-intron "
    f"Guo anchor loci: {', '.join(shared)}"
)