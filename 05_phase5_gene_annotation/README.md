# Phase 5 — Structural Gene Annotation

## Objective

Generate and compare multiple structural annotations while selecting one defensible primary annotation set.

## Main annotation tracks

1. BRAKER3 — primary evidence-guided annotation;
2. Helixer — independent sequence-only annotation;
3. standalone AUGUSTUS — educational and methodological control;
4. published Cai and Guo annotations — historical reference.

## Fair-comparison rules

- same final assembly version;
- same soft-masking procedure;
- same protein database;
- identical evidence rules where applicable;
- one primary transcript per locus for predictor comparison;
- same evaluation tools and database versions.

## Evaluation dimensions

- gene and transcript counts;
- exon, intron, CDS, and protein-length distributions;
- BUSCO and OMArk;
- RNA-seq junction support;
- protein homology and domain support;
- repeat overlap;
- split and fused gene models;
- Cai–Guo orthology and structural consistency;
- manual review of representative disagreements.

## Expected strategy

BRAKER3 supplies the primary evidence-guided set. Helixer audits the annotation and identifies sequence-supported candidates. Models are not chosen merely by gene count or BUSCO score.
