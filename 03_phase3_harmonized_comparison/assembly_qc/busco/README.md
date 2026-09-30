# BUSCO comparison across RE-SAPRIA genome representations

This directory contains the harmonized BUSCO comparison used to evaluate conserved embryophyte gene-space recovery across the main *Sapria himalayana* genome representations.

## Setup

All runs used:

- **BUSCO:** 5.8.0
- **Lineage:** `embryophyta_odb10`
- **BUSCO groups searched:** **1,614**
- **Lineage dataset creation date reported by BUSCO:** 2024-01-08
- **Genome mode with AUGUSTUS:** `euk_genome_aug`
- **AUGUSTUS:** 3.5.0
- **Genome mode with Miniprot:** `euk_genome_min`
- **Miniprot:** 0.14-r265

The original BUSCO short-summary files are retained under `raw_summaries/`.

## Summary

| Representation | AUGUSTUS C / F / M | Miniprot C / F / M | Miniprot complete BUSCOs |
|---|---:|---:|---:|
| **Guo** | **49.7 / 2.5 / 47.8%** | **51.2 / 4.5 / 44.2%** | **827** |
| **Cai fixed-on-Guo** | **49.8 / 2.6 / 47.6%** | **51.4 / 4.3 / 44.3%** | **830** |
| **Cai published** | **47.5 / 3.3 / 49.1%** | **49.3 / 5.4 / 45.4%** | **795** |
| **Cai min1200** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai min1250** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai min1300** | **47.5 / 3.3 / 49.1%** | **49.2 / 5.4 / 45.4%** | **794** |
| **Cai Flye–HyPo** | **47.3 / 3.8 / 48.9%** | **50.5 / 4.9 / 44.6%** | **815** |

`C`, `F`, and `M` denote complete, fragmented, and missing BUSCOs, respectively. Small departures from 100% reflect percentage rounding in the BUSCO summaries.

## Visualizations

### AUGUSTUS

![BUSCO completeness by AUGUSTUS](busco_augustus_stacked_bar.png)

**Figure caption.** BUSCO completeness across seven *S. himalayana* genome representations using BUSCO 5.8.0 in genome mode with AUGUSTUS and `embryophyta_odb10` (n = 1,614). Complete, fragmented, and missing BUSCO fractions remain broadly similar despite large differences in assembled genome span. Guo and Cai fixed-on-Guo are nearly indistinguishable, while filtering published Cai at 1,200–1,300 bp produces no change in the AUGUSTUS BUSCO profile.

### Miniprot

![BUSCO completeness by Miniprot](busco_miniprot_stacked_bar.png)

**Figure caption.** BUSCO completeness across the same seven genome representations using BUSCO 5.8.0 with Miniprot and `embryophyta_odb10` (n = 1,614). Guo and Cai fixed-on-Guo again show nearly identical conserved-gene recovery. Cai Flye–HyPo recovers 815 complete BUSCOs compared with 795 in published Cai despite its substantially smaller assembled span.

## Main interpretation

Three controls emerge from this comparison.

**1. The Cai 1,250-bp technical filter is conservative.**  
Published Cai and all three minimum-length derivatives have identical AUGUSTUS BUSCO profiles. Miniprot recovers 795 complete BUSCOs from published Cai and 794 from each filtered representation. The 1,250-bp filter therefore reduces the FASTA below 100,000 records while preserving essentially all BUSCO-detectable conserved gene space.

**2. Cai fixed-on-Guo behaves as intended as a sequence-divergence control.**  
Guo and Cai fixed-on-Guo differ by only one complete AUGUSTUS BUSCO (802 versus 803) and three complete Miniprot BUSCOs (827 versus 830). Introducing confident Cai homozygous-alternate alleles onto the Guo backbone therefore has little effect on global conserved-gene recovery.

**3. Reduced assembly span does not imply proportional loss of conserved gene space.**  
Cai Flye–HyPo is approximately 0.966 Gb, substantially smaller than published Cai (~1.276 Gb), yet Miniprot recovers **815 complete BUSCOs** versus **795** in published Cai. AUGUSTUS is essentially stable (764 versus 767 complete BUSCOs). The smaller independent reconstruction therefore does not show a proportional loss of BUSCO-detectable gene space.

## Important caution

BUSCO is a conserved-gene recovery benchmark, not a direct measurement of biological genome completeness.

The approximately 47–51% complete BUSCO range observed here can reflect a mixture of genuine gene loss, sequence divergence, gene fragmentation, unusual gene architecture, and predictor/alignment limitations. In *Sapria*, this is especially important because extreme parasitism, repeat-rich sequence, and giant introns may all complicate standard gene-recovery assumptions.

For RE-SAPRIA, BUSCO is therefore used as one orthogonal QC layer alongside read support, whole-genome alignment, RNA-seq mappability, repeat architecture, and standardized gene annotation.

## Files

- `busco_summary_table.tsv` — compact C/F/M comparison used for plotting.
- `busco_summary_full.tsv` — expanded BUSCO percentages and raw counts.
- `busco_augustus_stacked_bar.png` — AUGUSTUS stacked horizontal bar plot.
- `busco_miniprot_stacked_bar.png` — Miniprot stacked horizontal bar plot.
- `raw_summaries/augustus/` — original AUGUSTUS BUSCO short summaries.
- `raw_summaries/miniprot/` — original Miniprot BUSCO short summaries.

## References

Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM. (2021). BUSCO Update: Novel and Streamlined Workflows along with Broader and Deeper Phylogenetic Coverage for Scoring of Eukaryotic, Prokaryotic, and Viral Genomes. *Molecular Biology and Evolution* 38:4647–4654.  
https://doi.org/10.1093/molbev/msab199

Li H. (2023). Protein-to-genome alignment with miniprot. *Bioinformatics* 39:btad014.  
https://doi.org/10.1093/bioinformatics/btad014
