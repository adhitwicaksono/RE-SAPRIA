# RE-SAPRIA untuk Pembaca Umum 🌺🧬
## Dari Rafflesia yang terkenal ke kerabatnya yang lebih misterius


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

Banyak orang mengenal Rafflesia dari bunganya yang raksasa. Tetapi keluarga Rafflesiaceae menyimpan cerita lain yang tidak kalah aneh: **apa yang terjadi pada genom tumbuhan ketika hampir seluruh hidupnya bergantung pada inang?**

*Sapria himalayana* memberi kita kesempatan untuk melihatnya.

## Tiga representasi genom, satu spesies

| Representasi | Assembly span |
|---|---:|
| **Guo published** | **2,061 Gb** |
| **Cai published** | **1,276 Gb** |
| **Cai Flye–HyPo** | **0,966 Gb** |

Perbedaan terbesar sekitar **1,09 miliar pasangan basa**.

Apakah itu berarti salah satu *Sapria* benar-benar mempunyai genom dua kali lebih besar?

Belum tentu.

Genome assembly adalah **rekonstruksi komputasional**, bukan organisme itu sendiri.

## Kembali ke reads mentah

- **92,68%** primary ONT reads Cai memetakan ke Guo.
- **97,87%** primary Illumina reads Cai memetakan ke Guo.
- Illumina Cai mencakup sekitar **92,93%** breadth Guo.

Jadi sebagian besar Guo tetap dikenali oleh data Cai.

## Tetapi mereka memang berbeda

Kami juga menemukan lebih dari:

- **4,5 juta** high-confidence small differences;
- **54 ribu** long-read structural discrepancies.

Jadi ceritanya bukan “semua hanya artefak”, tetapi juga bukan “semua adalah perbedaan biologis”.

## “Ubah hurufnya, jangan ubah bukunya”

Cai fixed-on-Guo mempertahankan struktur Guo tetapi mengganti banyak posisi dengan alel Cai yang didukung kuat.

RNA-seq mapping:

| Genome | Mean alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |

Mengubah banyak alel tidak memberi perubahan sebesar mengganti keseluruhan reconstruction.

## BUSCO menambah twist

Dengan Miniprot:

- Guo: **51,2% complete**
- Cai fixed-on-Guo: **51,4%**
- Cai published: **49,3%**
- Cai Flye–HyPo: **50,5%**

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Lebih dari satu miliar pasangan basa perbedaan assembly hanya menghasilkan perubahan kecil dalam conserved gene recovery.

## Jadi apa yang sebenarnya sedang dicari?

Bukan “assembly mana yang menang”.

Tetapi:

> **Kesimpulan biologis mana yang tetap benar meskipun representasi genom berubah?**

Itulah inti RE-SAPRIA.

Phase 4 dan Phase 5 akan menambahkan bagian yang mungkin paling liar: repeat dan gene annotation.


## Sumber utama

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria
