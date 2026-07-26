# Phase 2.0 — Guo PacBio Flye Draft

## Objective

Generate a reference-free Guo draft assembly from all twelve compatible PacBio Sequel II runs.

## Input rule

Use run accessions (`SRR...`) rather than experiment accessions (`SRX...`) in Galaxy download tools.

## Run manifest

Complete the twelve-row Guo section in the root `DATA_MANIFEST.tsv`.

## Proposed Flye logic

- same sample;
- same PacBio read class;
- all twelve files in one Flye run;
- no genome-size prior;
- no metagenome mode;
- one initial long-read polishing iteration.

## Evaluation

Apply the same post-Flye gate used for Cai:

1. QUAST;
2. BUSCO AUGUSTUS;
3. BUSCO Miniprot;
4. long-read read-back mapping;
5. Samtools Flagstat;
6. Samtools coverage;
7. Mosdepth;
8. accept, rerun, or reject.

## Data-retention checkpoint

Do not delete the PacBio reads until read-back mapping and coverage QC are saved and the Guo Flye draft is accepted.
