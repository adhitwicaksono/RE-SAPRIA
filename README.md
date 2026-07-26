# RE-SAPRIA

**RE-SAPRIA** is a reproducible reassembly and comparative-genomics project for two published *Sapria himalayana* genome datasets:

- **Cai dataset / Thailand accession** — Oxford Nanopore long reads with published scaffolded assembly.
- **Guo dataset / China accession** — twelve PacBio Sequel II long-read runs plus Illumina data.

The project does not treat either published assembly as unquestioned ground truth. Instead, both datasets are reprocessed through a harmonized workflow, evaluated with the same metrics, and compared at several checkpoints.

## Main objectives

1. Reconstruct Cai and Guo independently from their own long reads.
2. Evaluate draft assemblies before and after short-read polishing.
3. Compare published and reassembled genomes using identical QC and alignment procedures.
4. build standardized repeat, structural-gene, and functional annotations.
5. Document all decisions, failed trials, settings, and evidence in a form suitable for training, reproducibility, and manuscript preparation.

## Repository philosophy

This repository is an **analysis notebook and provenance record**, not a polished software package.

Large primary data are not stored here. The repository should contain:

- accession manifests;
- Galaxy commands and histories;
- software versions;
- small QC outputs;
- summary tables;
- scripts;
- plots;
- decisions and interpretations;
- manuscript-ready materials.

Do not upload raw FASTQ, BAM, full genome FASTA, or other very large files.

## Phase map

| Phase | Scope | Status |
|---|---|---|
| Phase 0 | Published Cai and Guo baseline comparison | Complete |
| Phase 1.0 | Cai ONT Flye draft assembly | Complete |
| Phase 1.1 | Cai Illumina polishing | Planned |
| Phase 1.2 | Cai final assembly selection | Planned |
| Phase 2.0 | Guo PacBio Flye draft assembly | Planned |
| Phase 2.1 | Guo Illumina polishing | Planned |
| Phase 2.2 | Guo final assembly selection | Planned |
| Phase 3 | Harmonized Cai–Guo comparison | Planned |
| Phase 4 | Repeat annotation | Planned |
| Phase 5 | Structural gene annotation | Planned |
| Phase 6 | Functional and comparative genomics | Planned |
| Phase 7 | Manuscript and supplementary outputs | Planned |
| Track 90 | Andrian exploratory internship analyses | Active |

## Current Cai Flye checkpoint

The first Cai ONT Flye draft was generated in Galaxy with Flye 2.9.6:

```bash
flye --nano-raw input_0.fastq.gz -o out_dir -t ${GALAXY_SLOTS:-4} -i 1
```

No genome-size estimate was supplied.

Key results:

| Metric | Cai Flye v1 |
|---|---:|
| Assembly span | 963,878,780 bp |
| Contigs | 10,435 |
| Largest contig | 8,082,338 bp |
| Contig N50 | 1,036,241 bp |
| L50 | 199 |
| GC | 28.4% |
| BUSCO, AUGUSTUS | C:31.0%, F:6.5%, M:62.5% |
| BUSCO, Miniprot | C:49.8%, F:4.2%, M:46.0% |
| Miniprot BUSCOs with internal stops | 109 |
| Primary ONT read mapping | 92.40% |
| Overall mapped alignment records | 96.91% |
| Assembly breadth covered by ONT reads | 99.895% |
| Genome-wide mean depth | 31.13× |
| Main long-contig depth | approximately 13–15× |

The draft was accepted for short-read polishing. The original ONT reads were cleared for removal from Galaxy after mapping and coverage QC were saved.


## Project team

- **Dr. Adhityo Wicaksono (Aether Biomics, Indonesia)** — Project lead and main analyst
- **Prof. Dr. rer. nat. Arli Aditya Parikesit (Indonesia International Institute for Life-Sciences (i3L))** — Co-supervisor
- **Andrian Dary Fawwaz (Indonesia International Institute for Life-Sciences (i3L))** — Student research intern
- **H.E.L.I.O.S. (Hyper-Efficient Logic & Innovation Organization System) (OpenAI ChatGPT)** — AI-assisted analysis, workflow design, interpretation, and documentation support

## Suggested citation status

This repository is an active research record and should not yet be cited as a finalized genome resource.

## Maintainer

Adhityo Wicaksono

## Primary source publications

The two published *Sapria himalayana* genome resources reanalyzed in RE-SAPRIA originate from:

1. Cai L, Arnold BJ, Xi Z, et al. (2021). Deeply altered genome architecture in the endoparasitic flowering plant *Sapria himalayana* Griff. (Rafflesiaceae). *Current Biology* 31(5):1002–1011.e9. https://doi.org/10.1016/j.cub.2020.12.045

2. Guo X, et al. (2023). The *Sapria himalayana* genome provides new insights into the lifestyle of endoparasitic plants. *BMC Biology* 21:134. https://doi.org/10.1186/s12915-023-01620-3

These publications should be cited when using, discussing, or redistributing analyses derived from the corresponding published assemblies or sequencing datasets.

## License

This repository is licensed under **MIT License**.

## Disclaimer

Two accessions do not represent species-wide populations or regional adaptation. Assembly differences must not be interpreted automatically as biological structural variation without orthogonal validation.
