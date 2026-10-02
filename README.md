# RE-SAPRIA

## One species. Multiple genome representations. More than 1 Gb of disagreement.

**RE-SAPRIA** is a comparative-genomics project asking why independently generated genome representations of the endoparasitic plant *Sapria himalayana* differ so dramatically, and which biological conclusions remain stable when reconstruction, repeat treatment, and annotation strategy change.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23072450.svg)](https://doi.org/10.5281/zenodo.23072450)

> **Central question:** How much of the apparent Cai–Guo genomic difference is genuine biological divergence, and how much is reconstruction- and annotation-dependent behavior in an extraordinarily repeat-rich genome?

---

## Meet *Sapria*

*Sapria himalayana* is a member of **Rafflesiaceae**, the same family as *Rafflesia*, but it is a different genus. Most of the vegetative parasite remains embedded inside its host vine; the flower is the conspicuous part that emerges.

| Female *S. himalayana* | Male *S. himalayana* |
|:---:|:---:|
| <img src="src/s_himalayana_female_chiangmai.jpg" width="380" alt="Female Sapria himalayana flower from Chiang Mai, Thailand"> | <img src="src/s_himalayana_male_chiangmai.jpg" width="380" alt="Male Sapria himalayana flower from Chiang Mai, Thailand"> |
| Chiang Mai, Thailand | Chiang Mai, Thailand |

Two independent genome studies anchor this project:

- **Cai** = the 2021 *Current Biology* study by Liming Cai and colleagues.
- **Guo** = the 2023 *BMC Biology* study by Xuelian Guo, Xiaodi Hu, and colleagues.

In this repository, “Cai” and “Guo” are shorthand for **two independently studied accessions and their associated genome datasets/representations**, not species names.

---

## The paradox in 30 seconds

| Genome representation | Assembly span | Role |
|---|---:|---|
| **Guo published** | **2.061 Gb** | Published Guo structural reference |
| **Cai published** | **1.276 Gb** | Published Cai representation |
| **Cai Flye–HyPo** | **0.966 Gb** | Independent Cai long-read reconstruction |
| **Cai min1250** | **1.244 Gb** | Technical rescue of published Cai |
| **Cai fixed-on-Guo** | **2.061 Gb** | Guo backbone carrying confident fixed Cai alleles |

The largest and smallest representations differ by about **1.09 Gb**, yet:

- Cai ONT reads map to Guo at **92.68%** primary mapping with **88.11%** reference breadth.
- Cai Illumina reads map to Guo at **97.87%** primary mapping with **~92.93%** breadth.
- Complete BUSCO recovery changes only modestly across representations spanning ~0.97–2.06 Gb.

So assembly span alone does not explain recognizable conserved gene space.

---

# What RE-SAPRIA currently shows

## 1. The assembly disagreement is concentrated in repeat-rich sequence

RepeatMasker identifies approximately **84.32–90.35% of non-N sequence** as repetitive across the analyzed genome representations.

For the major Guo-versus-Cai comparisons, approximately **94–95% of the non-N assembly-span difference lies in repeat-masked sequence** under the corresponding genome-specific repeat workflows.

Among the three Cai structural representations, the non-repeat non-N component is comparatively stable at roughly **150–156 Mb**, even though represented genome span varies substantially.

**Interpretation:** the assembly-size paradox is primarily a **repeat-space problem**, although repeat recovery still mixes true biology with reconstruction effects.

---

## 2. Long introns are a robust feature, not a single-annotation artifact

Using one representative transcript per gene, selected by **longest total CDS length**:

| Representation | Representative introns | Introns ≥10 kb | Intronic bp inside ≥10-kb introns |
|---|---:|---:|---:|
| **Guo** | 107,624 | **9.13%** | **66.80%** |
| **Cai fixed-on-Guo** | 116,488 | **10.02%** | **70.57%** |
| **Cai min1250** | 81,668 | **11.18%** | **71.74%** |
| **Cai Flye–HyPo** | 77,610 | **11.44%** | **72.08%** |

Only ~9–11% of representative introns are at least 10 kb long, yet they contain ~67–72% of total representative intronic sequence.

---

## 3. Those long introns are strongly repeat-associated

Across the four standardized BRAKER3 annotations:

- **73.45–76.30%** of representative intronic sequence overlaps RepeatMasker intervals.
- only **11.45–17.41%** of representative CDS sequence overlaps repeats.
- intron length and repeat fraction are strongly positively associated (**Spearman ρ = 0.658–0.748**).

The trend is consistent across genome representations: longer introns contain progressively larger repeat fractions.

**Working interpretation:** repetitive sequence penetrates gene space primarily by expanding introns rather than coding sequence.

---

## 4. Repeat visibility can massively inflate ab initio gene prediction

A controlled Guo AUGUSTUS experiment holds the genome coordinates and trained model constant while changing repeat visibility:

| Guo AUGUSTUS input | Predicted genes | CDS features |
|---|---:|---:|
| **Softmasked** | **30,906** | **153,165** |
| **Unmasked** | **106,782** | **434,794** |

The unmasked genome produces **3.46×** as many predicted genes.

Among **60,530** unmasked models without a same-strand softmasked AUGUSTUS counterpart:

- median gene-span repeat fraction = **100%**
- median CDS repeat fraction = **100%**
- only **6.21%** overlap an RNA-supported BRAKER gene on the same strand

Thus, exposing repetitive sequence creates a large **repeat-associated, weakly RNA-supported prediction space**.

This does **not** mean every extra model is a false gene; some may represent TE proteins or genuine repeat-associated loci.

---

## 5. Annotation scale does not simply follow assembly span

The standardized softmasked BRAKER3 panel contains:

| Representation | Genes | Transcripts | Gene density |
|---|---:|---:|---:|
| **Guo** | **29,792** | **34,471** | **14.46/Mb** |
| **Cai fixed-on-Guo** | **29,887** | **34,783** | **14.50/Mb** |
| **Cai min1250** | **20,149** | **24,733** | **16.19/Mb** |
| **Cai Flye–HyPo** | **19,430** | **23,822** | **20.10/Mb** |

Cai min1250 and Cai Flye–HyPo differ by **22.3% in assembly span** but only ~**3.6–3.7%** in gene/transcript count.

Cai Flye–HyPo also produces a higher start+stop structural-completeness proxy than Cai min1250 (**97.30% vs 88.00%** of transcripts).

---

# Working model

The current evidence supports a linked model:

**repeat-rich genome architecture → reconstruction sensitivity → repeat-expanded introns → annotation sensitivity**

Biological Cai–Guo sequence divergence is real, but the observed genome difference cannot be interpreted as biological divergence alone.

---

# Genome representations and what they test

| Representation | Purpose |
|---|---|
| **Guo published** | Structural reference |
| **Cai published** | Historical published Cai representation |
| **Cai min1250** | Tests whether minimal scaffold filtering preserves biological signal |
| **Cai Flye–HyPo** | Tests reconstruction effects using an independent Cai assembly |
| **Cai fixed-on-Guo** | Tests fixed sequence divergence while largely holding Guo structure constant |

**Cai fixed-on-Guo is an analytical pseudogenome, not an independent Cai assembly.**

A Guo Flye reconstruction was attempted but did not yield a usable completed assembly; that failure is retained as technical provenance and is not interpreted biologically.

---

# Repository map

| Question | Directory |
|---|---|
| What did the published Cai and Guo assemblies originally look like? | [`00_phase0_published_baseline/`](00_phase0_published_baseline/) |
| How was the independent Cai reconstruction made? | [`01_phase1_cai_reassembly/`](01_phase1_cai_reassembly/) |
| Do Cai reads support Guo, and how was Cai-fixed constructed? | [`02_phase2_cai_mapping_to_guo/`](02_phase2_cai_mapping_to_guo/) |
| How do the genome representations compare under harmonized QC? | [`03_phase3_harmonized_comparison/`](03_phase3_harmonized_comparison/) |
| Where are the repeats, and how much sequence do they explain? | [`04_phase4_repeat_annotation/`](04_phase4_repeat_annotation/) |
| How do repeats affect gene architecture and prediction? | [`05_phase5_gene_annotation/`](05_phase5_gene_annotation/) |
| Which robust genes and functions survive across representations? | [`06_phase6_functional_comparative_genomics/`](06_phase6_functional_comparative_genomics/) |
| Manuscript-ready outputs | [`07_phase7_manuscript_outputs/`](07_phase7_manuscript_outputs/) |
| Andrian's exploratory internship analyses | [`90_andrian_exploratory/`](90_andrian_exploratory/) |
| Student/public introductions | [`99_education/`](99_education/) |

---

# Project status

| Phase | Scope | Status |
|---|---|---|
| **0** | Published Cai–Guo baseline | **Complete** |
| **1** | Cai independent reassembly | **Complete** |
| **2** | Cai mapping to Guo, variants, Cai-fixed | **Complete** |
| **3** | Harmonized genome comparison | **Complete** |
| **4** | Repeat discovery and annotation | **Complete** |
| **5** | Structural annotation + repeat-aware interpretation | **Phase 5A + core 5B complete** |
| **6** | Functional and comparative genomics | **Beginning** |
| **7** | Manuscript outputs | **Planned** |
| **90** | Internship exploratory track | **Active / archival** |

---

# Phase 6 direction

For each standardized BRAKER3 annotation:

1. extract CDS and peptides with `gffread` using the **matching softmasked genome**;
2. select one representative transcript per gene by **longest total CDS length**;
3. perform protein QC;
4. use representative proteins for:
   - DIAMOND `blastp` against **Swiss-Prot** as the first curated homology layer;
   - broader **NR rescue** for weak/no Swiss-Prot hits;
   - InterProScan / Pfam;
   - eggNOG-mapper;
   - OrthoFinder;
   - BUSCO protein mode;
5. retain CDS sequences for nucleotide homology, codon analyses, Ka/Ks where appropriate, and model validation.

Functional labels will be integrated across evidence sources rather than copied from a single top hit.

---

# Interpretation guardrails

RE-SAPRIA deliberately separates observation from inference.

- **Two accessions are not a population sample.**
- Assembly span is not automatically biological genome size.
- Cai–Guo structural discrepancies are not automatically biological structural variants.
- Lack of Cai read support is not automatically Guo-specific DNA.
- Repeat-class percentages are **method-sensitive** because RepeatModeler libraries were learned independently for each representation.
- Additional unmasked gene predictions are not automatically genuine genes, but neither are they automatically false.
- Repeat-rich giant introns are structurally robust, but repeat content alone does not establish function.
- Strong biological claims should survive multiple evidence types and alternative genome representations.

---

# Data availability

The standardized **Phase 5A BRAKER3 and AUGUSTUS GFF3 annotations** are archived on Zenodo:

**DOI: [10.5281/zenodo.23072450](https://doi.org/10.5281/zenodo.23072450)**

Large primary and intermediate files are intentionally kept outside ordinary Git history. GitHub stores compact summaries, scripts, figures, decision records, and interpretation.

---

# Project team

- **Dr. Adhityo Wicaksono** — project lead; conceptualization, analysis, interpretation, manuscript development
- **Prof. Dr. rer. nat. Arli Aditya Parikesit** — co-supervisor
- **Andrian Dary Fawwaz** — student research intern
- **H.E.L.I.O.S. / OpenAI ChatGPT** — AI-assisted workflow design, analysis support, interpretation, and documentation

---

# Key references

1. Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply altered genome architecture in the endoparasitic flowering plant Sapria himalayana*. **Current Biology** 31:1002–1011.e9. https://doi.org/10.1016/j.cub.2020.12.045
2. Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants*. **BMC Biology** 21:134. https://doi.org/10.1186/s12915-023-01620-3
3. Flynn JM, Hubley R, Goubert C, et al. (2020). RepeatModeler2. **PNAS** 117:9451–9457. https://doi.org/10.1073/pnas.1921046117
4. Gabriel L, Brůna T, Hoff KJ, et al. (2024). BRAKER3. **Genome Research**. https://doi.org/10.1101/gr.278090.123
5. Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM. (2021). BUSCO Update. **Molecular Biology and Evolution** 38:4647–4654. https://doi.org/10.1093/molbev/msab199
6. Li H. (2023). Protein-to-genome alignment with miniprot. **Bioinformatics** 39:btad014. https://doi.org/10.1093/bioinformatics/btad014

---

# License

MIT License.

---

## One species. Multiple plausible genome representations. The biology is hidden in the disagreement.
