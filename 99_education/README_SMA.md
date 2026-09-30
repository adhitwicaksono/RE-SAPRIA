# RE-SAPRIA untuk SMA 🌺🧬
## Genome assembly bukan genom itu sendiri


## Sebelum mulai: *Sapria* itu siapa? Dan siapa “Cai” dan “Guo”? 🌺

Kalau kamu mengenal **Rafflesia**, kamu sudah punya pintu masuk yang bagus.

*Rafflesia* dan *Sapria* bukan tumbuhan yang sama, tetapi keduanya berada dalam keluarga **Rafflesiaceae**—kelompok tumbuhan parasit yang terkenal karena tubuh vegetatifnya sangat tereduksi dan sebagian besar hidup tersembunyi di dalam jaringan inang.

*Rafflesia* jauh lebih terkenal karena bunganya yang raksasa. *Sapria himalayana* adalah kerabatnya yang lebih jarang terdengar, tetapi justru menjadi salah satu anggota Rafflesiaceae yang genomnya berhasil dipelajari secara mendalam.

Dan satu hal penting:

> **“Cai” dan “Guo” bukan nama spesies.**

Dalam folder RE-SAPRIA, **Cai** adalah singkatan praktis untuk dataset/assembly dari studi **Liming Cai dan kolega (2021)**. **Guo** adalah singkatan untuk dataset/assembly dari studi **Xuelian Guo dan kolega (2023)**.

Jadi kita sedang membandingkan **dua penelitian berbeda tentang spesies yang sama: *Sapria himalayana*.**

## Dua ekspedisi ilmiah ke genom *Sapria*

### Perjalanan Cai: dari tanaman hampir “tak terlihat” menuju genom

Tim Charles C. Davis di Harvard telah lama mempelajari Rafflesiaceae. Salah satu tantangan besarnya sederhana untuk diucapkan tetapi sulit dilakukan: **bagaimana mendapatkan genom yang dapat digunakan dari tumbuhan yang hidupnya sendiri tersembunyi di dalam inang?**

Liming Cai menjadikan *Sapria himalayana* sebagai bagian penting dari penelitian doktoralnya. Bersama Charles Davis, Timothy Sackton, tim bioinformatika Harvard, dan kolaborator dari Asia Tenggara, studi 2021 mereka menghasilkan salah satu gambaran genomik paling lengkap untuk garis keturunan Rafflesiaceae saat itu.

Mereka menemukan sesuatu yang luar biasa: *Sapria* telah kehilangan banyak gen tumbuhan yang biasanya sangat konservatif, namun genomnya tetap besar dan mempunyai arsitektur yang sangat tidak biasa. Mereka juga menemukan bukti horizontal gene transfer dari garis keturunan inang.

### Perjalanan Guo: kembali ke spesies yang sama dengan dataset baru

Dua tahun kemudian, **Xuelian Guo** dan tim dari Chinese Academy of Sciences, Novogene, dan kolaborator lain menerbitkan **assembly independen lain dari *S. himalayana***.

Studi Guo tidak sekadar mengulang Cai. Mereka menggunakan dataset lain dan menyoroti pertanyaan seperti perkembangan bunga, waktu berbunga, metabolisme, pertahanan, kehilangan gen, dan horizontal gene transfer.

Dan di sinilah RE-SAPRIA lahir sebagai pertanyaan baru:

> **Kalau dua tim mempelajari spesies yang sama tetapi menghasilkan representasi genom yang sangat berbeda, bagian mana yang merupakan biologi—dan bagian mana yang berasal dari cara genom direkonstruksi?**

## 1. Pertanyaan ilmiah RE-SAPRIA

Dua studi genom independen pada *Sapria himalayana* menghasilkan representasi yang sangat berbeda.

| Genome representation | Assembly span |
|---|---:|
| **Guo published** | **2.061 Gb** |
| **Cai published** | **1.276 Gb** |
| **Cai Flye–HyPo** | **0.966 Gb** |

Perbedaan terbesar ≈ **1,09 Gb**.

Pertanyaan yang diuji:

> **Seberapa banyak perbedaan Cai–Guo yang merupakan biological divergence, dan seberapa banyak yang reconstruction-dependent?**

## 2. Assembly metrics tidak berdiri sendiri

Published Cai:

- 128.027 scaffold records;
- 216.625 gap-free contigs menurut statistik BUSCO;
- scaffold N50 ≈ **952 kb**;
- contig N50 ≈ **19 kb**;
- gap content ≈ **7,319%**.

Published Guo:

- 18.718 scaffolds;
- 26.955 contigs;
- scaffold N50 ≈ **251 kb**;
- contig N50 ≈ **106 kb**;
- gap content ≈ **1,865%**.

Jadi Cai mempunyai scaffold N50 lebih besar tetapi gap-free contiguity lebih rendah.

## 3. Read-backed evidence

### ONT
- primary mapping: **92,68%**
- Guo breadth: **88,11%**
- mean depth: **~14,4×**

### Illumina
- primary mapping: **97,87%**
- Guo breadth: **~92,93%**
- mean depth: **~41,94×**

Perbedaan assembly span tidak dapat langsung diterjemahkan menjadi perbedaan biological genome size.

## 4. Variant evidence

| Variant | Count |
|---|---:|
| Total high-confidence small variants | **4.535.955** |
| SNP | **3.704.632** |
| Indel | **831.323** |
| Homozygous-alternate | **1.158.638** |

ONT juga menghasilkan **54.117 PASS structural-discrepancy calls**.

Istilah *discrepancy* dipakai karena sinyal dapat mencampur true variation, repeat ambiguity, assembly differences, dan alignment behavior.

## 5. Cai fixed-on-Guo sebagai eksperimen kontrol

Backbone Guo dipertahankan, confident Cai homozygous-alternate alleles dimasukkan.

Ini memungkinkan kita mengubah **sequence state** sambil mempertahankan **large-scale structure** relatif tetap.

| Representation | Mean HISAT2 alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |
| Cai min1250 | **95,15%** |

Perubahan Guo → Cai-fixed kecil; perubahan menuju independent Cai assemblies lebih besar.

## 6. BUSCO: span ≠ conserved gene space

| Representation | AUGUSTUS Complete | Miniprot Complete |
|---|---:|---:|
| Guo | **49,7%** | **51,2%** |
| Cai fixed-on-Guo | **49,8%** | **51,4%** |
| Cai published | **47,5%** | **49,3%** |
| Cai Flye–HyPo | **47,3%** | **50,5%** |

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Assembly span berubah >2×, complete BUSCO hanya beberapa persen.

Jangan overclaim: missing BUSCO dapat mencerminkan true loss, divergence, fragmentation, giant gene architecture, atau keterbatasan predictor.

## 7. min1250 sebagai technical control

Published Cai: **128.027 records**.

Setelah membuang scaffold <1.250 bp:

- **99.251 records**
- **97,49%** sequence retained
- AUGUSTUS complete BUSCO: tidak berubah
- Miniprot complete BUSCO: **795 → 794**
- RNA-seq mapping: **95,24% → 95,15%**

Ini adalah technical rescue, bukan bukti assembly menjadi “lebih baik”.

> **Pertanyaan utama comparative genomics bukan hanya “apa hasilnya?” tetapi “apakah hasil itu tetap bertahan ketika representasi dan metode berubah?”**


## Sumber utama

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria
