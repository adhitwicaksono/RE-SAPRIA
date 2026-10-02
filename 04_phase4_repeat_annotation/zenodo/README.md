# Phase 4 Zenodo deposition note

Recommended deposit type: **Dataset**

Upload the five RepeatMasker GFF3 files and five corresponding RepeatMasker summary files as individual files in one Zenodo record.

The raw files are not appropriate for ordinary Git history. GitHub should retain the compact tables, figures, scripts, and interpretation.

## Suggested title

**RE-SAPRIA Phase 4: Repeat annotations across Sapria himalayana genome representations**

## Important method note

RepeatModeler was run independently for each genome representation and each custom library was applied to its corresponding genome with RepeatMasker 4.1.5.

Therefore:
- total repeat burden and coordinate-level repeat overlap are suitable for direct analysis;
- raw repeat-class percentage differences mix genome representation and de novo library effects;
- class shifts should not automatically be interpreted as biological TE expansion/contraction.

See `phase4_zenodo_manifest.tsv` for recommended filenames, file sizes, and SHA-256 checksums.
