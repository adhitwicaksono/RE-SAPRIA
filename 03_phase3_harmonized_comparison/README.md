# Phase 3 — Harmonized Cai–Guo Comparison

## Objective

Phase 3 compares the principal *Sapria himalayana* genome representations under harmonized QC and evidence layers in order to separate:

1. **sequence-level biological divergence**;
2. **genome reconstruction effects**; and
3. **downstream annotation consequences**.

The phase no longer assumes that independent final reassemblies exist for both Cai and Guo. The independent Cai Flye–HyPo reconstruction succeeded, whereas the attempted Guo Flye reconstruction did not yield a usable completed assembly. The **published Guo assembly therefore remains the Guo structural reference**.

## Genome representations

| Representation | Role |
|---|---|
| **Guo published** | Guo structural reference |
| **Cai published** | Historical Cai representation |
| **Cai min1250** | Minimally filtered published Cai representation for annotation-compatible workflows |
| **Cai Flye–HyPo** | Independent Cai long-read reconstruction |
| **Cai fixed-on-Guo** | Guo-backbone pseudogenome carrying confident Cai homozygous-alternate alleles |

The Cai fixed-on-Guo genome is an analytical pseudogenome, not an independent Cai assembly.

---

## Core analytical contrasts

### Sequence divergence with structure held largely constant

**Guo vs Cai fixed-on-Guo**

This contrast asks how much changes when confident Cai fixed alleles are introduced while retaining the Guo scaffold framework.

### Reconstruction effect

**Guo / Cai fixed-on-Guo vs Cai Flye–HyPo**

This contrast asks how much apparent difference emerges when Cai is represented by an independent long-read reconstruction.

### Published-assembly effect

**Cai published vs Cai min1250 vs Cai Flye–HyPo**

This contrast distinguishes the historical published representation from a minimally filtered derivative and an independent reconstruction.

---

## Current checkpoints

### 1. Assembly span

Current SeqKit measurements:

| Representation | Assembly span |
|---|---:|
| Guo published | **2,060,974,854 bp** |
| Cai fixed-on-Guo | **2,060,941,893 bp** |
| Cai published | **1,276,270,856 bp** |
| Cai min1250 | **1,244,196,188 bp** |
| Cai Flye–HyPo | **966,497,149 bp** |

These values describe the analyzed FASTA representations and should not automatically be interpreted as biological genome-size estimates.

### 2. BUSCO conserved gene-space comparison

All harmonized BUSCO runs used **BUSCO 5.8.0**, `embryophyta_odb10`, and **1,614 BUSCO groups**, evaluated separately with AUGUSTUS and Miniprot.

| Representation | AUGUSTUS C / F / M | Miniprot C / F / M | Miniprot complete BUSCOs |
|---|---:|---:|---:|
| **Guo** | **49.7 / 2.5 / 47.8%** | **51.2 / 4.5 / 44.2%** | **827** |
| **Cai fixed-on-Guo** | **49.8 / 2.6 / 47.6%** | **51.4 / 4.3 / 44.3%** | **830** |
| **Cai published** | **47.5 / 3.3 / 49.1%** | **49.3 / 5.4 / 45.4%** | **795** |
| **Cai min1200** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai min1250** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai min1300** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai Flye–HyPo** | **47.3 / 3.8 / 48.9%** | **50.5 / 4.9 / 44.6%** | **815** |

![BUSCO completeness by AUGUSTUS](assembly_qc/busco/busco_augustus_stacked_bar.png)

![BUSCO completeness by Miniprot](assembly_qc/busco/busco_miniprot_stacked_bar.png)

The BUSCO comparison provides three useful controls:

- **Guo and Cai fixed-on-Guo are nearly indistinguishable**, supporting Cai-fixed as a sequence-divergence control.
- **Cai min1200/min1250/min1300 are essentially identical to published Cai**, supporting the 1,250-bp cutoff as a minimally destructive technical rescue.
- **Cai Flye–HyPo retains comparable conserved gene space despite its smaller span**; Miniprot recovers 815 complete BUSCOs from Flye–HyPo versus 795 from published Cai.

BUSCO completeness is not treated as a direct measurement of total biological genome completeness. In *Sapria*, genuine gene loss, extreme divergence, fragmentation, giant introns, and predictor behavior may all contribute to missing BUSCOs.

Detailed BUSCO outputs, plots, raw summaries, and interpretation are stored in:

[`assembly_qc/busco/`](assembly_qc/busco/)

### 3. Whole-genome alignment

Published Cai versus Guo:

- Cai aligned: **77.69%**
- Guo aligned: **66.28%**
- strict one-to-one aligned sequence: approximately **954.25 Mb**
- strict one-to-one identity: approximately **99.15%**
- many-to-many aligned sequence: approximately **1.503 Gb**

Cai Flye–HyPo versus Guo:

- Cai aligned: **89.48%**
- Guo aligned: **74.77%**
- strict one-to-one aligned sequence: approximately **880.5 Mb**
- strict one-to-one identity: approximately **98.72%**
- many-to-many aligned sequence: approximately **1.67 Gb**

These are representation-level comparisons. Alignment discordance is not automatically interpreted as biological structural variation.

### 4. RNA-seq mappability

The same three Guo paired-end RNA-seq libraries were mapped independently to each representation.

Mean HISAT2 overall alignment rates:

| Representation | Mean overall alignment |
|---|---:|
| Guo | **96.92%** |
| Cai fixed-on-Guo | **96.79%** |
| Cai Flye–HyPo | **95.88%** |
| Cai published | **95.24%** |
| Cai min1250 | **95.15%** |

The near-equivalence of Guo and Cai fixed-on-Guo, compared with the larger shift toward independently reconstructed Cai genomes, supports the use of Cai-fixed to distinguish sequence divergence from reconstruction-associated effects.

---

## Directory logic

Recommended Phase 3 organization:

```text
03_phase3_harmonized_comparison/
├── README.md
├── assembly_qc/
│   ├── seqkit/
│   └── busco/
├── coverage_comparison/
├── figures/
├── minimap2/
├── mummer_dnadiff/
├── tables/
└── unaligned_sequences/
```

Large FASTA, BAM, and other primary/intermediate datasets should remain outside normal Git history and be linked through archival deposition where appropriate.

---

## Interpretation rules

- Two accessions do not constitute a population sample.
- Assembly span is not automatically biological genome size.
- High sequence identity in aligned regions does not imply that unaligned sequence is artifactual.
- Unaligned sequence is not automatically accession-specific biology.
- MUMmer many-to-many cumulative length can contain overlapping alignments.
- Reverse-oriented alignment blocks are candidates for further investigation, not automatically validated inversions.
- BUSCO evaluates recovery of conserved orthologs; it does not measure repetitive, noncoding, lineage-specific, or total genome completeness.
- Differences are carried forward only when they help establish **concordance**, explain **discordance**, or demonstrate a **biological/annotation consequence**.

---

## References

Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM. (2021). BUSCO Update: Novel and Streamlined Workflows along with Broader and Deeper Phylogenetic Coverage for Scoring of Eukaryotic, Prokaryotic, and Viral Genomes. *Molecular Biology and Evolution* 38:4647–4654.  
https://doi.org/10.1093/molbev/msab199

Li H. (2023). Protein-to-genome alignment with miniprot. *Bioinformatics* 39:btad014.  
https://doi.org/10.1093/bioinformatics/btad014
