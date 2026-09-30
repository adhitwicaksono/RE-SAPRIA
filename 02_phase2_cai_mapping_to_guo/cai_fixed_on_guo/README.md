# Cai-fixed-on-Guo pseudogenome

This directory documents the Cai-fixed analytical pseudogenome.

## Concept

The Cai-fixed representation was created by applying confident homozygous-alternate Cai variants to the Guo genome backbone.

Its purpose is experimental control:

- retain Guo scaffold structure and coordinate organization;
- introduce strongly supported Cai fixed alleles;
- hold large-scale reconstruction largely constant;
- separate sequence-level divergence from assembly/reconstruction effects.

This is **not an independently assembled Cai genome**.

## SeqKit summary

| Metric | Value |
|---|---:|
| Sequences | 18,718 |
| Total length | 2,060,941,893 bp |
| Minimum sequence length | 5,125 bp |
| N50 | 251,615 bp |
| GC | 26.29% |
| Ns | 38,428,485 |

For comparison, the Guo backbone contains the same 18,718 sequence records and 38,428,485 Ns. The small change in total length reflects Cai indels introduced onto the Guo coordinate framework.

## RNA-seq mapping control

Mean HISAT2 overall alignment rates for the same three Guo RNA-seq libraries were approximately:

- Guo: **96.92%**
- Cai-fixed: **96.79%**
- Cai Flye–HyPo: **95.88%**
- published Cai: **95.24%**
- Cai min1250: **95.15%**

The near-equivalence of Guo and Cai-fixed transcriptomic mappability supports its use as a sequence-divergence control.

## Downstream role

Cai-fixed is carried into later phases for:

- BUSCO and general assembly QC;
- repeat annotation;
- standardized BRAKER annotation;
- comparison with Guo and independently reconstructed Cai genomes.
