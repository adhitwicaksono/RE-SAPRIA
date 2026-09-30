# Cai ONT mapping to Guo

This directory documents mapping of independent Cai Oxford Nanopore reads to the published Guo *Sapria himalayana* assembly.

## Purpose

The analysis asks how much of the larger Guo genome representation is independently supported by long-read data from the Cai accession. Because the two datasets represent different accessions and different genome reconstructions, mapping differences are interpreted conservatively and are not treated automatically as biological structural variation.

## Frozen summary

| Metric | Value |
|---|---:|
| Primary mapping rate | 92.68% |
| Reference breadth covered | 88.11% |
| Mean depth | ~14.4× |
| Guo sequence with Cai ONT support | ~1.816 Gb |
| Guo sequence without ONT coverage | ~245 Mb |
| Guo scaffolds with ≥90% breadth | 9,204 |
| Guo scaffolds with zero coverage | 1,402 |

## Interpretation

Most of the Guo assembly is recognized by independent Cai long reads despite the large difference between the published Cai and Guo assembly spans. The unsupported fraction should not automatically be classified as Guo-specific sequence because divergence, repeat structure, mapping ambiguity, and assembly/reconstruction differences can all reduce cross-accession read support.

## Suggested files

When available, retain compact reproducibility outputs such as:

- mapping summary/statistics;
- depth and breadth summaries;
- scaffold-level breadth table;
- workflow or Galaxy history notes;
- relevant BED intervals derived from the ONT mapping.

Large BAM files should remain in archival storage rather than ordinary Git history.
