# Phase 2 — Guo Reassembly

## Objective

Reassemble the Guo *Sapria himalayana* dataset from twelve PacBio Sequel II long-read runs, polish it with appropriate Illumina reads, and select a final Guo assembly through the same logic used for Cai.

## Phase structure

- `phase2_0_flye_pacbio/`
- `phase2_1_short_read_polishing/`
- `phase2_2_final_selection/`

## Important constraint

All twelve compatible PacBio runs from the same Guo sample are supplied to one Flye assembly job. They are not assembled independently and merged afterward.

## Baseline design

- genome-size estimate: blank;
- reduced assembly coverage: off;
- metagenome mode: off;
- one long-read polishing iteration;
- same Flye version used for Cai whenever practical.

## Resource risk

The archived PacBio data total roughly 353.4 Gb of sequence and approximately 83.2 GB of listed SRA downloads. Galaxy storage and temporary-space requirements must be monitored carefully.
