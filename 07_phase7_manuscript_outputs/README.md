# Phase 7 — Manuscript Preparation

**Status: ACTIVE**

**Phases 0–6 are analytically complete and frozen.**

Phase 7 converts the completed RE-SAPRIA analytical record into the manuscript,
figures, tables, supplementary materials, methods, and reproducibility package.

Detailed integrated interpretation is intentionally reserved for the manuscript
and eventual preprint/publication.

---

## The three central hypotheses

RE-SAPRIA was organized around three linked hypotheses.

| Hypothesis | Phase 7 answer |
|---|---|
| **1. Biological divergence versus reconstruction** — The large differences between Cai and Guo reflect both genuine biological divergence and reconstruction-dependent effects. | **Supported.** Independent sequence evidence supports genuine Cai–Guo divergence, while alternative genome representations demonstrate substantial reconstruction sensitivity. |
| **2. Repeat architecture shapes annotation** — Extreme repeat abundance makes gene prediction sensitive to genome representation, repeat treatment, and annotation strategy. | **Supported.** Repeat visibility and genome representation materially affect the prediction landscape. |
| **3. Giant introns represent repeat-expanded gene space** — Extremely long introns are reproducible genomic features associated with expansion of repetitive sequence inside gene space. | **Structurally supported.** Long introns and their strong repeat association persist across alternative representations. Their broader functional or regulatory significance remains unresolved. |

These conclusions define the analytical endpoint of RE-SAPRIA.

The detailed evidence, interpretation, limitations, and biological implications
will be developed in the manuscript.

---

## Practical annotation recommendation for repeat-rich Rafflesiaceae

RE-SAPRIA supports **soft-masking as the default substrate for primary
structural gene annotation in *Sapria himalayana*.**

In the controlled Guo AUGUSTUS comparison, exposing repetitive sequence
increased predicted gene number from 30,906 in the softmasked genome to
106,782 in the unmasked genome. Most predictions unique to the unmasked
analysis were strongly repeat-associated and showed little concordance with
RNA-supported BRAKER annotation.

Soft-masking therefore substantially suppresses repeat-driven prediction
inflation while retaining repetitive sequence within genuine gene
architecture.

For future *Sapria* and Rafflesiaceae annotation, the recommended workflow is:

**de novo repeat discovery → RepeatMasker soft-masking → evidence-supported
structural annotation → protein/domain validation → post-annotation
repeat-overlap audit**

Unmasked annotation remains valuable as a sensitivity control and for
investigating transposable-element-associated coding space, but should not be
treated as the primary host-gene catalogue without independent evidence.

This recommendation is directly supported for *S. himalayana* and should be
tested rather than assumed to generalize identically across all Rafflesiaceae.

---

## Extreme repeat-expanded gene architecture

Locus-level ranking was used to identify representative genes carrying the
largest individual introns and the greatest intronic repeat burden.

The five Guo representative genes with introns exceeding 100 kb all contain
strongly repeat-enriched giant introns:

| Gene | Longest intron | Repeat in longest intron | CDS repeat |
|---|---:|---:|---:|
| g15453 | 115,994 bp | 74.94% | 4.25% |
| g29049 | 106,933 bp | 71.71% | 0.00% |
| g7602 | 104,518 bp | 80.61% | 0.00% |
| g3944 | 103,898 bp | 80.58% | 0.00% |
| g827 | 102,135 bp | 83.14% | 0.00% |

These loci provide concrete examples of repeat expansion occurring primarily
inside introns rather than coding sequence.

The full ranked top-20 sets are generated from the Phase 5B representative
per-gene tables and retained as manuscript/supplementary source data.

---

## Two complementary views of genome and gene-space stability

### Repeat burden

![RepeatMasker burden](../04_phase4_repeat_annotation/figures/phase4_repeat_burden_nonN.png)

Across the five principal genome representations, RepeatMasker masks
approximately **84–90% of non-N sequence**. The representation-level genome
span differences are concentrated overwhelmingly in repeat-rich sequence.

### Conserved coding-space recovery

![BUSCO protein mode](../06_phase6_functional_comparative_genomics/figures/phase6_busco_protein_mode.png)

Despite large differences in assembly span and predicted gene number,
protein-mode BUSCO recovery remains comparatively stable across the four
standardized BRAKER proteomes.

Together, these observations summarize one of the central contrasts emerging
from RE-SAPRIA: **whole-genome representation is highly sensitive to repeat-rich
sequence, whereas the recoverable conserved protein-coding core is much more
stable.**

---

## Manuscript synthesis

The manuscript is being assembled from results generated and documented in
Phases 0–6.

The principal visual narrative follows five analytical transitions:

1. genome representation and read-supported concordance;
2. repeat contribution to assembly-span disagreement;
3. repeat-expanded intron architecture;
4. repeat-dependent annotation behavior;
5. stability of conserved coding gene space across representations.

Final manuscript figure plates are maintained locally during manuscript
development and will be released with the appropriate preprint/publication
version rather than exposing the integrated unpublished Results narrative in
advance.

---

## Figure provenance

Every final figure and table must remain traceable to:

1. its analytical phase;
2. the genome representation used;
3. a compact source table;
4. the software/database version;
5. the corresponding workflow or analysis record.

Phase 7 may redesign or combine existing analyses for presentation, but it does
not create undocumented analytical branches.

---

## Analysis freeze

Phase 7 is a manuscript-preparation phase rather than a new exploratory phase.

New analysis should be added only when:

- required to resolve a manuscript-level ambiguity;
- required during peer review;
- or necessary to correct an identified analytical problem.

Otherwise, Phases 0–6 remain frozen.

---

## Scope boundary

RE-SAPRIA does not currently make a definitive claim of *Sapria*-specific or
de novo genes.

Representation-robust orphan-like proteins can be identified in the present
dataset, but lineage-specific gene origin requires suitable external
Rafflesiaceae/Malpighiales comparators and locus-level evolutionary validation.

Similarly, repeat-rich giant introns are treated as robust structural features;
specific regulatory or evolutionary functions require additional evidence.

These questions are retained as future directions rather than forced into the
current manuscript.

---

## Data archives

### Phase 4 — repeat annotation

Zenodo DOI:  
https://doi.org/10.5281/zenodo.23105473

### Phase 5A — standardized BRAKER3 and AUGUSTUS annotations

Zenodo DOI:  
https://doi.org/10.5281/zenodo.23072450

Additional manuscript-associated datasets may be archived with the preprint or
publication.

---

## Contributors

- **Adhityo Wicaksono** — project lead; conceptualization, analysis,
  interpretation, manuscript development
- **Andrian Dary Fawwaz** — research intern; analytical contributions and
  manuscript development
- **Arli Aditya Parikesit** — supervision, interpretation, manuscript
  development

AI-assisted analytical and documentation support was provided using OpenAI
ChatGPT during project development.

---

## Next

**Write the paper.**
