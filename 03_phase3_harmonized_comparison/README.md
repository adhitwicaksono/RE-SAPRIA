# Phase 3 — Harmonized Cai–Guo Comparison

## Objective

Compare the final Cai and Guo reassemblies with identical alignment, filtering, QC, and plotting procedures.

## Required comparisons

1. published Cai vs published Guo;
2. final Cai vs published Cai;
3. final Guo vs published Guo;
4. final Cai vs final Guo;
5. self-controls for final Cai and final Guo.

## Tools

- Minimap2
- paftools
- MUMmer4 / NUCmer
- delta-filter
- show-coords
- DNAdiff
- Mummerplot
- custom plotting scripts

## Standard NUCmer baseline

```bash
nucmer --mum -l 100 -c 500 -t 1 \
  -p PREFIX \
  REFERENCE.fasta QUERY.fasta
```

Reference/query orientation should be chosen with memory limitations in mind and documented explicitly.

## Plot classes

- broad/raw plot;
- strict many-to-many plot;
- strict one-to-one plot;
- alignment-length distributions;
- identity-versus-length plots;
- breakpoint-category plots;
- unaligned-sequence length distributions.

## Interpretation rules

- MUMmer `--layout` does not create chromosome order.
- DNAdiff breakpoint classes are assembly-level discordance metrics.
- Reverse-oriented blocks are candidates for further investigation, not automatically validated inversions.
- Many-to-many cumulative alignment length may include overlapping matches.
