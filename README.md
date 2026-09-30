# RE-SAPRIA

**RE-SAPRIA** is a reproducible comparative-genomics project centered on two published *Sapria himalayana* genome datasets:

- **Cai dataset (Thailand accession)** — Oxford Nanopore long reads with a published scaffolded assembly.
- **Guo dataset (China accession)** — PacBio Sequel II long-read data with Illumina data and a published scaffolded assembly.

The project asks a simple but difficult question:

> **How much of the apparent genomic divergence between Cai and Guo reflects genuine biological variation, and how much reflects reconstruction- and annotation-dependent differences in an extremely repeat-rich genome?**

RE-SAPRIA therefore does not treat either published assembly as unquestioned ground truth. Instead, multiple genome representations are compared under harmonized QC, repeat annotation, read mapping, variant calling, and gene-annotation workflows.

---

## Current genome representations

The main analytical framework currently uses the following genome representations:

| Representation | Description | Role |
|---|---|---|
| **Guo published** | Published Guo assembly, header-cleaned | Guo structural reference |
| **Cai published** | Published Cai assembly, header-cleaned | Historical Cai representation |
| **Cai min1250** | Published Cai assembly with scaffolds <1,250 bp removed | Published-Cai representation compatible with downstream annotation workflows |
| **Cai Flye–HyPo** | Independent Cai ONT reassembly polished with Illumina using HyPo | Independent Cai reconstruction |
| **Cai fixed-on-Guo** | Guo backbone carrying confident homozygous-alternate Cai alleles | Sequence-divergence control |

The **Cai fixed-on-Guo** genome is an analytical pseudogenome and must not be interpreted as an independently assembled Cai genome.

A parallel Guo Flye reconstruction was attempted but did not produce a usable completed assembly; the published Guo assembly therefore remains the Guo structural representation used downstream.

---

## The Central Hypotheses

RE-SAPRIA is organized around three linked hypotheses:

**1. Biological divergence versus genome reconstruction**

The striking differences between the Cai and Guo *Sapria himalayana* genome representations reflect a combination of genuine biological divergence and reconstruction-dependent effects, rather than biological variation alone. Differences in assembly span, sequence recovery, structural organization, and apparent gene content therefore need to be tested against independent read support and alternative genome representations before being interpreted biologically.

**2. Repeat architecture shapes genome annotation**

The extremely repeat-rich architecture of *S. himalayana* makes gene prediction unusually sensitive to repeat treatment and annotation strategy. Exposed repetitive sequence can generate inflated or fragmented gene predictions, whereas inappropriate masking may also obscure genuine repeat-containing genes. Consequently, repeat-aware annotation supported by transcriptomic and comparative evidence is required before apparent gene gain, gene loss, or structural novelty can be treated as biological.

**3. Giant introns represent repeat-expanded gene space**

The unusually large introns found in *S. himalayana* are hypothesized to arise substantially through repeat accumulation within otherwise genuine genes, creating an expanded gene-space architecture that is particularly vulnerable to assembly and annotation errors. These giant introns may also preserve biologically informative sequence—including transposable-element relics, duplicated fragments, regulatory elements, conserved noncoding sequence, or other functional material—but such content must be demonstrated rather than assumed.

Together, these hypotheses predict that the apparent genomic extremity of *S. himalayana* emerges from the interaction of real evolutionary change, repeat expansion, genome reconstruction, and annotation methodology.

---

## Working biological model

Current analyses support a working model in which the large apparent Cai–Guo divergence reflects an interaction between:

1. **Real sequence-level biological variation**;
2. **Differential reconstruction of a highly repetitive genome**;
3. **Repeat-expanded gene architecture**, including very large introns;
4. **Annotation sensitivity to masking and genome representation**.

The project is designed to separate these effects rather than assume that assembly-size differences are directly biological.

---

## Current key observations

### Genome representation

Approximate assembly spans currently used in the project include:

- **Guo published:** ~2.061 Gb
- **Cai published:** ~1.276 Gb
- **Cai Flye–HyPo:** ~0.966 Gb
- **Cai fixed-on-Guo:** ~2.061 Gb

The difference in assembly span is therefore large even within a single species, making reconstruction strategy a central part of the biological interpretation.

### Cai read support for Guo

Independent Cai reads support most of the Guo assembly.

**Cai ONT → Guo**

- primary mapping rate: **92.68%**
- reference breadth covered: **88.11%**
- mean depth: approximately **14.4×**

**Cai Illumina → Guo**

- primary mapping rate: **97.87%**
- reference breadth covered: approximately **92.93%**
- mean depth: approximately **41.94×**

These results argue against interpreting the full assembly-size difference as straightforward biological genome-size divergence.

### High-confidence Cai-versus-Guo sequence differences

The strict small-variant set currently contains:

- **4,535,955** high-confidence small variants
- **3,704,632** SNPs
- **831,323** indels
- **1,158,638** homozygous-alternate calls

Cai ONT reads additionally produced **54,117 PASS structural-discrepancy calls** relative to the Guo coordinate system.

These are treated conservatively as accession- and reconstruction-associated differences rather than population-level variation.

### Published Cai minimum-length rescue

The published Cai assembly contained **128,027** FASTA records. Filtering scaffolds shorter than **1,250 bp** reduced this to **99,251** records while retaining **1,244,196,188 bp**, or **97.49%** of the original assembly span.

The same three Guo RNA-seq libraries showed only a small change in mean alignment rate:

- published Cai: approximately **95.24%**
- Cai min1250: approximately **95.15%**

This supports the 1,250-bp cutoff as a minimally destructive technical preprocessing step for workflows limited by extreme scaffold count.

### Repeat-expanded intron architecture

Using the current Guo BRAKER-derived working annotation and one representative transcript per gene:

- representative transcripts: **18,448**
- representative introns: **85,501**
- total intronic sequence: **264.2 Mb**
- median intron length: **145 bp**
- maximum intron length: **160,996 bp**

Only **10.53%** of representative introns exceed 10 kb, yet these introns account for approximately **73.51%** of total intronic sequence.

Repeat occupancy increases strongly with intron length, with a Spearman correlation of approximately **ρ = 0.740** between intron length and repeat fraction.

This supports the interpretation that extreme intron expansion in Guo is strongly associated with repeat accumulation.

### Annotation sensitivity

A controlled AUGUSTUS experiment using the same trained Guo gene model produced:

| Condition | Predicted genes |
|---|---:|
| Guo unmasked | **106,782** |
| Guo softmasked | **30,906** |

The same experiment produced:

- unmasked: **434,794 CDS features**
- softmasked: **153,165 CDS features**

This demonstrates strong sensitivity of AUGUSTUS gene prediction to repeat visibility in the Guo genome.

Helixer, using its land-plant model, produced **13,175 genes** and returned identical predictions on Guo softmasked and unmasked inputs, indicating that softmasking does not alter prediction in this implementation.

These annotation comparisons are being used as complementary tests of how robust gene inference is in an extremely repeat-rich parasitic-plant genome.

---

## Repository philosophy

This repository is an **analysis notebook, provenance record, and manuscript-development workspace**, not a polished software package.

It is intended to preserve:

- analysis decisions;
- software versions;
- Galaxy workflows and command histories;
- compact QC outputs;
- summary statistics;
- scripts;
- figures;
- failed major analytical branches;
- interpretation notes;
- manuscript-ready tables and figures.

Large primary or intermediate datasets such as FASTQ, BAM, full genome FASTA, and very large repeat catalogues should be deposited in archival storage such as **Zenodo** and linked from the corresponding repository folder.

---

## Phase map

| Phase | Scope | Status |
|---|---|---|
| **Phase 0** | Published Cai and Guo baseline comparison | Complete |
| **Phase 1** | Cai reassembly and polishing | Complete |
| **Phase 2** | Cai mapping to Guo, support analysis, variants, Cai-fixed pseudogenome | Complete |
| **Phase 3** | Harmonized comparison of genome representations | Active |
| **Phase 4** | Repeat discovery and repeat annotation | Active / completing |
| **Phase 5** | Structural gene annotation and annotation-method comparison | Active / major runs complete |
| **Phase 6** | Functional and comparative genomics | Planned / beginning |
| **Phase 7** | Manuscript figures, tables, methods, supplementary outputs | Planned |
| **Track 90** | Andrian exploratory internship analyses | Active / archival |

---

## Repository structure

```text
00_phase0_published_baseline/
01_phase1_cai_reassembly/
02_phase2_cai_mapping_to_guo/
03_phase3_harmonized_comparison/
04_phase4_repeat_annotation/
05_phase5_gene_annotation/
06_phase6_functional_comparative_genomics/
07_phase7_manuscript_outputs/
90_andrian_exploratory/
docs/
scripts/
```

The numbered phases represent the manuscript-grade analytical stream. Exploratory work remains separated under `90_andrian_exploratory/` until reproduced, quality-checked, and judged relevant to the main analysis.

---

## Main analytical contrasts

Several contrasts are intentionally built into the project.

### Biological sequence divergence

**Guo vs Cai fixed-on-Guo**

This comparison holds the Guo structural backbone largely constant while introducing confident Cai fixed alleles.

### Reconstruction effect

**Guo / Cai fixed-on-Guo vs Cai Flye–HyPo**

This contrast tests how much apparent difference emerges when Cai is represented by an independent long-read reconstruction.

### Historical published representation

**Published Cai vs Cai min1250 vs Cai Flye–HyPo**

This comparison helps distinguish properties of the original published assembly from properties that remain after minimal filtering or full reassembly.

### Repeat-treatment effect

Controlled gene-prediction comparisons on Guo test the effect of exposing or masking repetitive sequence while holding the prediction model constant.

---

## Interpretation limits

The Cai and Guo datasets represent **two accessions**, not population samples.

Accordingly:

- sequence differences should not be generalized as species-wide polymorphism;
- Thailand-versus-China regional adaptation cannot be inferred from these two accessions;
- structural discrepancies should not automatically be treated as biological structural variants;
- unsupported regions should not automatically be called accession-specific sequence;
- assembly-size differences must not be interpreted directly as genome-size differences without orthogonal evidence;
- annotation differences must be interpreted in the context of masking, reconstruction, evidence type, and predictor behavior.

The project therefore distinguishes as carefully as possible between **biological divergence**, **reconstruction-associated differences**, and **annotation-dependent differences**.

---

## Project team

- **Dr. Adhityo Wicaksono (Aether Biomics, Indonesia)** — Project lead, conceptualization, main analysis, interpretation, and manuscript development
- **Prof. Dr. rer. nat. Arli Aditya Parikesit (Indonesia International Institute for Life-Sciences, i3L)** — Co-supervisor
- **Andrian Dary Fawwaz (Indonesia International Institute for Life-Sciences, i3L)** — Student research intern
- **H.E.L.I.O.S. (OpenAI ChatGPT)** — AI-assisted workflow design, analysis support, interpretation, and documentation

---

## Primary source publications

The two published *Sapria himalayana* genome resources reanalyzed in RE-SAPRIA originate from:

1. Cai L, Arnold BJ, Xi Z, et al. (2021). Deeply altered genome architecture in the endoparasitic flowering plant *Sapria himalayana* Griff. (Rafflesiaceae). *Current Biology* 31(5):1002–1011.e9. https://doi.org/10.1016/j.cub.2020.12.045

2. Guo X, et al. (2023). The *Sapria himalayana* genome provides new insights into the lifestyle of endoparasitic plants. *BMC Biology* 21:134. https://doi.org/10.1186/s12915-023-01620-3

These source publications should be cited when using, discussing, or redistributing analyses derived from the corresponding published assemblies or sequencing datasets.

---

## Citation status

This repository is an active research record and should not yet be cited as a finalized genome resource.

A stable archival dataset and formal citation will be provided as the project reaches manuscript-ready status.

---

## License

This repository is licensed under the **MIT License**.

---

## Maintainer

**Adhityo Wicaksono**

---

## Disclaimer

RE-SAPRIA is designed to investigate why multiple representations of the same extreme parasitic-plant genome can differ so dramatically.

The central aim is not to declare one assembly or one annotation universally “correct,” but to determine which differences are robust to independent read evidence, genome reconstruction, repeat treatment, and annotation strategy.
