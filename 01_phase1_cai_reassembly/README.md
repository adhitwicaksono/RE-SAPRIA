# Phase 1 — Cai Reassembly

## Objective

Reassemble the Cai *Sapria himalayana* dataset from its Oxford Nanopore reads, polish the draft with Illumina reads, and select a final Cai assembly using predefined QC criteria.

## Phase structure

- `phase1_0_flye_ont/` — unpolished ONT Flye draft and QC
- `phase1_1_short_read_polishing/` — Pilon and/or HyPo polishing trials
- `phase1_2_final_selection/` — final assembly selection and comparison with published Cai and Guo

## Governing principle

The initial Flye assembly does not use the published genome span as an estimated genome size.
