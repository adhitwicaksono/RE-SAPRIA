# Decision Log

## 2026-07-26 — Treat genome size as unknown during Flye assembly

**Decision:** Leave estimated genome size blank for Cai and Guo baseline Flye runs.

**Reason:** The project aims to reconstruct each assembly from the read data without imposing the published assembly span as a prior.

**Fallback:** A genome-size estimate may be introduced only if a future resource-saving option explicitly requires it. Such a run must be documented as a separate parameterized experiment.

---

## 2026-07-26 — Cai Flye v1 accepted for polishing

**Evidence:**

- 963,878,780 bp total span
- 10,435 contigs
- 1,036,241 bp N50
- 99.895% assembly breadth covered by ONT alignments
- 92.40% primary ONT read mapping
- BUSCO Miniprot completeness 49.8%
- Similar Miniprot completeness to published Cai and Guo
- No assembly gaps

**Limitation:**

- BUSCO AUGUSTUS completeness only 31.0%
- 109 Miniprot-complete BUSCOs contain internal stop codons
- Residual ONT errors likely disrupt coding sequences

**Decision:** Proceed to Illumina polishing. Do not use this draft as the final annotation substrate.

---

## 2026-07-26 — Original Cai ONT reads cleared for Galaxy deletion

**Condition met:**

- BUSCO complete
- ONT read-back mapping complete
- Flagstat saved
- Samtools coverage saved
- Mosdepth summary saved
- Cai Flye v1 accepted for polishing

**Decision:** The 24-GB ONT FASTQ may be permanently purged from Galaxy because the source data remain publicly retrievable.
