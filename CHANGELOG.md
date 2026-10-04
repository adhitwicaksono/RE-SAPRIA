# Changelog

Major analytical and repository milestones for RE-SAPRIA.

---

## 0.5.0 — 2026-10-04

### Phase 6 complete

- Completed representative CDS and peptide sequence preparation and QC.
- Completed functional annotation using DIAMOND against Swiss-Prot and NR.
- Completed eggNOG-mapper functional annotation.
- Completed InterProScan / Pfam domain analysis.
- Completed cross-representation OrthoFinder analysis.
- Completed BUSCO protein-mode validation.
- Integrated structural, repeat-aware, sequence-level, functional, and
  comparative evidence.
- Froze the Phase 0–6 analytical workflow for manuscript preparation.
- Retained orphan-like proteins as exploratory observations rather than making
  unsupported lineage-specific or de novo gene claims.

### Phase 7 initiated

- Opened manuscript-preparation phase.
- Defined the manuscript synthesis around the three central RE-SAPRIA
  hypotheses:
  - biological divergence versus reconstruction;
  - repeat-dependent annotation;
  - repeat-expanded giant introns.
- Prepared manuscript figure-plate and source-table framework.
- Adopted a Phase 7 freeze rule: additional core analysis should be performed
  only to resolve manuscript ambiguities, reviewer requests, or analytical
  corrections.
- Integrated manuscript-level interpretation is intentionally reserved for the
  manuscript and eventual preprint/publication.

### Project state

**Phases 0–6 complete.**

**Phase 7 active — manuscript preparation.**

---

## 0.4.0 — 2026-10-02

### Phase 4 — repeat analysis complete

- Completed RepeatMasker analysis across:
  - Guo published;
  - Cai fixed-on-Guo;
  - Cai published;
  - Cai min1250;
  - Cai Flye–HyPo.
- Repeat-masked sequence accounts for **84.32–90.35% of non-N sequence** across representations.
- Found that approximately **94–95% of the Guo-versus-Cai non-N assembly-span difference** is concentrated in repeat-masked sequence.
- Found that published Cai versus Cai Flye–HyPo differs by ~216.5 Mb of non-N sequence, of which ~212.0 Mb (**97.91%**) is repeat-masked.
- Validated Cai min1250 as a repeat-space-preserving technical filter; base-level repeat-mask Jaccard on retained sequence is **0.941**.
- Identified strong repeat-class assignment sensitivity across independently learned RepeatModeler libraries.
- Adopted the interpretation rule that cross-representation biological conclusions should prioritize:
  - total repeat burden;
  - coordinate-level repeat overlap;
  - representation-robust patterns;
  rather than raw repeat-class percentage shifts.

### Phase 5B — core repeat-aware interpretation complete

- Recomputed repeat–gene architecture using the standardized four-way BRAKER3 panel.
- Representative intronic sequence is **73.45–76.30% repeat-overlapped**, compared with **11.45–17.41%** for CDS.
- Intron length versus repeat fraction is strongly positive in every representation (**Spearman ρ = 0.658–0.748**).
- Confirmed that introns ≥10 kb represent only ~9–11% of representative introns but contain ~67–72% of total representative intronic sequence.
- Confirmed persistence of all five Guo ≥100-kb giant-intron loci in overlapping Cai fixed-on-Guo models.
- Added direct repeat evidence to the AUGUSTUS masking control:
  - 60,530 unmasked-only models lack a same-strand softmasked AUGUSTUS counterpart;
  - their median gene-span and CDS repeat fractions are both 100%;
  - only 6.21% overlap an RNA-supported BRAKER gene on the same strand.
- Strengthened the interpretation from generic “masking sensitivity” to a **repeat-associated, weakly RNA-supported prediction expansion** when repetitive sequence is exposed.

### Phase 6 — begun

- Defined an early structural candidate set for repeat-expanded host-gene models.
- Locked the representative-transcript rule:
  - longest total CDS length per gene;
  - transcript span and transcript ID as deterministic tie-breakers.
- Locked the functional-annotation direction:
  - representative proteins as the primary functional input;
  - DIAMOND `blastp` against Swiss-Prot first;
  - broader NR rescue for weak/no Swiss-Prot hits;
  - InterProScan/Pfam, eggNOG-mapper, OrthoFinder, and BUSCO protein mode;
  - CDS retained for nucleotide/codon-level downstream analysis.
- Standardized sequence extraction to use each BRAKER GFF3 with its **matching softmasked genome FASTA**.

### Documentation

- Reduced the root README to a concise project overview and navigation hub.
- Moved detailed analytical interpretation to phase-specific READMEs.
- Prepared a canonical six-figure visual story for:
  1. repeat/non-repeat sequence space;
  2. repeat contribution to span discrepancy;
  3. long-intron architecture;
  4. intron-versus-CDS repeat occupancy;
  5. repeat occupancy versus intron size;
  6. AUGUSTUS repeat/evidence behavior.

---

## 0.3.0 — 2026-09-30

### Project reframing and Phases 1–3

- Reframed RE-SAPRIA around the question of **biological divergence versus reconstruction- and annotation-dependent effects**.
- Finalized the principal analytical genome representations:
  - Guo published;
  - Cai published;
  - Cai min1250;
  - Cai Flye–HyPo;
  - Cai fixed-on-Guo.
- Finalized Cai Flye–HyPo as the principal independent Cai reconstruction:
  - 10,435 contigs;
  - 966,497,149 bp;
  - N50 = 1,056,318 bp;
  - no ambiguous `N` bases.
- Completed Cai ONT and Illumina mapping to Guo:
  - ONT primary mapping = 92.68%;
  - ONT breadth = 88.11%;
  - Illumina primary mapping = 97.87%;
  - Illumina breadth ≈ 92.93%.
- Finalized the strict small-variant set:
  - 4,535,955 total variants;
  - 3,704,632 SNPs;
  - 831,323 indels;
  - 1,158,638 homozygous-alternate calls.
- Retained 54,117 PASS ONT structural-discrepancy calls with conservative terminology.
- Constructed the Cai fixed-on-Guo analytical pseudogenome.
- Marked Phase 3 harmonized genome comparison complete.
- Validated the 1,250-bp published-Cai scaffold cutoff:
  - 128,027 → 99,251 FASTA records;
  - 97.49% of original assembled span retained;
  - negligible RNA-seq mappability change;
  - essentially unchanged BUSCO recovery.
- Confirmed that conserved-gene recovery changes far less than genome span across the major representations.

### Phase 5A — standardized structural annotation

- Completed the standardized softmasked BRAKER3 panel:
  - Guo: 29,792 genes / 34,471 transcripts;
  - Cai fixed-on-Guo: 29,887 / 34,783;
  - Cai min1250: 20,149 / 24,733;
  - Cai Flye–HyPo: 19,430 / 23,822.
- Found that Cai min1250 and Cai Flye–HyPo differ by 22.3% in assembly span but only ~3.6–3.7% in gene/transcript count.
- Found a higher start+stop structural-completeness proxy in Cai Flye–HyPo (**97.30%**) than Cai min1250 (**88.00%**).
- Re-baselined long-intron architecture using the standardized annotations.
- Established the Guo AUGUSTUS masking control:
  - unmasked = 106,782 genes;
  - softmasked = 30,906 genes.
- Archived standardized Phase 5A BRAKER3/AUGUSTUS GFF3 files on Zenodo:
  - **DOI: 10.5281/zenodo.23072450**

---

## 0.2.0 — 2026-07-26

- Completed the Phase 0 published Cai-versus-Guo baseline.
- Archived published-assembly BUSCO summaries.
- Archived the published Cai-versus-Guo DNAdiff report.
- Added broad, many-to-many, and strict one-to-one MUMmer comparisons.
- Added reproducible MUMmer4 command documentation.

---

## 0.1.0 — 2026-07-26

- Initialized the RE-SAPRIA repository.
- Added the Phase 0 published baseline.
- Added the initial Cai Flye assembly branch and QC summaries.
- Created the first phase structure for reassembly, comparison, repeat annotation, structural annotation, and manuscript outputs.
- Added Andrian's exploratory internship track.
