# AUGUSTUS masking control

This is a controlled Guo experiment designed to isolate the effect of masking visibility.

The genome representation and trained AUGUSTUS model are held constant; the analysis changes whether the genome is supplied as softmasked or unmasked sequence.

| Metric | Softmasked | Unmasked |
|---|---:|---:|
| Genes | 30,906 | 106,782 |
| CDS features | 153,165 | 434,794 |
| Total predicted CDS bp | 29,288,958 | 90,408,639 |
| Median gene span | 3,856 bp | 1,776 bp |
| Scaffolds with predictions | 8,953 | 16,025 |

The unmasked genome generates 3.46× as many gene models.

The result is consistent with strong masking sensitivity, but the additional predictions must not yet be called repeat-derived false positives. Coordinate-level RepeatMasker overlap is the Phase 5B test.

See [`../tables/phase5_augustus_masking_control.tsv`](../tables/phase5_augustus_masking_control.tsv) and [`../tables/phase5_augustus_vs_braker_overlap.tsv`](../tables/phase5_augustus_vs_braker_overlap.tsv).
