# Phase 1.1 — Cai Short-Read Polishing

## Objective

Correct residual ONT substitutions and indels using Cai Illumina reads, then determine the best polishing endpoint.

## Candidate polishers

- Pilon
- HyPo

A single tool may be selected after pilot evaluation. Do not merge outputs from different polishing branches without an explicit rationale.

## Baseline input

`Cai_Flye_v1_unpolished`

## Proposed workflow

```text
Cai Flye v1
    ↓
Map Cai Illumina reads
    ↓
Polishing round 1
    ↓
Remap Illumina reads from scratch
    ↓
QUAST + BUSCO AUGUSTUS + BUSCO Miniprot
    ↓
Polishing round 2 only if corrections and QC still improve
    ↓
Final comparison
```

## Required evaluation after every round

- assembly length
- contig number
- N50 and auN
- gap percentage
- Illumina mapping rate
- correction counts
- BUSCO AUGUSTUS
- BUSCO Miniprot
- number and percentage of internal-stop BUSCOs
- major unexpected sequence loss or gain

## Primary success criteria

1. AUGUSTUS completeness rises toward the Miniprot result.
2. Internal-stop BUSCO count declines.
3. Miniprot completeness does not materially decline.
4. Contiguity remains stable.
5. No major unsupported changes occur.

## Stopping rule

Stop when another polishing round produces negligible correction and no meaningful improvement in BUSCO or mapping QC.

## Outputs

Keep each polishing round in its own subfolder. Never overwrite earlier accepted assemblies or reports.
