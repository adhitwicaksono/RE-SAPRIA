# RE-SAPRIA untuk SMA 🌺🧬
## Genome assembly bukan genom itu sendiri

RE-SAPRIA menggunakan *Sapria himalayana* untuk menunjukkan salah satu masalah paling penting dalam genomik modern:

> **Ketika dua assembly berbeda, bagaimana kita tahu apakah yang berbeda adalah biologinya atau cara kita merekonstruksi biologinya?**

Ini bukan pertanyaan filosofis. Kita dapat mengujinya dengan reads, whole-genome alignment, RNA-seq, BUSCO, variant calling, dan genome representation controls.

---

# 1. Sistem biologinya

*Sapria himalayana* adalah tumbuhan endoparasit dari Rafflesiaceae.

Kelompok ini menarik karena evolusinya melibatkan reduksi banyak fungsi tumbuhan, ketergantungan tinggi pada inang, dan perubahan genom yang ekstrem.

Tetapi RE-SAPRIA tidak hanya bertanya “seberapa aneh genom *Sapria*?”

Kami bertanya:

> **Apakah genom yang ekstrem juga menjadi lebih sulit direkonstruksi secara stabil?**

---

# 2. Paradox assembly

Tiga representasi utama:

| Genome representation | Assembly span |
|---|---:|
| **Guo published** | **2.061 Gb** |
| **Cai published** | **1.276 Gb** |
| **Cai Flye–HyPo** | **0.966 Gb** |

Perbedaan terbesar ≈ **1.09 Gb**.

Itu lebih besar daripada keseluruhan genom banyak organisme.

Namun angka assembly span bukan otomatis biological genome size.

Assembly dapat dipengaruhi oleh:

- repeat collapse;
- redundant haplotypes;
- gap/scaffolding;
- unresolved sequence;
- filtering;
- assembler behavior.

---

# 3. Scaffold N50 dapat menipu

Published Cai:

- 128.027 scaffold records;
- 216.625 gap-free contigs menurut statistik BUSCO;
- scaffold N50 ≈ **952 kb**;
- contig N50 ≈ **19 kb**;
- gaps ≈ **7,319%**.

Published Guo:

- 18.718 scaffolds;
- 26.955 contigs;
- scaffold N50 ≈ **251 kb**;
- contig N50 ≈ **106 kb**;
- gaps ≈ **1,865%**.

Jadi Cai mempunyai scaffold N50 lebih tinggi, tetapi gap-free contiguity jauh lebih rendah.

Pelajarannya:

> **Tidak ada satu metrik assembly yang boleh dibaca sendirian.**

---

# 4. Read-backed test: apakah Cai mengenali Guo?

### Oxford Nanopore

- primary mapping: **92,68%**
- Guo reference breadth: **88,11%**
- mean depth: **~14,4×**

### Illumina

- primary mapping: **97,87%**
- Guo reference breadth: **~92,93%**
- mean depth: **~41,94×**

Walaupun Guo jauh lebih besar, sebagian besar Guo masih didukung oleh sequence evidence dari Cai.

Karena itu, assembly-size difference tidak dapat langsung dianggap sebagai genome-size difference biologis.

---

# 5. Sequence divergence memang ada

Strict Cai-versus-Guo small-variant set:

| Variant | Count |
|---|---:|
| Total | **4.535.955** |
| SNP | **3.704.632** |
| Indel | **831.323** |
| Homozygous-alternate | **1.158.638** |

Long reads juga menghasilkan **54.117 PASS structural-discrepancy calls**.

Kata **discrepancy** sengaja dipakai.

Mengapa?

Karena sinyal tersebut dapat berasal dari campuran:

- true accession variation;
- repeat ambiguity;
- assembly difference;
- alignment behavior;
- collapsed/expanded regions.

Dua accession juga tidak cukup untuk membuat klaim population genomics.

---

# 6. Eksperimen kontrol: Cai fixed-on-Guo

Salah satu trik analitik terpenting RE-SAPRIA adalah membuat **Cai fixed-on-Guo**.

Pada representasi ini:

- backbone Guo dipertahankan;
- confident homozygous-alternate Cai alleles dimasukkan.

Dengan demikian, kita dapat mengubah **sequence state** sambil mempertahankan **large-scale structure** hampir tetap.

### RNA-seq test

| Representation | Mean HISAT2 alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |
| Cai min1250 | **95,15%** |

Guo → Cai-fixed hanya berubah sedikit.

Perbedaan lebih besar muncul ketika kita pindah ke independently reconstructed Cai genomes.

Interpretasi sementara:

> **Reconstruction-associated effects tampaknya berkontribusi lebih besar pada transcriptomic mappability dibanding fixed nucleotide substitutions saja.**

---

# 7. BUSCO: genome span ≠ conserved gene-space recovery

BUSCO mencari conserved single-copy ortholog groups yang umum ditemukan dalam suatu lineage.

RE-SAPRIA memakai:

- BUSCO 5.8.0;
- `embryophyta_odb10`;
- 1.614 BUSCO groups;
- AUGUSTUS dan Miniprot secara terpisah.

| Representation | AUGUSTUS Complete | Miniprot Complete |
|---|---:|---:|
| Guo | **49,7%** | **51,2%** |
| Cai fixed-on-Guo | **49,8%** | **51,4%** |
| Cai published | **47,5%** | **49,3%** |
| Cai Flye–HyPo | **47,3%** | **50,5%** |

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Assembly span berubah lebih dari dua kali lipat.

Complete BUSCO hanya berubah beberapa persen.

Ini berarti:

> **Perubahan besar pada jumlah DNA yang direkonstruksi tidak menghasilkan perubahan sebanding pada conserved gene space yang dapat dikenali.**

Tetapi jangan overclaim: missing BUSCO dapat disebabkan oleh true gene loss, divergence, fragmentation, giant gene structure, atau keterbatasan predictor.

---

# 8. Eksperimen kecil yang sangat berguna: min1250

Published Cai memiliki **128.027** FASTA records, terlalu banyak untuk beberapa workflow anotasi.

Kami membuang scaffold <1.250 bp.

Hasilnya:

- records: **128.027 → 99.251**
- sequence retained: **97,49%**
- AUGUSTUS complete BUSCO: **tidak berubah**
- Miniprot complete BUSCO: **795 → 794**
- RNA-seq mapping: **95,24% → 95,15%**

Jadi cutoff ini adalah **technical rescue**, bukan “improved assembly”.

Ini contoh bagus tentang bagaimana preprocessing harus diuji, bukan hanya dilakukan.

---

# 9. Cara berpikir ilmiah yang ingin ditunjukkan RE-SAPRIA

Pada genomik, pipeline yang baik tidak hanya menghasilkan angka.

Ia membuat **kontrol**.

RE-SAPRIA menggunakan beberapa jenis kontrol:

- published vs reassembled genome;
- reads vs assembly;
- same backbone + changed alleles;
- BUSCO dengan dua metode;
- RNA-seq ke beberapa representations;
- filtered vs unfiltered Cai.

Pertanyaan yang selalu sama:

> **Apakah kesimpulannya tetap bertahan ketika cara kita melihat genom diubah?**

---

# 10. Untuk siswa OGI: konsep yang bisa keluar dari proyek ini

RE-SAPRIA menyentuh banyak konsep olimpiade genomik:

- genome assembly;
- long reads vs short reads;
- reference mapping;
- SNP dan indel;
- structural variation;
- N50;
- scaffolds vs contigs;
- BUSCO;
- gene annotation;
- RNA-seq mapping;
- repeats;
- bioinformatics controls;
- evidence-based interpretation.

Dan yang paling penting:

> **Data yang besar tidak otomatis menghasilkan kesimpulan yang benar.**

Yang membedakan analisis kuat dan lemah adalah desain kontrol dan interpretasinya.

---

# Pertanyaan latihan

1. Mengapa scaffold N50 published Cai tidak cukup untuk menyimpulkan bahwa assembly-nya lebih contiguous daripada Guo?
2. Mengapa Cai fixed-on-Guo merupakan kontrol yang berguna?
3. Apa makna biologis dari mapping rate yang tinggi tetapi assembly span yang sangat berbeda?
4. Mengapa 54.117 structural-discrepancy calls tidak langsung disebut 54.117 true SV?
5. Mengapa complete BUSCO ~50% tidak boleh langsung diterjemahkan menjadi “setengah gen *Sapria* hilang”?

Jika kamu bisa menjelaskan kelimanya dengan jelas, kamu sudah masuk ke pola pikir comparative genomics yang sesungguhnya.

---

# Repository paths

- [`../00_phase0_published_baseline/`](../00_phase0_published_baseline/)
- [`../02_phase2_cai_mapping_to_guo/`](../02_phase2_cai_mapping_to_guo/)
- [`../03_phase3_harmonized_comparison/`](../03_phase3_harmonized_comparison/)
- [`../README.md`](../README.md)

Materi ini berdasarkan hasil sampai Phase 3. Phase 4 dan Phase 5 akan menambahkan cerita tentang repeat dan gene annotation.
