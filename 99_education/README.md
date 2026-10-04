# 99_education — RE-SAPRIA for Everyone 🌺🧬

This folder is the educational entrance to RE-SAPRIA.

The goal: **make the extreme genomics of *Sapria himalayana* astonishing without sacrificing scientific accuracy.**


## Before we begin: what is *Sapria*? And who are “Cai” and “Guo”? 🌺

If you already know **Rafflesia**, you have the perfect starting point.

*Rafflesia* and *Sapria* are not the same plant, but both belong to the family **Rafflesiaceae**—a remarkable group of parasitic flowering plants with extremely reduced vegetative bodies that spend much of their lives hidden inside host tissue.

*Rafflesia* is much more famous because of its enormous flowers. *Sapria himalayana* is a less familiar relative, but it has become one of the best genomic windows into how extreme endoparasitism can reshape a flowering plant.

And one important clarification:

> **“Cai” and “Guo” are not species names.**

In RE-SAPRIA, **Cai** is shorthand for the dataset/assembly from the **Liming Cai et al. (2021)** study. **Guo** is shorthand for the dataset/assembly from the **Xuelian Guo et al. (2023)** study.

So we are comparing **two different scientific studies of the same species: *Sapria himalayana*.**

## Two scientific journeys into the *Sapria* genome

### The Cai journey: from an almost invisible plant body to a genome

Charles C. Davis's group at Harvard had studied Rafflesiaceae for years. One of the major challenges was easy to state but difficult to solve: **how do you build a usable genome for a plant that spends most of its life hidden inside another plant?**

Liming Cai made *Sapria himalayana* a major part of his doctoral research. Together with Charles Davis, Timothy Sackton, Harvard bioinformaticians, and collaborators in Southeast Asia, the 2021 study produced one of the most complete genomic views then available for a major Rafflesiaceae lineage.

The study revealed something remarkable: *Sapria* had lost many genes that are normally deeply conserved in flowering plants, yet its genome remained large and structurally unusual. The team also found evidence of horizontal gene transfer from host lineages.

### The Guo journey: returning to the same species with a new dataset

Two years later, **Xuelian Guo** and colleagues from the Chinese Academy of Sciences, Novogene, and collaborating institutions published **another independent genome assembly of *S. himalayana***.

The Guo study was not simply a repeat of Cai. It used a different dataset and emphasized questions including flower development, flowering time, metabolism, defense, gene loss, and horizontal gene transfer.

And that is where RE-SAPRIA finds its new question:

> **If two teams study the same species but produce very different genome representations, which differences reflect biology—and which reflect reconstruction?**

## Choose your level

| Audience | File |
|---|---|
| **Elementary School** | [`README_ELEMENTARY.md`](README_ELEMENTARY.md) |
| **Middle School** | [`README_MIDDLE_SCHOOL.md`](README_MIDDLE_SCHOOL.md) |
| **High School** | [`README_HIGH_SCHOOL.md`](README_HIGH_SCHOOL.md) |
| **General / Lay Readers** | [`README_LAYPEOPLE.md`](README_LAYPEOPLE.md) |
| **Indonesian index** | [`README_ID.md`](README_ID.md) |

## Current data version

This educational set reflects the **analytically frozen RE-SAPRIA synthesis
through Phase 7 (2026-10-04)**.

The project began from the striking disagreement between published Cai and Guo
assemblies, but its final biological focus is broader: **the genome architecture
of *Sapria himalayana* across alternative representations.**

## What RE-SAPRIA found

Across the principal genome representations, approximately **84–90% of non-N
sequence is repeat-masked**. Approximately **94–98% of the major differences in
represented genome span are associated with repeat-rich sequence**.

Repeats also penetrate gene space. Only about **9–11% of representative introns
are at least 10 kb long, yet these long introns contain about 67–72% of all
intronic sequence**. Introns are far more repeat-overlapped than coding sequence.

Gene prediction is therefore strongly affected by how repeats are treated.
Soft-masking is supported as the default substrate for primary structural gene
annotation in *S. himalayana*, while unmasked annotation is useful as a
sensitivity control.

Despite large changes in represented genome span and predicted gene number,
conserved protein-coding recovery remains comparatively stable across
representations.

## The one-sentence core idea

> **In *Sapria himalayana*, repeat-rich DNA makes genome reconstruction and gene prediction unusually sensitive, yet a recognizable conserved coding core persists across alternative representations.**


## Primary sources

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria

## RE-SAPRIA project synthesis

- [Phase 7 — final analytical synthesis](../07_phase7_manuscript_outputs/README.md)
- Phase 4 repeat annotation archive: https://doi.org/10.5281/zenodo.23105473
- Phase 5A standardized annotation archive: https://doi.org/10.5281/zenodo.23072450
