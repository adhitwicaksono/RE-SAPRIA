# Contributing to RE-SAPRIA

RE-SAPRIA is an active comparative-genomics research project focused on *Sapria himalayana*. The repository functions as a **reproducible analysis record, provenance archive, and manuscript-development workspace** rather than as a general-purpose software package.

Contributions are welcome when they strengthen reproducibility, biological interpretation, or the manuscript-grade analytical stream.

---

## 1. General principles

All contributions should follow five rules:

1. **Preserve provenance.**  
   Record where an input came from, how it was transformed, and which software/settings were used.

2. **Separate observation from interpretation.**  
   Report what the data show before assigning biological meaning.

3. **Do not erase informative failures.**  
   Failed major analytical branches should be documented when they affect project decisions.

4. **Do not inflate conclusions.**  
   Two accessions are not a population sample, assembly discordance is not automatically biological structural variation, and additional gene predictions are not automatically genuine genes.

5. **Keep the repository readable.**  
   GitHub should contain compact outputs, scripts, figures, summaries, and documentation. Very large primary/intermediate files belong in archival storage such as Zenodo.

---

## 2. What belongs in GitHub

Suitable repository content includes:

- README files;
- scripts;
- workflow descriptions;
- software versions;
- command records;
- compact QC reports;
- BUSCO/QUAST/SeqKit summaries;
- summary tables;
- BED/GFF files when reasonably sized;
- figures;
- manuscript-ready tables and plots;
- decision logs;
- failed-run notes that materially affect interpretation.

Avoid committing:

- raw FASTQ files;
- large BAM/CRAM files;
- full genome FASTA files;
- very large repeat catalogues or alignment intermediates;
- redundant temporary outputs;
- files that can be regenerated trivially from a documented upstream source.

Large datasets should be deposited in archival storage and linked from the relevant phase README.

---

## 3. Phase structure

The manuscript-grade workflow is organized as:

- **Phase 0** — published Cai–Guo baseline;
- **Phase 1** — independent Cai reassembly and polishing;
- **Phase 2** — Cai mapping to Guo, read support, variants, and Cai fixed-on-Guo;
- **Phase 3** — harmonized genome comparison;
- **Phase 4** — repeat discovery and repeat annotation;
- **Phase 5** — structural gene annotation and annotation-method comparison;
- **Phase 6** — functional/comparative genomics;
- **Phase 7** — manuscript outputs;
- **Track 90** — exploratory internship analyses.

Exploratory work should remain outside the main phase stream until it is:

1. reproduced;
2. quality-checked;
3. documented;
4. interpreted conservatively; and
5. judged relevant to the central RE-SAPRIA questions.

---

## 4. Required documentation for new analyses

Each manuscript-grade analysis should document, where applicable:

- biological question;
- input dataset(s);
- genome representation used;
- software and version;
- important parameters;
- filtering criteria;
- output file(s);
- QC result;
- interpretation;
- limitations;
- whether the result is exploratory, provisional, or frozen.

The relevant phase README should be updated when a checkpoint becomes stable.

If an analytical choice changes the project logic, add it to `DECISIONS.md`.

---

## 5. Naming conventions

Prefer filenames that identify:

- accession or genome representation;
- analysis type;
- important transformation;
- software/method when useful.

Examples:

```text
Cai_Flye_HyPo_seqkit.tsv
Cai_fixed_on_Guo_seqkit.tsv
Guo_published_BUSCO5.8_embryophyta_odb10_Miniprot.txt
busco_miniprot_stacked_bar.png
```

Avoid generic names such as:

```text
final.txt
new2.gff
test_output.tsv
result_latest.csv
```

unless they are temporary local files that will not enter the repository.

---

## 6. Genome-representation terminology

Use these terms consistently:

- **Guo published** — published Guo genome representation;
- **Cai published** — published Cai genome representation;
- **Cai min1250** — published Cai filtered at a minimum scaffold length of 1,250 bp;
- **Cai Flye–HyPo** — independent Cai ONT reconstruction polished with HyPo;
- **Cai fixed-on-Guo** — Guo-backbone analytical pseudogenome carrying confident Cai homozygous-alternate alleles.

`Cai fixed-on-Guo` must never be described as an independently assembled Cai genome.

---

## 7. Interpretation guardrails

The following language should be used conservatively.

### Accessions and variation

Cai and Guo represent **two accessions**, not species-wide or regional populations.

Do not describe Cai–Guo differences as:

- population polymorphism;
- Thailand-versus-China adaptation;
- species-wide variation;

without additional sampling.

### Structural differences

Use terms such as:

- **structural discrepancy**;
- **assembly-level discordance**;
- **read-supported difference**;

unless there is independent evidence sufficient to validate a biological structural variant.

### Assembly span

Assembly span is not automatically biological genome size.

Differences can reflect:

- repeat collapse or expansion;
- scaffolding;
- gaps;
- haplotypic redundancy;
- unresolved sequence;
- filtering;
- reconstruction strategy.

### Gene prediction

Do not assume:

- unmasked-only predictions are genuine genes;
- masked predictions are automatically correct;
- larger gene counts imply greater biological gene content.

Annotation results must be interpreted in the context of repeat treatment, transcript evidence, genome representation, and predictor behavior.

---

## 8. Figures and tables

Figures should be publication-readable and should state:

- what is being compared;
- which genome representation is used;
- units;
- sample size where relevant;
- whether values are exact or approximate.

Tables should retain raw counts whenever possible, not percentages alone.

Derived summary plots should be accompanied by the underlying TSV/CSV whenever practical.

---

## 9. Software and reproducibility

Whenever possible, preserve:

- software version;
- workflow version;
- Galaxy history/workflow export;
- command line;
- relevant parameter settings.

Do not silently change a method after results have been generated.

If a method changes, document the reason and keep earlier major results when they affect interpretation.

---

## 10. Failed analyses

A failed analysis should be retained when it influences project decisions.

Examples include:

- the attempted Guo Flye reconstruction;
- repeated Guo-unmasked BRAKER failures.

A failure should be described as a **technical outcome**, not converted into a biological conclusion unless the evidence supports that inference.

---

## 11. AI-assisted work

AI-assisted workflow design, coding support, interpretation, and documentation may be used in RE-SAPRIA.

All AI-assisted outputs must be:

- checked by a human researcher;
- traceable to underlying data or documented analyses;
- corrected when unsupported;
- excluded from the evidence chain unless independently verified.

AI assistance does not replace scientific responsibility or authorship criteria.

---

## 12. Authorship and credit

Repository participation does **not** automatically establish manuscript authorship.

Authorship will be based on documented intellectual and analytical contribution, including substantial involvement in one or more of:

- conceptualization;
- methodology;
- analysis;
- interpretation;
- validation;
- writing/revision;
- project-level scientific responsibility.

Routine comments, access to prior datasets, or historical association with the subject do not by themselves establish authorship.

---

## 13. Before submitting a contribution

Before adding or proposing a new result, ask:

> Does this result help establish assembly concordance, explain assembly discordance, or demonstrate a biological/annotation consequence?

If not, it may belong in:

- supplementary material;
- exploratory analysis;
- provenance;
- future work;

rather than the central manuscript stream.
