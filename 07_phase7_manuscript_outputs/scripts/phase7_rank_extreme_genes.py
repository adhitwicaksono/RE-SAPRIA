#!/usr/bin/env python3

import argparse
from pathlib import Path
import pandas as pd


parser = argparse.ArgumentParser()

parser.add_argument(
    "--genes",
    nargs="+",
    required=True,
    help="Full Phase 5B *.genes.tsv.gz files"
)

parser.add_argument(
    "--n",
    type=int,
    default=20
)

parser.add_argument(
    "--anchor",
    default="Guo published"
)

parser.add_argument(
    "--outdir",
    default="phase7_extreme_genes"
)

args = parser.parse_args()


# ------------------------------------------------------------
# Load
# ------------------------------------------------------------

frames = []

for f in args.genes:
    x = pd.read_csv(
        f,
        sep="\t",
        compression="infer"
    )
    frames.append(x)

df = pd.concat(
    frames,
    ignore_index=True
)


# ------------------------------------------------------------
# Derived fields
# ------------------------------------------------------------

df["gene_repeat_pct"] = (
    100 * df["gene_repeat_fraction"]
)

df["cds_repeat_pct"] = (
    100 * df["cds_repeat_fraction"]
)

df["intron_repeat_pct"] = (
    100 * df["intron_repeat_fraction"]
)

df["longest_intron_repeat_pct"] = (
    100 * df["longest_intron_repeat_fraction"]
)

# Two deliberately separate definitions:
df["longest_intron_repeat_majority"] = (
    df["longest_intron_repeat_fraction"] >= 0.50
)

df["longest_intron_highly_repeat_laden"] = (
    df["longest_intron_repeat_fraction"] >= 0.75
)


# ------------------------------------------------------------
# Structurally complete representative models only
# ------------------------------------------------------------

complete = df[
    (df["complete_start_stop_proxy"] == 1) &
    (df["intron_count"] > 0)
].copy()


# ------------------------------------------------------------
# A. Repeat-heavy HOST-gene candidates
#
# Rank by absolute intronic repeat burden.
#
# CDS repeat <=10% prevents tiny TE-like/repeat-derived ORFs from
# trivially winning solely because they are 100% repetitive.
# ------------------------------------------------------------

repeat_heavy = complete[
    complete["cds_repeat_fraction"] <= 0.10
].copy()

repeat_heavy = repeat_heavy.sort_values(
    [
        "intron_repeat_bp",
        "intron_repeat_fraction",
        "longest_intron_bp",
        "gene_id"
    ],
    ascending=[
        False,
        False,
        False,
        True
    ]
)


# ------------------------------------------------------------
# B. Largest introns
#
# No repeat filter here.
# We want repeat enrichment to be an OBSERVATION, not a criterion.
# ------------------------------------------------------------

largest_introns = complete.sort_values(
    [
        "longest_intron_bp",
        "longest_intron_repeat_fraction",
        "gene_id"
    ],
    ascending=[
        False,
        False,
        True
    ]
)


# ------------------------------------------------------------
# Output columns
# ------------------------------------------------------------

cols = [
    "representation",
    "gene_id",
    "transcript_id",
    "seqid",

    "gene_span_bp",
    "gene_repeat_pct",

    "intron_count",
    "intron_bp",
    "intron_repeat_bp",
    "intron_repeat_pct",

    "longest_intron_bp",
    "longest_intron_repeat_pct",
    "longest_intron_repeat_majority",
    "longest_intron_highly_repeat_laden",

    "cds_bp",
    "cds_repeat_pct",

    "complete_start_stop_proxy"
]


outdir = Path(args.outdir)
outdir.mkdir(
    parents=True,
    exist_ok=True
)


# ------------------------------------------------------------
# Per-representation Top N
# ------------------------------------------------------------

repeat_by_rep = (
    repeat_heavy
    .groupby(
        "representation",
        group_keys=False
    )
    .head(args.n)
)

largest_by_rep = (
    largest_introns
    .groupby(
        "representation",
        group_keys=False
    )
    .head(args.n)
)


repeat_by_rep[cols].to_csv(
    outdir /
    f"top{args.n}_repeat_heavy_by_representation.tsv",
    sep="\t",
    index=False
)

largest_by_rep[cols].to_csv(
    outdir /
    f"top{args.n}_largest_introns_by_representation.tsv",
    sep="\t",
    index=False
)


# ------------------------------------------------------------
# Manuscript anchor = Guo
# ------------------------------------------------------------

anchor_repeat = repeat_heavy[
    repeat_heavy["representation"] ==
    args.anchor
].head(args.n)

anchor_largest = largest_introns[
    largest_introns["representation"] ==
    args.anchor
].head(args.n)


anchor_repeat[cols].to_csv(
    outdir /
    f"top{args.n}_repeat_heavy_Guo.tsv",
    sep="\t",
    index=False
)

anchor_largest[cols].to_csv(
    outdir /
    f"top{args.n}_largest_introns_Guo.tsv",
    sep="\t",
    index=False
)


# ------------------------------------------------------------
# Summary: are the largest introns repeat-laden?
# ------------------------------------------------------------

rows = []

for rep, sub in largest_by_rep.groupby(
    "representation"
):

    rows.append({

        "representation":
            rep,

        "n":
            len(sub),

        "largest_intron_bp":
            int(
                sub[
                    "longest_intron_bp"
                ].max()
            ),

        "median_longest_intron_repeat_pct":
            sub[
                "longest_intron_repeat_pct"
            ].median(),

        "n_repeat_majority_ge50pct":
            int(
                sub[
                    "longest_intron_repeat_majority"
                ].sum()
            ),

        "n_highly_repeat_laden_ge75pct":
            int(
                sub[
                    "longest_intron_highly_repeat_laden"
                ].sum()
            )
    })


pd.DataFrame(rows).to_csv(
    outdir /
    "largest_intron_repeat_summary.tsv",
    sep="\t",
    index=False
)


print()
print("Done.")
print()

print(
    f"Top {args.n} repeat-heavy host-gene "
    "candidates:"
)

print(
    outdir /
    f"top{args.n}_repeat_heavy_Guo.tsv"
)

print()

print(
    f"Top {args.n} largest-intron genes:"
)

print(
    outdir /
    f"top{args.n}_largest_introns_Guo.tsv"
)