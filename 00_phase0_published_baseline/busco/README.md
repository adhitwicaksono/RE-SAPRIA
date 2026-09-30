# Phase 0 BUSCO — Published Cai and Guo baseline

This directory contains the original harmonized BUSCO 5.8.0 short summaries for the **published Cai** and **published Guo** *Sapria himalayana* assemblies.

These files are retained as the Phase 0 conserved-gene-space baseline against which later genome representations are compared.

## BUSCO setup

All four runs used:

- **BUSCO:** 5.8.0
- **Lineage:** `embryophyta_odb10`
- **BUSCO groups searched:** **1,614**
- **Lineage dataset creation date:** 2024-01-08
- **AUGUSTUS mode:** `euk_genome_aug`
- **AUGUSTUS:** 3.5.0
- **Miniprot mode:** `euk_genome_min`
- **Miniprot:** 0.14-r265

## BUSCO summary

| Assembly | Predictor | Complete | Single-copy | Duplicated | Fragmented | Missing | Complete BUSCOs with internal stops |
|---|---|---:|---:|---:|---:|---:|---:|
| **Cai published** | AUGUSTUS | **47.5%** | 46.7% | 0.9% | 3.3% | 49.1% | not reported |
| **Cai published** | Miniprot | **49.3%** | 48.1% | 1.1% | 5.4% | 45.4% | 47 |
| **Guo published** | AUGUSTUS | **49.7%** | 48.0% | 1.7% | 2.5% | 47.8% | not reported |
| **Guo published** | Miniprot | **51.2%** | 48.7% | 2.5% | 4.5% | 44.2% | 43 |

The two published assemblies therefore recover broadly similar conserved embryophyte gene space despite their very different assembled spans.

## Why do the BUSCO assembly statistics show more contigs than FASTA records?

This is expected and is not a BUSCO error.

The input FASTA files contain **scaffold records**. BUSCO's assembly-statistics step also estimates the number and N50 of **contiguous sequence blocks separated by gaps**.

Runs of `N` bases therefore split a scaffold into multiple underlying contigs.

### Published Cai

| Metric | Value |
|---|---:|
| FASTA scaffold records | **128,027** |
| BUSCO-reported contigs | **216,625** |
| Total span | **1,276,270,856 bp** |
| Gap content | **7.319%** |
| Scaffold N50 | **952 kb** |
| Contig N50 | **19 kb** |

### Published Guo

| Metric | Value |
|---|---:|
| FASTA scaffold records | **18,718** |
| BUSCO-reported contigs | **26,955** |
| Total span | **2,060,974,854 bp** |
| Gap content | **1.865%** |
| Scaffold N50 | **251 kb** |
| Contig N50 | **106 kb** |

This distinction is biologically and methodologically important for RE-SAPRIA.

The published Cai assembly has a much larger **scaffold N50** than Guo, but a much smaller **contig N50** and substantially more gap sequence. Its apparently high scaffold continuity is therefore partly produced by scaffold joins across gaps.

By contrast, Guo has a lower scaffold N50 but substantially greater gap-free contig continuity.

Later, the independent Cai Flye–HyPo reconstruction provides a useful third comparison because it contains **10,435 contigs, no Ns, and an N50 of approximately 1.056 Mb**. Its megabase-scale N50 therefore reflects gap-free contig sequence rather than scaffold joins.

## Interpretation

Two separate questions should not be conflated:

1. **How much conserved plant gene space is recoverable?**  
   BUSCO answers this approximately. Cai and Guo are broadly similar at ~47–51% complete BUSCOs depending on predictor.

2. **How continuous is the underlying assembled sequence?**  
   Scaffold N50 alone does not answer this. The scaffold-versus-contig contrast shows that the two published assemblies have very different reconstruction structures.

This is one of the earliest clues motivating the central RE-SAPRIA question: large differences between *Sapria* genome representations may arise from a mixture of genuine biology and reconstruction strategy.

## Files

- `Cai_published_BUSCO5.8_embryophyta_odb10_AUGUSTUS.txt`
- `Cai_published_BUSCO5.8_embryophyta_odb10_Miniprot.txt`
- `Guo_published_BUSCO5.8_embryophyta_odb10_AUGUSTUS.txt`
- `Guo_published_BUSCO5.8_embryophyta_odb10_Miniprot.txt`

## Caution

BUSCO completeness should not be interpreted as total biological genome completeness.

Missing BUSCOs can reflect genuine gene loss, sequence divergence, fragmentation, unusual gene architecture, or predictor/alignment limitations. In *Sapria*, this is particularly relevant because extreme parasitism, repeat-rich sequence, and very large introns may all complicate conserved-gene recovery.
