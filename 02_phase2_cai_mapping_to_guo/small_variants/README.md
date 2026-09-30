# High-confidence Cai-versus-Guo small variants

This directory documents stringent small-variant calls obtained from Cai Illumina reads mapped to the Guo assembly.

## Frozen strict call set

| Variant class | Count |
|---|---:|
| Total strict high-confidence variants | 4,535,955 |
| SNPs | 3,704,632 |
| Indels | 831,323 |
| Heterozygous-like calls | 3,377,317 |
| Homozygous-alternate calls | 1,158,638 |

## Core filtering logic

Basic filters included:

- QUAL ≥30
- GQ ≥20
- DP between 10 and 100

The strict call set additionally applied allele-balance criteria to heterozygous-like calls and required an alternate-allele fraction ≥0.80 for homozygous-alternate calls.

## Genomic distribution of strict variants

Frozen compartment counts:

| Compartment | Variant count |
|---|---:|
| CDS | 22,704 |
| Intron-only | 681,920 |
| Intergenic | 3,831,331 |
| Repeat | 4,177,871 |
| Nonrepeat | 358,084 |

Because genomic compartments can overlap conceptually (for example, repeats can occur within introns), compartment totals should not be summed as mutually exclusive categories unless explicitly constructed that way.

## Interpretation

These are read-supported Cai-versus-Guo differences in a Guo coordinate system. They are not population variants and should not be generalized to Thailand-versus-China regional differentiation from two accessions.

The homozygous-alternate subset was used to construct the Cai-fixed-on-Guo pseudogenome.
