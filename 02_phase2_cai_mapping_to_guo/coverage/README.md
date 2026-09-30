# Cai-on-Guo coverage masks

This directory stores or documents derived genomic intervals used to distinguish confidently supported/callable Guo sequence from regions with weak or absent Cai read support.

## Canonical interval sets

Two interval masks are central to downstream analyses:

- `Cai_ONT_on_Guo_SUPPORTED_DP5.bed`  
  Guo genomic intervals supported by Cai ONT depth ≥5.

- `Cai_Illumina_on_Guo_CALLABLE_DP10-100.bed`  
  Guo genomic intervals within the selected Illumina depth window of 10–100.

These masks are used to prevent unsupported sequence from being treated as equivalent to confidently interrogated sequence in later variant, structural-discrepancy, and genome-compartment analyses.

## Related Guo compartment BEDs

Later analyses may intersect support/callability masks with the following Guo genomic compartments:

- `Guo_GENE_union.bed`
- `Guo_CDS_union.bed`
- `Guo_INTRON_union.bed`
- `Guo_INTRON_ONLY.bed`
- `Guo_REPEAT_union.bed`
- `Guo_CDS_INTRON_union.bed`
- `Guo_INTERGENIC.bed`
- `Guo_NONREPEAT.bed`

## Interpretation

Coverage masks describe evidence availability, not biological presence/absence. Regions lacking Cai read support can reflect true divergence, repetitive or low-mappability sequence, sequencing depth, or assembly/reconstruction differences.
