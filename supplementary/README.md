# Final Mummerplot Figure Plates (Supplementary)

Nucmer + dnadiff + Mummerplot were run across the genomes, between Guo genome against:
1. Cai
2. Cai minlen 1250
3. Cai mapped
4. Cai HyPo

The figure plate was constructed using the `.fplot` and `.rplot` data generated from Mummerplot. Using `make_mummer_supp_plate.py`

Command:

```
python make_mummer_supp_plate.py \
    --input-dir /path/to/files \
    --output Supplementary_Fig_S1_MUMmer
```

Run results:

```
Loading: Cai fixed-on-Guo
  Strict forward: 27,160
  Strict reverse: 0
  Additional many-to-many forward: 10,952
  Additional many-to-many reverse: 177
  Plot extent: 2.061 Gb × 2.061 Gb

Loading: Cai published
  Strict forward: 108,192
  Strict reverse: 5,141
  Additional many-to-many forward: 186,562
  Additional many-to-many reverse: 64,087
  Plot extent: 1.276 Gb × 2.061 Gb

Loading: Cai min1250
  Strict forward: 97,744
  Strict reverse: 5,541
  Additional many-to-many forward: 171,947
  Additional many-to-many reverse: 60,869
  Plot extent: 1.244 Gb × 2.061 Gb

Loading: Cai Flye-HyPo
  Strict forward: 27,368
  Strict reverse: 1,994
  Additional many-to-many forward: 68,205
  Additional many-to-many reverse: 37,332
  Plot extent: 0.966 Gb × 2.061 Gb
```
