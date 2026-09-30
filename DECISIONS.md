# Decision Log

This file records analytical decisions that materially changed the RE-SAPRIA workflow or interpretation.

---

## 2026-07-26 — Treat genome size as unknown during Flye assembly

**Decision:** Leave estimated genome size blank for Cai and Guo baseline Flye runs.

**Reason:** The project aims to reconstruct each assembly from the read data without imposing the published assembly span as a prior.

**Fallback:** A genome-size estimate may be introduced only if a future resource-saving option explicitly requires it. Such a run must be documented as a separate parameterized experiment.

---

## 2026-07-26 — Cai Flye v1 accepted for polishing

**Evidence:**

- 963,878,780 bp total span;
- 10,435 contigs;
- 1,036,241 bp N50;
- 99.895% assembly breadth covered by ONT alignments;
- 92.40% primary ONT read mapping;
- BUSCO Miniprot completeness 49.8%;
- similar Miniprot completeness to published Cai and Guo;
- no assembly gaps.

**Limitation:**

- BUSCO AUGUSTUS completeness only 31.0%;
- 109 Miniprot-complete BUSCOs contain internal stop codons;
- residual ONT errors likely disrupt coding sequence.

**Decision:** Proceed to Illumina polishing. Do not use this draft as the final annotation substrate.

---

## 2026-07-26 — Original Cai ONT reads cleared for Galaxy deletion

**Condition met:**

- BUSCO complete;
- ONT read-back mapping complete;
- Flagstat saved;
- Samtools coverage saved;
- Mosdepth summary saved;
- Cai Flye v1 accepted for polishing.

**Decision:** The 24-GB ONT FASTQ may be permanently purged from Galaxy because the source data remain publicly retrievable.

---

## 2026-09-30 — Cai Flye–HyPo adopted as the principal independent Cai reconstruction

**Decision:** Use the HyPo-polished Flye assembly as the canonical independent Cai reconstruction for downstream comparison.

**Current metrics:**

- 10,435 contigs;
- 966,497,149 bp total span;
- N50 = 1,056,318 bp;
- 0 `N` bases.

**Reason:** It preserves the independent long-read reconstruction while providing a polished, gap-free Cai representation suitable for comparison with the published genomes.

**Interpretation limit:** This does not establish Cai Flye–HyPo as the uniquely “correct” Cai genome.

---

## 2026-09-30 — Do not force a symmetric Guo reassembly branch

**Decision:** Stop treating independent Guo reassembly as a required mirror of the Cai workflow.

**Reason:** The Guo Flye remake did not produce a usable completed assembly.

**Consequence:** The published Guo assembly remains the Guo structural representation used downstream.

**Interpretation limit:** The failed reconstruction is a technical outcome and is not evidence that the Guo genome is intrinsically unassemblable.

---

## 2026-09-30 — Redefine Phase 2 as Cai mapping to Guo

**Decision:** Replace the original `02_phase2_guo_reassembly` concept with:

`02_phase2_cai_mapping_to_guo`

**Reason:** The productive analytical branch became independent Cai read support for Guo, Cai–Guo variant calling, structural-discrepancy analysis, and construction of a Cai-on-Guo analytical pseudogenome.

**Consequence:** Phase 2 now directly supports the project’s central biological-versus-reconstruction question.

---

## 2026-09-30 — Use “structural discrepancy” rather than assuming biological SV

**Decision:** Describe the 54,117 PASS Sniffles2 calls from Cai ONT mapped to Guo as **structural discrepancies** unless independently validated.

**Reason:** Calls may reflect:

- genuine accession-level structural variation;
- repeat-associated mapping ambiguity;
- collapsed or expanded repeats;
- assembly/reconstruction differences;
- unresolved haplotypes;
- alignment limitations.

**Consequence:** Structural calls are interpreted in genomic context rather than automatically treated as biological variants.

---

## 2026-09-30 — Cai fixed-on-Guo established as the sequence-divergence control

**Decision:** Use the Guo-backbone pseudogenome carrying confident Cai homozygous-alternate alleles as a controlled comparison representation.

**Reason:** It changes Cai-like fixed sequence while holding Guo-like large-scale structure largely constant.

**Validation:**

- Guo and Cai fixed-on-Guo have nearly identical SeqKit structure;
- BUSCO completeness is nearly unchanged;
- Guo RNA-seq mappability differs only minimally between the two.

**Interpretation limit:** Cai fixed-on-Guo is not an independent Cai assembly.

---

## 2026-09-30 — Retain Cai min1250 as the published-Cai annotation-compatible representation

**Decision:** Use a minimum scaffold length of **1,250 bp** for the filtered published Cai representation.

**Reason:**

- reduces FASTA records from 128,027 to **99,251**;
- retains **97.49%** of published Cai assembled sequence;
- preserves all complete AUGUSTUS BUSCOs;
- loses only one complete Miniprot BUSCO relative to published Cai;
- changes mean RNA-seq alignment by only ~0.09 percentage points.

**Interpretation limit:** The higher N50 after filtering is a mathematical consequence of removing short records and is not evidence of improved assembly quality.

---

## 2026-09-30 — Phase 3 harmonized comparison considered complete

**Decision:** Mark Phase 3 complete.

**Evidence layers completed:**

- harmonized SeqKit statistics;
- harmonized BUSCO analysis;
- whole-genome alignment comparison;
- Cai read support for Guo;
- RNA-seq mappability comparison;
- Cai fixed-on-Guo control;
- interpretation of published-versus-independent reconstruction.

**Consequence:** New work now moves primarily into repeat biology (Phase 4) and annotation consequences (Phase 5).

---

## 2026-09-30 — Separate repeat analysis from structural gene annotation

**Decision:**

- **Phase 4** = repeat discovery, RepeatMasker summaries, repeat GFFs, softmasked genomes, and repeat architecture;
- **Phase 5** = BRAKER, AUGUSTUS, Helixer, structural gene annotation, and annotation-method comparison.

**Reason:** Repeat architecture is a biological explanatory layer, while gene prediction is a downstream response to that architecture.

---

## 2026-09-30 — Use softmasked BRAKER runs as the standardized annotation panel

**Decision:** Use the completed softmasked BRAKER analyses for:

- Guo;
- Cai min1250;
- Cai fixed-on-Guo;
- Cai Flye–HyPo.

**Reason:** These constitute the directly comparable, successfully completed RNA-supported annotation panel.

**Guo unmasked BRAKER:** repeated failures are retained as technical provenance but are not interpreted biologically.

---

## 2026-09-30 — Use fixed-model AUGUSTUS as the clean masking-control experiment

**Decision:** Compare Guo unmasked and softmasked sequence using the **same Guo-trained AUGUSTUS model** and matched settings.

**Reason:** This holds the genome sequence and gene model constant while changing repeat visibility.

**Current result:**

- unmasked: 106,782 genes; 434,794 CDS features;
- softmasked: 30,906 genes; 153,165 CDS features.

**Interpretation limit:** The additional unmasked predictions are not automatically false genes. Repeat overlap and evidence support must be quantified.

---

## 2026-09-30 — Retain Helixer as an orthogonal annotation control

**Decision:** Use Helixer as a pretrained land-plant comparison rather than as the primary annotation.

**Observation:** Current Guo unmasked and softmasked Helixer runs are identical.

**Interpretation:** In this implementation, lower-case softmasking does not alter Helixer output.

**Consequence:** Helixer is useful as an orthogonal model of plant gene structure, not as a repeat-masking experiment.

---

## 2026-09-30 — Treat scaffold continuity and contig continuity separately

**Decision:** Do not use scaffold N50 alone to describe published Cai continuity.

**Reason:** Published Cai has:

- scaffold N50 ≈ 952 kb;
- contig N50 ≈ 19 kb;
- 7.319% gap content.

The apparent scaffold continuity is therefore partly produced by scaffold joins across `N` gaps.

**Consequence:** Phase 0 and downstream documentation explicitly distinguish scaffold-based and gap-free contig continuity.

---

## 2026-09-30 — Repository stop rule

**Decision:** A result belongs in the central RE-SAPRIA story only if it does at least one of the following:

1. establishes assembly concordance;
2. explains assembly discordance;
3. demonstrates a biological or annotation consequence.

Results that do not meet this rule move to:

- supplementary material;
- exploratory analysis;
- provenance;
- future work.

This rule is used to prevent the project from becoming an uncontrolled software or benchmark catalogue.
