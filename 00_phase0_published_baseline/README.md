# Phase 0 — Published Cai and Guo Baseline

## Objective

Establish a historical baseline using the published Cai and Guo assemblies and the methods described in their original studies.

## Inputs

- Published Cai assembly, Thailand accession
- Published Guo assembly, China accession
- Published structural annotations where available
- Original papers and supplementary methods

## Main activities

1. Compare reported sequencing and assembly workflows.
2. Run reference-free QUAST.
3. Run BUSCO using the same predictor and lineage.
4. Compare published assemblies with Minimap2.
5. Compare published assemblies with MUMmer/NUCmer and DNAdiff.
6. Record how filtering and layout affect MUMmerplot interpretation.

## Current published-assembly BUSCO baseline

### Cai published

| Predictor | Complete | Fragmented | Missing | Internal-stop complete BUSCOs |
|---|---:|---:|---:|---:|
| AUGUSTUS | 47.5% | 3.3% | 49.1% | not reported |
| Miniprot | 49.3% | 5.4% | 45.4% | 47 |

Assembly summary:

- 1,276,270,856 bp
- 128,027 scaffolds
- 216,625 contigs
- 7.319% gaps
- scaffold N50: 952 kb
- contig N50: 19 kb

### Guo published

| Predictor | Complete | Fragmented | Missing | Internal-stop complete BUSCOs |
|---|---:|---:|---:|---:|
| AUGUSTUS | 49.7% | 2.5% | 47.8% | not reported |
| Miniprot | 51.2% | 4.5% | 44.2% | 43 |

Assembly summary:

- 2,060,974,854 bp
- 18,718 scaffolds
- 26,955 contigs
- 1.865% gaps
- scaffold N50: 251 kb
- contig N50: 106 kb

## MUMmerplot interpretation

Three visualizations may appear dramatically different despite using the same biological samples:

1. Broad or weakly filtered Galaxy plot — saturated by repetitive and ambiguous matches.
2. Strict MUMmer many-to-many plot — retains repeat-related correspondence while reducing weaker noise.
3. Strict one-to-one plot — reveals the strongest shared assembly backbone.

A diagonal generated after `--layout` represents alignment-informed contig ordering, not chromosome order.

## Known DNAdiff lesson

Breakpoint, relocation, translocation, and inversion estimates are assembly-level discordance metrics. They must not be interpreted automatically as validated biological structural variants.

## Outputs to retain

- paper-method summary
- software and parameter table
- BUSCO summaries
- QUAST summaries
- Minimap2 command and PAF summary
- NUCmer commands
- strict and many-to-many plots
- DNAdiff report
- interpretation notes
