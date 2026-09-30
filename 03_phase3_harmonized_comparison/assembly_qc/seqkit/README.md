# SeqKit assembly statistics

This directory contains **SeqKit summary statistics** for the principal *Sapria himalayana* genome representations used in RE-SAPRIA, together with the minimum-length filtering test performed on the published Cai assembly.

These files provide a lightweight record of sequence count, total assembly span, sequence-length distribution, N50, GC content, and ambiguous-base (`N`) content before downstream comparative and annotation analyses.

## Genome representations

| Representation | Role in RE-SAPRIA | No. sequences | Assembly span (bp) | N50 (bp) | GC (%) | Ns (bp) |
|---|---|---:|---:|---:|---:|---:|
| Guo published, header-cleaned | Published Guo genome representation | 18,718 | 2,060,974,854 | 251,644 | 26.29 | 38,428,485 |
| Cai published, header-cleaned | Published Cai genome representation | 128,027 | 1,276,270,856 | 952,963 | 25.43 | 93,416,560 |
| Cai fixed on Guo | Guo structural backbone carrying confident fixed Cai sequence variants; derived pseudogenome, not an independent assembly | 18,718 | 2,060,941,893 | 251,615 | 26.29 | 38,428,485 |
| Cai Flye–HyPo reassembly | Independent Cai reconstruction from ONT reads, polished with Illumina data using HyPo | 10,435 | 966,497,149 | 1,056,318 | 28.15 | 0 |
| Cai min1200 | Published Cai with sequences <1,200 bp removed | 103,843 | 1,249,817,592 | 1,179,380 | 25.48 | 92,935,860 |
| **Cai min1250** | **Published Cai with sequences <1,250 bp removed; selected filtered representation** | **99,251** | **1,244,196,188** | **1,210,301** | **25.49** | **92,847,230** |
| Cai min1300 | Published Cai with sequences <1,300 bp removed | 95,130 | 1,238,945,336 | 1,292,621 | 25.50 | 92,756,430 |

## Why the 1,250-bp Cai filter was selected

The published Cai assembly contains **128,027 FASTA records**. A minimum-length filter was tested at 1,200, 1,250, and 1,300 bp to reduce the record count while preserving as much assembled sequence as possible.

| Minimum length | No. sequences | Assembly span (bp) | Assembly retained (%) | Sequence removed (bp) |
|---:|---:|---:|---:|---:|
| Unfiltered | 128,027 | 1,276,270,856 | 100.00 | 0 |
| 1,200 bp | 103,843 | 1,249,817,592 | 97.93 | 26,453,264 |
| **1,250 bp** | **99,251** | **1,244,196,188** | **97.49** | **32,074,668** |
| 1,300 bp | 95,130 | 1,238,945,336 | 97.08 | 37,325,520 |

The **1,250-bp cutoff** was selected because it reduced the published Cai assembly to fewer than 100,000 FASTA records while retaining **97.49%** of the original assembled sequence. This filtered representation was subsequently used where the fragmentation of the full published Cai FASTA created practical limits for downstream analysis.

The filtering decision was also evaluated separately using BUSCO and RNA-seq mapping results; those results are stored in their corresponding RE-SAPRIA directories.

## Interpretation notes

- **Cai min1200, min1250, and min1300 are filtered derivatives of the published Cai assembly, not new genome assemblies.**
- The increase in N50 after minimum-length filtering is an expected consequence of removing many short records and must **not** be interpreted as an improvement in the biological reconstruction of the genome.
- **Cai fixed on Guo is a derived pseudogenome/control**, preserving the Guo scaffold framework while incorporating confident fixed Cai variants. Its assembly span and sequence count therefore closely resemble Guo by design.
- The Cai Flye–HyPo representation is structurally distinct from the published Cai assembly: it contains 10,435 sequences, no `N` bases in the SeqKit summary, and a total span of approximately 966.5 Mb.
- Assembly-size differences among these representations should not, by themselves, be interpreted as biological genome-size differences between accessions.

## Files represented here

The source SeqKit outputs in this directory correspond to:

- `SeqKit statistics on Guo.tsv`
- `SeqKit statistics on Cai.tsv`
- `SeqKit statistics on Cai mapped on Guo (fixed).tsv`
- `SeqKit statistics on Cai Reassembly.tsv`
- `SeqKit statistics on Cai min 1200.tsv`
- `SeqKit statistics on Cai 1250.tsv`
- `SeqKit statistics on Cai min 1300.tsv`

For software versions and broader workflow provenance, see the repository-level `SOFTWARE_VERSIONS.tsv`, `DATA_MANIFEST.tsv`, and phase-specific documentation.
