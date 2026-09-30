# Changelog

## 0.3.0 — 2026-09-30

### Project restructuring

- Reframed RE-SAPRIA around the central question of how much apparent Cai–Guo genomic divergence reflects **biological variation versus reconstruction- and annotation-dependent effects**.
- Replaced the original symmetric Cai/Guo reassembly plan with the current evidence-based phase structure.
- Renamed Phase 2 from the abandoned Guo-reassembly branch to **`02_phase2_cai_mapping_to_guo/`**.
- Documented the unsuccessful Guo Flye reconstruction as technical provenance rather than treating it as biological evidence.
- Defined the current main analytical genome representations:
  - Guo published;
  - Cai published;
  - Cai min1250;
  - Cai Flye–HyPo;
  - Cai fixed-on-Guo.
- Expanded the repository README into a visitor-facing scientific overview with the three central hypotheses, current key results, interpretation limits, project logic, and literature references.

### Phase 1 — Cai independent reassembly

- Finalized **Cai Flye–HyPo** as the principal independent Cai reconstruction.
- Current SeqKit metrics:
  - 10,435 contigs;
  - 966,497,149 bp total span;
  - N50 = 1,056,318 bp;
  - 0 ambiguous `N` bases.
- Retained the unpolished Flye draft and polishing history as provenance.
- Adopted HyPo-polished Cai as the downstream independent-reconstruction comparator.

### Phase 2 — Cai mapping to Guo

- Completed independent Cai ONT and Illumina mapping against the published Guo assembly.
- Cai ONT → Guo:
  - 92.68% primary mapping;
  - 88.11% reference breadth;
  - ~14.4× mean depth.
- Cai Illumina → Guo:
  - 97.87% primary mapping;
  - ~92.93% reference breadth;
  - ~41.94× mean depth.
- Finalized the strict small-variant set:
  - 4,535,955 total high-confidence variants;
  - 3,704,632 SNPs;
  - 831,323 indels;
  - 1,158,638 homozygous-alternate calls.
- Retained **54,117 PASS ONT structural-discrepancy calls** from Sniffles2, using conservative terminology rather than assuming all are biological structural variants.
- Constructed the **Cai fixed-on-Guo** analytical pseudogenome by applying confident Cai homozygous-alternate alleles to the Guo structural backbone.
- Added phase-level documentation for mapping, coverage masks, variants, structural discrepancies, Cai-fixed, and the failed Guo-reassembly branch.

### Phase 3 — Harmonized genome comparison

- Marked **Phase 3 complete**.
- Added harmonized SeqKit statistics for the principal genome representations and the Cai minimum-length filtering series.
- Validated **1,250 bp** as the practical published-Cai scaffold cutoff:
  - 128,027 → 99,251 FASTA records;
  - 97.49% of assembled sequence retained;
  - negligible effect on RNA-seq mappability;
  - no loss of complete AUGUSTUS BUSCOs and only one complete Miniprot BUSCO relative to published Cai.
- Added harmonized BUSCO 5.8.0 results using `embryophyta_odb10` with both AUGUSTUS and Miniprot.
- Added BUSCO stacked horizontal bar visualizations and expanded summary tables.
- Confirmed that Guo and Cai fixed-on-Guo are nearly indistinguishable in conserved-gene recovery.
- Confirmed that Cai Flye–HyPo retains comparable conserved gene space despite its substantially smaller assembly span.
- Added harmonized RNA-seq mappability comparison across Guo, Cai fixed-on-Guo, Cai Flye–HyPo, published Cai, and Cai min1250.
- Updated Phase 0 documentation to distinguish **scaffold continuity from underlying contig continuity**, including the published Cai contrast:
  - scaffold N50 ≈ 952 kb;
  - contig N50 ≈ 19 kb;
  - 7.319% gap content.

### Phase 4 — Repeat annotation

- Opened Phase 4 as the active repeat-analysis stage.
- Standardized the downstream role of RepeatModeler/RepeatMasker outputs for:
  - softmasked genome generation;
  - repeat-feature GFF annotation;
  - genome-wide repeat summaries;
  - later gene/repeat overlap analyses.
- Large repeat catalogues and alignment-level intermediates remain archival rather than GitHub targets.

### Phase 5 — Structural gene annotation

- Defined Phase 5 as the home for standardized BRAKER, AUGUSTUS, Helixer, and annotation-comparison analyses.
- Completed the main softmasked BRAKER runs for Guo, Cai min1250, Cai fixed-on-Guo, and Cai Flye–HyPo; detailed repository archiving is ongoing.
- Retained the failed Guo-unmasked BRAKER attempts as technical provenance.
- Established a controlled AUGUSTUS masking experiment using the same Guo-trained model:
  - unmasked Guo: 106,782 predicted genes and 434,794 CDS features;
  - softmasked Guo: 30,906 predicted genes and 153,165 CDS features.
- Retained Helixer as an orthogonal land-plant prediction control; the current Guo unmasked and softmasked runs produced identical outputs.

### Documentation and reproducibility

- Reworked the main README into an **Importance–Significance–Impact** narrative for both technical users and external scientific visitors.
- Added explicit interpretation limits throughout the repository:
  - two accessions are not a population sample;
  - assembly span is not automatically biological genome size;
  - structural discrepancies are not automatically biological structural variants;
  - additional unmasked gene predictions are not automatically genuine genes.
- Added DOI-linked references for the two published *Sapria* genomes and major methodological tools.
- Began pruning stale placeholder structure and obsolete planning documents from the early repository layout.

---

## 0.2.0 — 2026-07-26

- Marked Phase 0 as complete.
- Archived four published-assembly BUSCO summaries.
- Archived the published Cai-versus-Guo DNAdiff report.
- Added Galaxy broad, Gargantua many-to-many, and Gargantua strict one-to-one MUMmerplots.
- Rewrote the Phase 0 README with quantitative results, figure interpretation, limitations, and completion criteria.
- Added a reproducible MUMmer4 command record.

---

## 0.1.0 — 2026-07-26

- Initialized RE-SAPRIA repository structure.
- Added Phase 0 published baseline.
- Added Cai Phase 1.0 Flye results and QC summaries.
- Added plans for Cai polishing, Guo reassembly, harmonized comparison, repeat annotation, gene annotation, and manuscript outputs.
- Added a separate exploratory internship track for Andrian.
