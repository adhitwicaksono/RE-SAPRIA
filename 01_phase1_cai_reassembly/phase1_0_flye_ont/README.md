# Phase 1.0 — Cai ONT Flye Draft

## Objective

Generate and evaluate a reference-free Cai draft assembly from Oxford Nanopore reads.

## Flye invocation

- Flye version: 2.9.6
- Read mode: raw Oxford Nanopore
- Genome-size estimate: blank
- Metagenome mode: off
- Polishing iterations: 1
- Galaxy threads: `${GALAXY_SLOTS:-4}`

```bash
flye --nano-raw input_0.fastq.gz -o out_dir -t ${GALAXY_SLOTS:-4} -i 1
```

## QUAST results

| Metric | Result |
|---|---:|
| Total length | 963,878,780 bp |
| Contigs, all lengths | 10,435 |
| Contigs ≥500 bp | 10,389 |
| Largest contig | 8,082,338 bp |
| N50 | 1,036,241 bp |
| L50 | 199 |
| N90 | 43,404 bp |
| L90 | 2,692 |
| auN | 1,715,255 bp |
| GC | 28.4% |
| Gaps | 0% |

## BUSCO results

Lineage: `embryophyta_odb10`; total BUSCO groups: 1,614.

### AUGUSTUS

- Complete: 31.0%
- Single-copy: 30.9%
- Duplicated: 0.1%
- Fragmented: 6.5%
- Missing: 62.5%

### Miniprot

- Complete: 49.8%
- Single-copy: 48.9%
- Duplicated: 0.8%
- Fragmented: 4.2%
- Missing: 46.0%
- Complete BUSCOs with internal stop codons: 109

## ONT read-back mapping

### Samtools Flagstat

- Total alignment records: 6,241,606
- Primary reads: 2,532,164
- Primary reads mapped: 2,339,609
- Primary mapping rate: 92.40%
- Overall mapped alignment records: 96.91%
- Secondary alignments: 2,899,055
- Supplementary alignments: 810,387

### Coverage

- Assembly breadth covered by at least one ONT alignment: 99.895%
- Uncovered bases: approximately 1.015 Mb
- Zero-depth contigs: 47
- Zero-depth contig span: 54,015 bp
- Genome-wide mean depth: 31.13×
- Main long-contig backbone: approximately 13–15×
- Most assembled bases lie on contigs with mean depth of 10–20×

## Interpretation

The draft has strong long-read support and markedly improved true contiguity relative to published Cai. Miniprot BUSCO completeness is similar to published Cai and Guo, indicating that much of the conserved gene space is present. The large AUGUSTUS–Miniprot gap and 109 internal-stop BUSCOs indicate residual ONT base errors, especially frameshifting indels.

## Decision

Accepted for short-read polishing.

The draft is not yet suitable as the final annotation substrate.

## Data-retention decision

The original 24-GB ONT FASTQ was cleared for Galaxy deletion after mapping, coverage, and QC reports were saved.
