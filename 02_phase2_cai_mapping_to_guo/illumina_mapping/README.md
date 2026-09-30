# Cai Illumina mapping to Guo

This directory documents mapping of independent Cai Illumina reads to the published Guo *Sapria himalayana* assembly.

## Purpose

Short-read mapping provides an independent test of how much of the Guo assembly is recognized by Cai sequence data and supplies the read evidence used for stringent small-variant calling.

## Frozen summary

| Metric | Value |
|---|---:|
| Primary mapping rate | 97.87% |
| Reference breadth covered | ~92.93% |
| Mean depth | ~41.94× |
| Sequence in scaffolds with ≥90% breadth | ~1.70 Gb |
| Sequence in completely unsupported scaffolds | ~0.56 Mb |

## Interpretation

The very high mapping rate and broad reference coverage indicate that a large fraction of the Guo assembly is supported by Cai short reads. This does not establish biological identity between accessions, but it argues against interpreting the published assembly-size difference directly as accession-level genome-size divergence.

## Suggested files

Retain compact outputs such as:

- mapping summary/statistics;
- depth and breadth summaries;
- scaffold-level breadth table;
- callable-region BED files;
- Galaxy workflow/history notes.

Large BAM files should be archived outside ordinary Git history.
