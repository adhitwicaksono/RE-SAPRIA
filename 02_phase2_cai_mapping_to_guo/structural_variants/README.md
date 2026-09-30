# Cai ONT structural discrepancies relative to Guo

This directory documents structural-discrepancy calls obtained from Cai Oxford Nanopore reads mapped to the Guo assembly.

## Frozen summary

- **54,117 PASS events** were retained from Sniffles2.

These events are treated as **structural discrepancies** between Cai long-read evidence and the Guo genome representation rather than automatically as biological structural variants.

## Why the conservative terminology?

A Cai-versus-Guo structural call can arise from several sources:

- genuine accession-level structural difference;
- local assembly/reconstruction difference;
- repeat-associated mapping ambiguity;
- collapsed or expanded repetitive sequence;
- unresolved or differently represented haplotypes;
- alignment limitations.

Accordingly, downstream analyses should use read support, genomic context, repeat overlap, and assembly comparison before assigning biological interpretation.

## Downstream use

Span-bearing events such as deletions, duplications, and inversions can be intersected with:

- genes;
- CDS;
- introns;
- repeats;
- callable/supported regions.

This branch contributes to the broader RE-SAPRIA goal of separating biological divergence from reconstruction-associated differences.
