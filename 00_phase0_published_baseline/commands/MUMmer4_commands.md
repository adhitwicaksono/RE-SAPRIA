# Phase 0 MUMmer4 commands

## Comparison orientation

- Reference: published Cai assembly, Thailand accession
- Query: published Guo assembly, China accession

The smaller Cai assembly was used as the NUCmer reference because the Guo-reference orientation exceeded the local WSL memory ceiling on Gargantua.

## NUCmer

```bash
/usr/bin/time -v nucmer \
  --mum \
  -l 100 \
  -c 500 \
  -t 1 \
  -p CaiPublishedRef_GuoPublishedQuery_strict \
  Cai_published.fasta \
  Guo_published.fasta \
  2> CaiPublishedRef_GuoPublishedQuery_strict.time.log
```

## Strict one-to-one filtering

```bash
delta-filter -1 \
  CaiPublishedRef_GuoPublishedQuery_strict.delta \
  > CaiPublishedRef_GuoPublishedQuery_strict.1delta

show-coords -THrcl \
  CaiPublishedRef_GuoPublishedQuery_strict.1delta \
  > CaiPublishedRef_GuoPublishedQuery_strict.1coords.tsv
```

## Many-to-many filtering

```bash
delta-filter -m \
  CaiPublishedRef_GuoPublishedQuery_strict.delta \
  > CaiPublishedRef_GuoPublishedQuery_strict.mdelta

show-coords -THrcl \
  CaiPublishedRef_GuoPublishedQuery_strict.mdelta \
  > CaiPublishedRef_GuoPublishedQuery_strict.mcoords.tsv
```

## DNAdiff

```bash
dnadiff \
  -p CaiPublishedRef_GuoPublishedQuery_dnadiff \
  -d CaiPublishedRef_GuoPublishedQuery_strict.delta
```

## Strict MUMmerplot

```bash
mummerplot \
  --png \
  --layout \
  -R Cai_published.fasta \
  -Q Guo_published.fasta \
  -p CaiPublishedRef_GuoPublishedQuery_strict \
  CaiPublishedRef_GuoPublishedQuery_strict.1delta

gnuplot CaiPublishedRef_GuoPublishedQuery_strict.gp
```

## Many-to-many MUMmerplot

```bash
mummerplot \
  --png \
  --layout \
  -R Cai_published.fasta \
  -Q Guo_published.fasta \
  -p CaiPublishedRef_GuoPublishedQuery_many \
  CaiPublishedRef_GuoPublishedQuery_strict.mdelta

gnuplot CaiPublishedRef_GuoPublishedQuery_many.gp
```

## Interpretation warning

`--layout` reorders contigs according to alignment relationships. It does not reconstruct chromosomes or establish native genomic order.
