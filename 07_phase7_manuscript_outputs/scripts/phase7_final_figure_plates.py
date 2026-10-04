from pathlib import Path
import csv
import matplotlib.pyplot as plt

# ============================================================
# RE-SAPRIA — Phase 7 final manuscript figure plates
# Frozen analytical synthesis, 2026-10-04
#
# Intended repository placement:
# 07_phase7_manuscript_outputs/scripts/phase7_final_figure_plates.py
# ============================================================

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
FIG = BASE / "figures"
TAB = BASE / "tables"

FIG.mkdir(parents=True, exist_ok=True)
TAB.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "figure.titlesize": 13,
})

SHORT4 = ["Guo", "Cai fixed", "Cai min1250", "Cai Flye–HyPo"]
SHORT5 = ["Guo", "Cai fixed", "Cai published", "Cai min1250", "Cai Flye–HyPo"]


def panel(ax, letter):
    ax.text(
        -0.10, 1.06, letter,
        transform=ax.transAxes,
        fontsize=14,
        fontweight="bold",
        va="top",
    )


def clean(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def save_plate(fig, basename):
    fig.tight_layout()
    fig.savefig(FIG / f"{basename}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG / f"{basename}.svg", bbox_inches="tight")
    fig.savefig(FIG / f"{basename}.pdf", bbox_inches="tight")
    plt.close(fig)


def write_tsv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(header)
        w.writerows(rows)


# ============================================================
# MASTER REPRESENTATION DATA
# ============================================================

assembly_span_mb = {
    "Guo": 2060.974854,
    "Cai fixed": 2060.941893,
    "Cai published": 1276.270856,
    "Cai min1250": 1244.196188,
    "Cai Flye–HyPo": 966.497149,
}

n_bases_mb = {
    "Guo": 38.428485,
    "Cai fixed": 38.428485,
    "Cai published": 93.416560,
    "Cai min1250": 92.847230,
    "Cai Flye–HyPo": 0.0,
}

repeat_pct_non_n = {
    "Guo": 90.02,
    "Cai fixed": 90.35,
    "Cai published": 86.81,
    "Cai min1250": 87.00,
    "Cai Flye–HyPo": 84.32,
}

genome_busco_miniprot_complete = {
    "Guo": 51.2,
    "Cai fixed": 51.4,
    "Cai published": 49.3,
    "Cai min1250": 49.2,
    "Cai Flye–HyPo": 50.5,
}

braker_genes = {
    "Guo": 29792,
    "Cai fixed": 29887,
    "Cai min1250": 20149,
    "Cai Flye–HyPo": 19430,
}

protein_busco_complete = {
    "Guo": 48.0,
    "Cai fixed": 48.4,
    "Cai min1250": 45.8,
    "Cai Flye–HyPo": 47.1,
}

strict_orf = {
    "Guo": 92.94,
    "Cai fixed": 91.42,
    "Cai min1250": 84.37,
    "Cai Flye–HyPo": 96.84,
}

orthogroup_assigned = {
    "Guo": 88.4,
    "Cai fixed": 87.8,
    "Cai min1250": 82.1,
    "Cai Flye–HyPo": 77.7,
}

master_rows = []

for rep in SHORT5:
    non_n = assembly_span_mb[rep] - n_bases_mb[rep]
    repeat_mb = non_n * repeat_pct_non_n[rep] / 100
    nonrepeat_mb = non_n - repeat_mb

    master_rows.append([
        rep,
        assembly_span_mb[rep],
        n_bases_mb[rep],
        non_n,
        repeat_pct_non_n[rep],
        repeat_mb,
        nonrepeat_mb,
        braker_genes.get(rep, "NA"),
        genome_busco_miniprot_complete[rep],
        protein_busco_complete.get(rep, "NA"),
        strict_orf.get(rep, "NA"),
        orthogroup_assigned.get(rep, "NA"),
    ])

write_tsv(
    TAB / "phase7_representation_master_summary.tsv",
    [
        "representation",
        "assembly_span_Mb",
        "N_bases_Mb",
        "non_N_span_Mb",
        "repeat_pct_non_N",
        "repeat_span_Mb",
        "nonrepeat_span_Mb",
        "BRAKER_genes",
        "genome_BUSCO_Miniprot_complete_pct",
        "protein_BUSCO_complete_pct",
        "strict_complete_ORF_proxy_pct",
        "orthogroup_assigned_pct",
    ],
    master_rows,
)


# ============================================================
# FIGURE 1
# Genome representation paradox
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

# A — assembly span
ax = axes[0]
vals = [assembly_span_mb[r] / 1000 for r in SHORT5]
bars = ax.barh(SHORT5, vals)
for b, v in zip(bars, vals):
    ax.text(v + 0.025, b.get_y() + b.get_height()/2,
            f"{v:.2f}", va="center")
ax.set_xlabel("Assembly span (Gb)")
ax.set_title("Genome representations")
clean(ax)
panel(ax, "A")

# B — Cai reads mapped to Guo
ax = axes[1]

read_types = ["ONT", "Illumina"]
primary_mapping = [92.68, 97.87]
reference_breadth = [88.11, 92.93]

x = range(len(read_types))
width = 0.35

ax.bar([i - width/2 for i in x], primary_mapping,
       width=width, label="Primary mapping")
ax.bar([i + width/2 for i in x], reference_breadth,
       width=width, label="Reference breadth")

ax.set_xticks(list(x), read_types)
ax.set_ylim(0, 100)
ax.set_ylabel("Percent")
ax.set_title("Cai reads support Guo")
ax.legend(frameon=False)
clean(ax)
panel(ax, "B")

# C — genome BUSCO Miniprot
ax = axes[2]

vals = [genome_busco_miniprot_complete[r] for r in SHORT5]
bars = ax.bar(SHORT5, vals)
ax.set_ylim(40, 55)
ax.set_ylabel("Complete BUSCOs (%)")
ax.set_title("Conserved gene recovery\n(genome mode, Miniprot)")
ax.tick_params(axis="x", rotation=35)

for b, v in zip(bars, vals):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 0.2,
        f"{v:.1f}",
        ha="center",
        va="bottom",
    )

clean(ax)
panel(ax, "C")

fig.suptitle(
    "Figure 1. Large differences in represented genome span coexist with strong read support and similar conserved-gene recovery",
    y=1.03,
)

save_plate(fig, "Fig1_genome_representation_paradox")

write_tsv(
    TAB / "Fig1_source_data.tsv",
    ["metric", "representation_or_read_type", "value", "unit"],
    [
        *[
            ["assembly_span", r, assembly_span_mb[r], "Mb"]
            for r in SHORT5
        ],
        ["ONT_primary_mapping", "ONT", 92.68, "percent"],
        ["ONT_reference_breadth", "ONT", 88.11, "percent"],
        ["Illumina_primary_mapping", "Illumina", 97.87, "percent"],
        ["Illumina_reference_breadth", "Illumina", 92.93, "percent"],
        *[
            ["genome_BUSCO_Miniprot_complete", r,
             genome_busco_miniprot_complete[r], "percent"]
            for r in SHORT5
        ],
    ],
)


# ============================================================
# FIGURE 2
# Repeat-rich sequence space
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# A — repeat/non-repeat non-N sequence
ax = axes[0]

repeat_values = []
nonrepeat_values = []

for rep in SHORT5:
    non_n = assembly_span_mb[rep] - n_bases_mb[rep]
    repeat_mb = non_n * repeat_pct_non_n[rep] / 100
    repeat_values.append(repeat_mb / 1000)
    nonrepeat_values.append((non_n - repeat_mb) / 1000)

ax.barh(SHORT5, repeat_values, label="Repeat-masked")
ax.barh(
    SHORT5,
    nonrepeat_values,
    left=repeat_values,
    label="Non-repeat",
)

ax.set_xlabel("Non-N sequence (Gb)")
ax.set_title("Repeat versus non-repeat represented sequence")
ax.legend(frameon=False)
clean(ax)
panel(ax, "A")

# B — fraction of span discrepancy associated with repeats
ax = axes[1]

comparisons = [
    "Guo vs Cai published",
    "Guo vs Cai min1250",
    "Guo vs Flye–HyPo",
    "Cai published vs Flye–HyPo",
]

repeat_share = [94.54, 94.01, 95.23, 97.91]

bars = ax.barh(comparisons, repeat_share)

for b, v in zip(bars, repeat_share):
    ax.text(
        v - 0.7,
        b.get_y() + b.get_height()/2,
        f"{v:.2f}%",
        ha="right",
        va="center",
    )

ax.set_xlim(85, 100)
ax.set_xlabel("Span discrepancy associated with repeat-masked sequence (%)")
ax.set_title("Representation-level span differences")
clean(ax)
panel(ax, "B")

fig.suptitle(
    "Figure 2. Genome-span disagreement is concentrated in repeat-rich sequence",
    y=1.02,
)

save_plate(fig, "Fig2_repeat_space")

repeat_rows = []

for rep in SHORT5:
    non_n = assembly_span_mb[rep] - n_bases_mb[rep]
    repeat_mb = non_n * repeat_pct_non_n[rep] / 100
    nonrepeat_mb = non_n - repeat_mb

    repeat_rows.append([
        rep,
        non_n,
        repeat_pct_non_n[rep],
        repeat_mb,
        nonrepeat_mb,
    ])

write_tsv(
    TAB / "Fig2_repeat_space_source_data.tsv",
    [
        "representation",
        "non_N_span_Mb",
        "repeat_pct_non_N",
        "repeat_span_Mb",
        "nonrepeat_span_Mb",
    ],
    repeat_rows,
)

write_tsv(
    TAB / "Fig2_span_discrepancy_source_data.tsv",
    ["comparison", "repeat_share_of_span_difference_pct"],
    list(zip(comparisons, repeat_share)),
)


# ============================================================
# FIGURE 3
# Repeat-expanded gene space
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

intron_ge10_pct = [9.13, 10.02, 11.18, 11.44]
bp_inside_ge10_pct = [66.80, 70.57, 71.74, 72.08]

intron_repeat_pct = [73.45, 76.30, 74.20, 75.49]
cds_repeat_pct = [14.12, 17.41, 13.18, 11.45]

rho = [0.702, 0.658, 0.716, 0.748]

x = range(len(SHORT4))
width = 0.36

# A
ax = axes[0]

ax.bar(
    [i - width/2 for i in x],
    intron_ge10_pct,
    width=width,
    label="Introns ≥10 kb",
)

ax.bar(
    [i + width/2 for i in x],
    bp_inside_ge10_pct,
    width=width,
    label="Intronic bp within ≥10-kb introns",
)

ax.set_xticks(list(x), SHORT4, rotation=35, ha="right")
ax.set_ylabel("Percent")
ax.set_title("Few long introns contain most intronic sequence")
ax.legend(frameon=False)
clean(ax)
panel(ax, "A")

# B
ax = axes[1]

ax.bar(
    [i - width/2 for i in x],
    intron_repeat_pct,
    width=width,
    label="Intronic sequence",
)

ax.bar(
    [i + width/2 for i in x],
    cds_repeat_pct,
    width=width,
    label="CDS sequence",
)

ax.set_xticks(list(x), SHORT4, rotation=35, ha="right")
ax.set_ylabel("Repeat-overlapped sequence (%)")
ax.set_title("Repeats preferentially occupy introns")
ax.legend(frameon=False)
clean(ax)
panel(ax, "B")

# C
ax = axes[2]

bars = ax.bar(SHORT4, rho)

for b, v in zip(bars, rho):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 0.012,
        f"{v:.3f}",
        ha="center",
    )

ax.set_ylim(0, 0.85)
ax.set_ylabel("Spearman ρ")
ax.set_title("Intron length versus repeat fraction")
ax.tick_params(axis="x", rotation=35)
clean(ax)
panel(ax, "C")

fig.suptitle(
    "Figure 3. Repeat expansion penetrates gene space through long introns",
    y=1.03,
)

save_plate(fig, "Fig3_repeat_expanded_gene_space")

write_tsv(
    TAB / "Fig3_source_data.tsv",
    [
        "representation",
        "introns_ge10kb_pct",
        "intronic_bp_within_ge10kb_pct",
        "intron_repeat_overlap_pct",
        "CDS_repeat_overlap_pct",
        "spearman_rho_intron_length_repeat_fraction",
    ],
    [
        [
            SHORT4[i],
            intron_ge10_pct[i],
            bp_inside_ge10_pct[i],
            intron_repeat_pct[i],
            cds_repeat_pct[i],
            rho[i],
        ]
        for i in range(4)
    ],
)


# ============================================================
# FIGURE 4
# Repeat visibility destabilizes ab initio prediction
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))

# A — genes
ax = axes[0]

conditions = ["Softmasked", "Unmasked"]
gene_counts = [30906, 106782]

bars = ax.bar(conditions, gene_counts)

for b, v in zip(bars, gene_counts):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 1800,
        f"{v:,}",
        ha="center",
    )

ax.set_ylabel("Predicted genes")
ax.set_title("AUGUSTUS gene models")
clean(ax)
panel(ax, "A")

# B — CDS features
ax = axes[1]

cds_features = [153165, 434794]

bars = ax.bar(conditions, cds_features)

for b, v in zip(bars, cds_features):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 7000,
        f"{v:,}",
        ha="center",
    )

ax.set_ylabel("CDS features")
ax.set_title("AUGUSTUS CDS predictions")
clean(ax)
panel(ax, "B")

# C — unmasked-only prediction space
ax = axes[2]

labels = [
    "≥50% gene-span\nrepeat overlap",
    "RNA-BRAKER\nsame-strand overlap",
]

values = [97.41, 6.21]

bars = ax.bar(labels, values)

for b, v in zip(bars, values):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 1.3,
        f"{v:.2f}%",
        ha="center",
    )

ax.set_ylim(0, 105)
ax.set_ylabel("Models (%)")
ax.set_title("60,530 unmasked-only AUGUSTUS models")
clean(ax)
panel(ax, "C")

fig.suptitle(
    "Figure 4. Exposing repetitive sequence greatly expands ab initio prediction space",
    y=1.03,
)

save_plate(fig, "Fig4_annotation_sensitivity")

write_tsv(
    TAB / "Fig4_source_data.tsv",
    [
        "metric",
        "softmasked",
        "unmasked_or_unmasked_only",
    ],
    [
        ["AUGUSTUS_genes", 30906, 106782],
        ["AUGUSTUS_CDS_features", 153165, 434794],
        ["unmasked_only_models", "NA", 60530],
        ["unmasked_only_gene_repeat_ge50_pct", "NA", 97.41],
        ["unmasked_only_RNA_BRAKER_overlap_pct", "NA", 6.21],
    ],
)


# ============================================================
# FIGURE 5
# Stable coding core
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(12.5, 9))

# A — standardized BRAKER gene counts
ax = axes[0][0]

gene_vals = [braker_genes[r] for r in SHORT4]
bars = ax.bar(SHORT4, gene_vals)

for b, v in zip(bars, gene_vals):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 400,
        f"{v:,}",
        ha="center",
    )

ax.set_ylabel("BRAKER genes")
ax.set_title("Standardized gene annotation")
ax.tick_params(axis="x", rotation=30)
clean(ax)
panel(ax, "A")

# B — genome versus protein BUSCO
ax = axes[0][1]

genome_vals = [
    genome_busco_miniprot_complete[r]
    for r in SHORT4
]

protein_vals = [
    protein_busco_complete[r]
    for r in SHORT4
]

x = range(4)
width = 0.36

ax.bar(
    [i - width/2 for i in x],
    genome_vals,
    width=width,
    label="Genome mode — Miniprot",
)

ax.bar(
    [i + width/2 for i in x],
    protein_vals,
    width=width,
    label="Representative proteins",
)

ax.set_xticks(list(x), SHORT4, rotation=30, ha="right")
ax.set_ylim(40, 55)
ax.set_ylabel("Complete BUSCOs (%)")
ax.set_title("Genome-detectable versus annotated conserved genes")
ax.legend(frameon=False)
clean(ax)
panel(ax, "B")

# C — OrthoFinder assignment
ax = axes[1][0]

assigned = [
    orthogroup_assigned[r]
    for r in SHORT4
]

unassigned = [
    100 - v for v in assigned
]

ax.barh(SHORT4, assigned, label="Assigned")
ax.barh(
    SHORT4,
    unassigned,
    left=assigned,
    label="Unassigned",
)

ax.set_xlim(0, 100)
ax.set_xlabel("Representative proteins (%)")
ax.set_title("Cross-representation orthogroup assignment")
ax.legend(frameon=False)
clean(ax)
panel(ax, "C")

# D — representation robustness
ax = axes[1][1]

presence = [
    "1 representation",
    "2 representations",
    "3 representations",
    "All 4",
]

og_counts = [1188, 6874, 2970, 8815]

bars = ax.bar(presence, og_counts)

for b, v in zip(bars, og_counts):
    ax.text(
        b.get_x() + b.get_width()/2,
        v + 120,
        f"{v:,}",
        ha="center",
    )

ax.set_ylabel("Orthogroups")
ax.set_title("Orthogroup persistence")
ax.tick_params(axis="x", rotation=25)
clean(ax)
panel(ax, "D")

fig.suptitle(
    "Figure 5. A comparatively stable coding core persists across alternative genome representations",
    y=1.01,
)

save_plate(fig, "Fig5_stable_coding_core")

write_tsv(
    TAB / "Fig5_source_data.tsv",
    [
        "representation",
        "BRAKER_genes",
        "genome_BUSCO_Miniprot_complete_pct",
        "protein_BUSCO_complete_pct",
        "orthogroup_assigned_pct",
    ],
    [
        [
            r,
            braker_genes[r],
            genome_busco_miniprot_complete[r],
            protein_busco_complete[r],
            orthogroup_assigned[r],
        ]
        for r in SHORT4
    ],
)


# ============================================================
# HYPOTHESIS SUMMARY
# ============================================================

write_tsv(
    TAB / "phase7_hypothesis_summary.tsv",
    [
        "hypothesis",
        "status",
        "phase7_summary",
    ],
    [
        [
            "Biological divergence versus reconstruction",
            "Supported",
            "Observed Cai–Guo differences reflect genuine sequence divergence together with reconstruction-dependent effects.",
        ],
        [
            "Repeat architecture shapes annotation",
            "Supported",
            "Repeat visibility and genome representation materially alter the prediction landscape.",
        ],
        [
            "Giant introns represent repeat-expanded gene space",
            "Structurally supported",
            "Long introns and their strong repeat association persist across alternative genome representations; broader function remains unresolved.",
        ],
    ],
)


# ============================================================
# FIGURE MANIFEST
# ============================================================

write_tsv(
    TAB / "phase7_figure_manifest.tsv",
    [
        "figure",
        "basename",
        "principal_message",
        "source_phases",
    ],
    [
        [
            "Figure 1",
            "Fig1_genome_representation_paradox",
            "Large differences in represented genome span coexist with strong Cai-read support for Guo and broadly similar conserved-gene recovery.",
            "Phases 2–3",
        ],
        [
            "Figure 2",
            "Fig2_repeat_space",
            "Most representation-level assembly-span disagreement is concentrated in repeat-rich sequence.",
            "Phase 4",
        ],
        [
            "Figure 3",
            "Fig3_repeat_expanded_gene_space",
            "Long introns contain disproportionate intronic sequence and are strongly repeat-associated.",
            "Phases 5A–5B",
        ],
        [
            "Figure 4",
            "Fig4_annotation_sensitivity",
            "Repeat visibility greatly expands repeat-associated ab initio prediction space.",
            "Phase 5B",
        ],
        [
            "Figure 5",
            "Fig5_stable_coding_core",
            "Conserved and cross-representation coding space is substantially more stable than whole-genome representation.",
            "Phase 6",
        ],
    ],
)

print()
print("RE-SAPRIA Phase 7 figure plates complete.")
print(f"Figures: {FIG}")
print(f"Tables : {TAB}")
print()
print("Generated:")
for p in sorted(FIG.glob("Fig*")):
    print(" ", p.name)
