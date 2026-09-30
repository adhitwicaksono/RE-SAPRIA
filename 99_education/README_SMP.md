# RE-SAPRIA untuk SMP 🌺🧬
## Satu spesies, beberapa assembly: bagaimana mungkin?


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

## 1. Teka-teki assembly

| Representasi | Assembly span |
|---|---:|
| **Guo published** | **2,061 Gb** |
| **Cai published** | **1,276 Gb** |
| **Cai Flye–HyPo** | **0,966 Gb** |

Semua mewakili *Sapria himalayana*.

Pertanyaannya:

> **Apakah perbedaan itu berasal dari tumbuhannya, atau dari cara genom direkonstruksi?**

## 2. Kenapa assembly bisa berbeda?

Genome assembly seperti puzzle raksasa. Repeat membuat banyak keping terlihat sama.

Komputer dapat:

- menyatukan daerah yang sebenarnya berbeda;
- memisahkan daerah yang seharusnya tersambung;
- meninggalkan gap;
- membangun scaffold panjang dari contig yang pendek.

Published Cai adalah contoh bagus:

- scaffold N50 ≈ **952 kb**
- contig N50 ≈ **19 kb**
- gap content ≈ **7,319%**

Jadi scaffold N50 yang besar belum tentu berarti sequence tanpa gap juga panjang.

## 3. Kembali ke reads asli

### Cai ONT → Guo
- primary mapping: **92,68%**
- breadth Guo: **88,11%**

### Cai Illumina → Guo
- primary mapping: **97,87%**
- breadth Guo: **~92,93%**

Sebagian besar Guo masih dikenali oleh data Cai.

## 4. Tetapi Cai dan Guo tidak identik

Kami menemukan:

- **4.535.955** high-confidence small variants;
- **3.704.632** SNP;
- **831.323** indel;
- **54.117** structural-discrepancy calls.

Ada perbedaan nyata, tetapi hanya ada dua accession. Kita tidak boleh menganggap angka ini mewakili variasi seluruh spesies.

## 5. Kontrol Cai fixed-on-Guo

Kami mempertahankan struktur Guo tetapi memasukkan alel Cai yang sangat yakin.

Hasil RNA-seq:

| Genome | Mean alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |

Guo dan Cai fixed-on-Guo hampir sama.

Ini membantu memisahkan efek **perbedaan basa DNA** dari efek **reconstruction**.

## 6. BUSCO

Dengan Miniprot:

- Guo: **51,2%**
- Cai fixed-on-Guo: **51,4%**
- Cai published: **49,3%**
- Cai Flye–HyPo: **50,5%**

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Assembly span berubah lebih dari dua kali lipat, tetapi conserved gene recovery berubah sedikit.

## 7. Tantangan OGI-style 🧠

1. Mengapa N50 tidak boleh dibaca sendirian?
2. Mengapa mapping rate tinggi penting?
3. Mengapa 54.117 structural discrepancies tidak otomatis berarti 54.117 true SV?
4. Mengapa assembly dua kali lebih besar tidak otomatis berarti dua kali lebih banyak gen?

> **Bioinformatika bukan sekadar menjalankan software. Bioinformatika adalah menguji apakah suatu kesimpulan tetap benar ketika cara melihat data berubah.**


## Sumber utama

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria
