# Phase 6 — Functional and Comparative Genomics

**Status: Beginning — structural candidate triage complete; functional annotation pending protein extraction**

## Objective

Phase 6 assigns functional evidence to structurally robust gene models and asks which biological conclusions survive changes in genome reconstruction, repeat architecture, and annotation strategy.

The first Phase 6 step is deliberately structural: identify loci worth carrying forward before attaching functional labels.

---

## 1. Early repeat-expanded gene candidate sets

A conservative **Tier A** structural candidate requires:

- a representative transcript with explicit start and stop codons;
- longest intron ≥50 kb;
- total intronic repeat fraction ≥75%;
- CDS repeat fraction ≤10%.

Current Tier A counts:

| Representation | Tier A genes |
|---|---:|
| **Guo published** | **179** |
| **Cai fixed-on-Guo** | **166** |
| **Cai min1250** | **160** |
| **Cai Flye–HyPo** | **183** |

![Tier A candidates](phase6_early_tierA_candidate_counts.png)

A broader Tier B set uses the same criteria but lowers the longest-intron threshold to ≥10 kb.

These are **candidate repeat-expanded host gene models**, not yet functionally validated genes and not yet cross-representation ortholog sets.

The representation-specific candidate tables are under [`tables/`](tables/).

---

## 2. Extreme ≥100-kb intron loci

The standardized annotations contain:

- Guo: **5** genes with a longest intron ≥100 kb
- Cai fixed-on-Guo: **6**
- Cai min1250: **7**
- Cai Flye–HyPo: **4**

All five Guo ≥100-kb loci persist in overlapping Cai-fixed models.

These loci are high-priority candidates for later domain annotation, orthology analysis, repeat-composition inspection, and manual genome-browser review.

---

## 3. Locked functional-annotation direction

Once the BRAKER peptide FASTAs are available, the functional branch will use **one representative protein per gene**, selected from the same longest-total-CDS representative transcript rule used in the structural analysis.

### Protein FASTA — primary functional evidence

Planned analyses:

- **DIAMOND blastp against Swiss-Prot** as the first curated homology layer;
- broader **NR rescue** for weak/no Swiss-Prot matches;
- **InterProScan**;
- **Pfam/domain analysis**;
- **eggNOG-mapper**;
- **OrthoFinder**;
- **BUSCO protein mode**.

Protein-level functional labels will be integrated across evidence sources rather than copied blindly from one top hit.

### CDS FASTA — retained for sequence-level work

Planned uses:

- nucleotide-level homology;
- codon analyses;
- Ka/Ks where appropriate;
- sequence validation;
- transcript/gene reconstruction checks.

---

## 4. Protein extraction rule

For each standardized BRAKER annotation:

1. use the **exact corresponding softmasked genome FASTA** used by that annotation;
2. extract CDS and peptide sequence using `gffread`;
3. preserve all transcript IDs;
4. choose one representative transcript per gene by **longest total CDS length**;
5. retain all isoforms separately for archival/reference purposes;
6. perform basic protein QC before functional annotation.

Protein QC should include internal stop codons, suspiciously short proteins, suspiciously long proteins, and ID mismatches between GFF3 and FASTA.

---

## Interpretation principles

- a repeat-rich intron does not establish function;
- repeat overlap in a CDS requires scrutiny and may indicate TE-associated prediction;
- absence of a Swiss-Prot hit is not evidence of novelty;
- apparent gene-family expansion must be checked for fragmented or repeat-derived models;
- cross-representation robustness should precede strong biological claims.

---

## Representative longest-CDS rule
One transcript per gene was selected by **maximum extracted CDS length**. BRAKER IDs follow `gN.tM`, so gene membership is recovered from the prefix. The representative counts exactly match the standardized Phase 5 BRAKER gene counts: 29,792 (Guo), 29,887 (Cai fixed), 20,149 (Cai min1250), and 19,430 (Cai Flye–HyPo).

For exact CDS-length ties, transcript ID was used deterministically because transcript-span metadata is not present in this FASTA upload. Only 27, 34, 29, and 20 genes, respectively, have such ties. The locked Phase 5 structural rule used transcript span and then transcript ID after longest total CDS, so only this very small tied subset could differ from the structural representative list.

## CDS analyses completed
- CDS length and frame checks
- canonical start / terminal-stop proxies
- representative translation and internal-stop checks
- ambiguous-base checks
- GC and GC3 summaries
- lowercase/softmasked fraction retained in CDS
- representative codon usage
- exact CDS-sequence redundancy
- strict sequence-quality candidate FASTAs for later codon-aware analyses

The Ka/Ks FASTAs are **prefilters only**. Ka/Ks still requires defensible ortholog pairs and codon-aware alignment.

## Peptide analyses completed
- protein length distributions
- internal stop-marker and `X` checks
- representative CDS↔PEP translation concordance
- exact protein-sequence redundancy
- representative amino-acid composition
- short/long/extreme-length review flags
- representative longest-CDS peptide FASTAs

Flags are review signals, not automatic exclusions.

## DIAMOND-ready files
Use `analysis_ready/DIAMOND/`. It contains four individual representative-proteome FASTAs and one combined query FASTA with representation-prefixed IDs.

Locked functional direction: **Swiss-Prot DIAMOND blastp → NR rescue → InterPro/Pfam → eggNOG → OrthoFinder/BUSCO protein mode → evidence integration.**

## CDS downstream direction
Use `representative_CDS/` for nucleotide homology, orthology-confirmed codon analyses, Ka/Ks preparation, and gene-model validation. `analysis_ready/KaKs_strict_CDS/` is only a high-quality sequence candidate pool.

## Key QC observations
- Guo, Cai fixed, and Cai Flye–HyPo representative CDS↔PEP translations are fully concordant under the standard code.
- Cai min1250 has 34 representative translation exceptions (~0.17%), all associated with ambiguous `N` sequence.
- The strict sequence-level complete-ORF proxy is highest in Cai Flye–HyPo (~96.84%) and lowest in Cai min1250 (~84.37%), independently echoing the Phase 5 structural-completeness pattern.
- Lowercase/softmasked bases occupy ~9–14% of extracted CDS sequence; coordinate-level RepeatMasker overlap remains authoritative for repeat interpretation.

## Start here
- `tables/sequence_QC_summary.tsv`
- `tables/representative_longest_CDS_mapping.tsv`
- `tables/representative_basic_QC.tsv.gz`
- `tables/flagged_representative_models_for_review.tsv.gz`
- `tables/translation_concordance_exceptions_representatives.tsv`
- `tables/codon_usage_representatives.tsv`
- `tables/amino_acid_composition_representatives.tsv`
- `tables/exact_sequence_duplicate_summary.tsv`

## Guardrails
- Non-ATG starts may be partial models, not exotic biology.
- Internal stops need locus-level review.
- Lowercase bases are a FASTA-level softmask signal, not a substitute for coordinate-level RepeatMasker overlap.
- Exact duplicate proteins may have several biological or annotation causes.
- No Swiss-Prot hit is **not** evidence of novelty.
