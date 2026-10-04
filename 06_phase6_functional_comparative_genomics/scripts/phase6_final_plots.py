from pathlib import Path
import csv
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
FIG = BASE / "figures"
TAB = BASE / "tables"

FIG.mkdir(exist_ok=True)
TAB.mkdir(exist_ok=True)

representations = [
    "Guo",
    "Cai fixed",
    "Cai min1250",
    "Cai Flye–HyPo",
]

# ------------------------------------------------------------------
# 1. OrthoFinder assignment
# ------------------------------------------------------------------

assigned = [88.4, 87.8, 82.1, 77.7]
unassigned = [11.6, 12.2, 17.9, 22.3]

with open(TAB / "phase6_orthofinder_assignment.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["representation", "assigned_pct", "unassigned_pct"])
    for row in zip(representations, assigned, unassigned):
        w.writerow(row)

fig, ax = plt.subplots(figsize=(9.5, 5.7))
ax.barh(representations, assigned, label="Assigned to orthogroup")
ax.barh(representations, unassigned, left=assigned, label="Unassigned")

for y, value in enumerate(assigned):
    ax.text(value / 2, y, f"{value:.1f}%", ha="center", va="center")
    ax.text(
        value + unassigned[y] / 2,
        y,
        f"{unassigned[y]:.1f}%",
        ha="center",
        va="center",
    )

ax.set_xlim(0, 100)
ax.set_xlabel("Representative proteins (%)")
ax.set_title("OrthoFinder assignment across genome representations")
ax.legend(frameon=False, loc="lower right")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()

fig.savefig(
    FIG / "phase6_orthofinder_assignment.png",
    dpi=300,
    bbox_inches="tight",
)
fig.savefig(
    FIG / "phase6_orthofinder_assignment.svg",
    bbox_inches="tight",
)
plt.close(fig)

# ------------------------------------------------------------------
# 2. Orthogroup representation robustness
# ------------------------------------------------------------------

presence = ["1 representation", "2 representations",
            "3 representations", "All 4"]
orthogroups = [1188, 6874, 2970, 8815]

with open(
    TAB / "phase6_orthogroup_representation_robustness.tsv",
    "w",
    newline=""
) as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["number_of_representations", "orthogroups"])
    for row in zip([1, 2, 3, 4], orthogroups):
        w.writerow(row)

fig, ax = plt.subplots(figsize=(8.5, 5.7))
bars = ax.bar(presence, orthogroups)

for bar, value in zip(bars, orthogroups):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:,}",
        ha="center",
        va="bottom",
    )

ax.set_ylabel("Number of orthogroups")
ax.set_title("Orthogroup robustness across genome representations")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()

fig.savefig(
    FIG / "phase6_orthogroup_representation_robustness.png",
    dpi=300,
    bbox_inches="tight",
)
fig.savefig(
    FIG / "phase6_orthogroup_representation_robustness.svg",
    bbox_inches="tight",
)
plt.close(fig)

# ------------------------------------------------------------------
# 3. BUSCO protein mode
# ------------------------------------------------------------------

single = [45.7, 45.7, 44.7, 45.8]
duplicated = [2.3, 2.7, 1.1, 1.4]
fragmented = [4.6, 4.4, 6.5, 4.9]
missing = [47.4, 47.2, 47.6, 48.0]

with open(TAB / "phase6_busco_protein_mode.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow([
        "representation",
        "complete_single_pct",
        "complete_duplicated_pct",
        "fragmented_pct",
        "missing_pct",
    ])
    for row in zip(
        representations,
        single,
        duplicated,
        fragmented,
        missing,
    ):
        w.writerow(row)

fig, ax = plt.subplots(figsize=(9.5, 5.8))

left1 = single
left2 = [a + b for a, b in zip(single, duplicated)]
left3 = [a + b + c for a, b, c in zip(single, duplicated, fragmented)]

ax.barh(representations, single, label="Complete single-copy")
ax.barh(representations, duplicated, left=single,
        label="Complete duplicated")
ax.barh(representations, fragmented, left=left2,
        label="Fragmented")
ax.barh(representations, missing, left=left3,
        label="Missing")

for y, value in enumerate(single):
    ax.text(value / 2, y, f"{value:.1f}%", ha="center", va="center")

ax.set_xlim(0, 100)
ax.set_xlabel("BUSCOs (%)")
ax.set_title(
    "BUSCO protein-mode completeness — embryophyta_odb10 (n=1,614)"
)
ax.legend(frameon=False, bbox_to_anchor=(1.02, 1), loc="upper left")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()

fig.savefig(
    FIG / "phase6_busco_protein_mode.png",
    dpi=300,
    bbox_inches="tight",
)
fig.savefig(
    FIG / "phase6_busco_protein_mode.svg",
    bbox_inches="tight",
)
plt.close(fig)

print("Phase 6 final figures and source tables written.")
