# RE-SAPRIA for High School 🌺🧬
## A genome assembly is not the genome itself


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

## 1. The RE-SAPRIA question

Two independent genome studies of *Sapria himalayana* produced dramatically different representations.

| Genome representation | Assembly span |
|---|---:|
| **Guo published** | **2.061 Gb** |
| **Cai published** | **1.276 Gb** |
| **Cai Flye–HyPo** | **0.966 Gb** |

Largest difference ≈ **1.09 Gb**.

The testable question is:

> **How much Cai–Guo divergence is biological, and how much is reconstruction-dependent?**

## 2. Assembly metrics must be combined

Published Cai:

- 128,027 scaffold records;
- 216,625 gap-free contigs in BUSCO assembly statistics;
- scaffold N50 ≈ **952 kb**;
- contig N50 ≈ **19 kb**;
- gap content ≈ **7.319%**.

Published Guo:

- 18,718 scaffolds;
- 26,955 contigs;
- scaffold N50 ≈ **251 kb**;
- contig N50 ≈ **106 kb**;
- gap content ≈ **1.865%**.

Cai therefore has a higher scaffold N50 but much lower gap-free contiguity.

## 3. Read-backed evidence

### ONT
- primary mapping: **92.68%**
- Guo breadth: **88.11%**
- mean depth: **~14.4×**

### Illumina
- primary mapping: **97.87%**
- Guo breadth: **~92.93%**
- mean depth: **~41.94×**

Assembly-span difference cannot be translated directly into biological genome-size difference.

## 4. Variant evidence

| Variant | Count |
|---|---:|
| Total high-confidence small variants | **4,535,955** |
| SNP | **3,704,632** |
| Indel | **831,323** |
| Homozygous-alternate | **1,158,638** |

ONT also produced **54,117 PASS structural-discrepancy calls**.

“Discrepancy” is deliberately conservative because the signal can mix true variation, repeat ambiguity, assembly differences, and alignment behavior.

## 5. Cai fixed-on-Guo as a control

The Guo backbone is retained while confident Cai homozygous-alternate alleles are introduced.

This changes **sequence state** while keeping **large-scale structure** mostly constant.

| Representation | Mean HISAT2 alignment |
|---|---:|
| Guo | **96.92%** |
| Cai fixed-on-Guo | **96.79%** |
| Cai Flye–HyPo | **95.88%** |
| Cai published | **95.24%** |
| Cai min1250 | **95.15%** |

The Guo → Cai-fixed change is small; shifts toward independently reconstructed Cai genomes are larger.

## 6. BUSCO: span ≠ conserved gene space

| Representation | AUGUSTUS Complete | Miniprot Complete |
|---|---:|---:|
| Guo | **49.7%** | **51.2%** |
| Cai fixed-on-Guo | **49.8%** | **51.4%** |
| Cai published | **47.5%** | **49.3%** |
| Cai Flye–HyPo | **47.3%** | **50.5%** |

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Assembly span changes by >2×, while complete BUSCO changes by only a few percentage points.

Do not overinterpret missing BUSCOs: they can reflect true loss, divergence, fragmentation, giant gene architecture, or predictor limitations.

## 7. min1250 as a technical control

Published Cai has **128,027** FASTA records.

After removing scaffolds shorter than 1,250 bp:

- **99,251 records**
- **97.49%** sequence retained
- AUGUSTUS complete BUSCOs: unchanged
- Miniprot complete BUSCOs: **795 → 794**
- RNA-seq mapping: **95.24% → 95.15%**

This is a technical rescue, not evidence that the assembly became biologically “better.”

## 8. OGI practice questions

1. Why can scaffold N50 and contig N50 tell different stories?
2. Why is Cai fixed-on-Guo a useful control?
3. How can high mapping coexist with very different assembly spans?
4. Why are two accessions insufficient for population genomics?
5. Why does ~50% complete BUSCO not automatically mean “half of all *Sapria* genes are gone”?

> **Comparative genomics is not only about obtaining an answer. It is about testing whether the answer survives changes in representation and method.**


## Primary sources

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria
