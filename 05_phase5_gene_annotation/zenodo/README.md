# Phase 5 Zenodo deposition note

The raw GFF3 files are too large and too primary-output-like for normal GitHub history. They should be deposited on Zenodo and linked back to RE-SAPRIA.

## Recommended deposited filenames

- `Guo_softmasked_BRAKER3.gff3.gz`
- `Cai_fixed_on_Guo_softmasked_BRAKER3.gff3.gz`
- `Cai_min1250_softmasked_BRAKER3.gff3.gz`
- `Cai_Flye_HyPo_softmasked_BRAKER3.gff3.gz`
- `Guo_softmasked_AUGUSTUS_control.gff3.gz`
- `Guo_unmasked_AUGUSTUS_control.gff3.gz`

## Metadata to record with the deposit

For each file, record:

- genome representation;
- masking state;
- predictor/workflow;
- RNA evidence used or absent;
- protein evidence used or absent;
- relevant software versions;
- creation date/history identifier;
- SHA-256 checksum.

The checksum and source-filename mapping are in `../tables/phase5_zenodo_manifest.tsv`.

After deposition, add the Zenodo DOI here and to the main repository README.

## Important interpretation note

`Cai fixed-on-Guo` is an analytical pseudogenome and not an independent Cai assembly.

The two AUGUSTUS files are methodological controls and should not be presented as primary gene annotations.
