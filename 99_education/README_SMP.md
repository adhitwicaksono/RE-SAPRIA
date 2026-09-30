# RE-SAPRIA untuk SMP 🌺🧬
## Ketika satu spesies memiliki tiga “versi genom” yang sangat berbeda

Kalau kamu mempelajari genom, kamu mungkin membayangkan bahwa satu organisme mempunyai satu urutan DNA yang bisa langsung dibaca.

Kenyataannya tidak sesederhana itu.

Mesin sequencing membaca DNA sebagai banyak potongan. Komputer kemudian harus menyusun potongan-potongan itu menjadi **genome assembly**.

Dan pada *Sapria himalayana*, proses ini menjadi sangat ekstrem.

---

## 1. Teka-teki utamanya

Dalam RE-SAPRIA, kami membandingkan beberapa representasi genom *Sapria*.

| Representasi | Panjang assembly |
|---|---:|
| **Guo published** | **2,061 Gb** |
| **Cai published** | **1,276 Gb** |
| **Cai Flye–HyPo** | **0,966 Gb** |

Versi terbesar lebih dari dua kali versi terkecil.

Padahal semuanya berasal dari **spesies yang sama**.

Pertanyaannya:

> **Apakah perbedaan itu benar-benar berasal dari biologi tumbuhannya, atau sebagian berasal dari cara genom disusun?**

---

## 2. Kenapa assembly bisa berbeda?

Bayangkan genom sebagai puzzle raksasa.

Kalau semua keping unik, penyusunan relatif mudah.

Tetapi kalau banyak keping memiliki gambar yang hampir sama, komputer bisa:

- menyatukan beberapa daerah yang sebenarnya terpisah;
- menghitung daerah berulang lebih dari sekali;
- gagal menghubungkan dua bagian;
- meninggalkan gap;
- membuat scaffold yang panjang tetapi sebenarnya tersusun dari contig yang lebih pendek.

Pada published Cai, misalnya:

- scaffold N50 ≈ **952 kb**
- tetapi contig N50 hanya ≈ **19 kb**
- gap content ≈ **7,319%**

Artinya, scaffold-nya tampak panjang, tetapi banyak kontinuitasnya berasal dari penghubung yang mengandung `N`.

---

## 3. Kami kembali ke reads asli

Kalau Guo benar-benar memiliki hampir 1 Gb DNA tambahan yang sama sekali tidak ada pada Cai, reads Cai seharusnya sulit mengenali sebagian besar Guo.

Tetapi hasilnya:

### Cai ONT → Guo

- primary mapping: **92,68%**
- breadth Guo yang tertutup: **88,11%**

### Cai Illumina → Guo

- primary mapping: **97,87%**
- breadth Guo yang tertutup: **~92,93%**

Jadi sebagian besar representasi Guo masih dikenali oleh data Cai.

Ini membuat cerita “Guo hanya mempunyai genom jauh lebih besar” menjadi terlalu sederhana.

---

## 4. Tetapi Cai dan Guo memang tidak identik

Kami menemukan:

- **4.535.955** small variants berkualitas tinggi;
- **3.704.632** SNP;
- **831.323** indel;
- **54.117** structural-discrepancy calls dari long reads.

Jadi ada perbedaan nyata.

Tetapi hanya ada **dua accession**, sehingga kita tidak boleh menyebut angka tersebut sebagai variasi seluruh spesies.

---

## 5. Bagaimana cara memisahkan “beda DNA” dari “beda assembly”?

Kami membuat sebuah kontrol bernama **Cai fixed-on-Guo**.

Idenya:

- pertahankan struktur scaffold Guo;
- ganti posisi tertentu dengan alel Cai yang sangat yakin;
- lalu lihat apa yang berubah.

Ini seperti mengambil satu buku dengan susunan halaman tetap, kemudian mengganti beberapa kata agar mengikuti versi buku lain.

Hasilnya menarik.

RNA-seq Guo memetakan ke:

| Genome | Mean alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |

Guo dan Cai fixed-on-Guo hampir sama.

Ini mendukung gagasan bahwa **perubahan struktur/reconstruction dapat memberi pengaruh lebih besar daripada sekadar mengganti basa tertentu**.

---

## 6. BUSCO: mencari gen yang biasanya dimiliki tumbuhan

BUSCO mencari kelompok gen konservatif yang diharapkan ditemukan pada banyak tumbuhan.

Yang mengejutkan:

walaupun assembly kita berkisar dari sekitar **0,966 sampai 2,061 Gb**, complete BUSCO tetap hanya berubah sedikit.

Dengan Miniprot:

- Guo: **51,2%**
- Cai fixed-on-Guo: **51,4%**
- Cai published: **49,3%**
- Cai Flye–HyPo: **50,5%**

Jadi assembly dua kali lebih panjang **tidak otomatis** berarti dua kali lebih banyak gene space yang dapat dikenali.

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

---

## 7. Kenapa ini penting?

Karena bioinformatika bukan hanya “menekan tombol software”.

Kita harus bertanya:

- Apakah data mendukung hasil assembly?
- Apakah angka besar berarti sesuatu yang biologis?
- Apakah repeat membingungkan assembler?
- Apakah satu software memberi jawaban berbeda dari software lain?
- Apakah kesimpulan tetap sama jika representasi genom diubah?

Itulah cara kerja sains komputasi.

---

## 8. Tantangan OGI-style 🧠

### Pertanyaan 1

Satu assembly memiliki N50 lebih tinggi, tetapi juga memiliki banyak gap.

Apakah kita boleh langsung menyimpulkan assembly itu lebih baik?

**Tidak.** N50 harus dibaca bersama contig continuity, gap content, read support, dan metrik lain.

### Pertanyaan 2

Mengapa mapping rate tinggi dari Cai ke Guo penting?

Karena itu menunjukkan bahwa banyak sequence Guo masih memiliki pasangan yang dapat dikenali dalam reads Cai.

### Pertanyaan 3

Jika complete BUSCO hampir sama pada assembly 0,966 Gb dan 2,061 Gb, apa yang dapat kita simpulkan?

Bahwa perbedaan assembly span yang besar **tidak diikuti oleh perbedaan sebesar itu pada conserved gene space**.

Kita masih belum boleh menyimpulkan semua sequence tambahan adalah repeat atau artefak; itu perlu diuji.

---

## Pesan utama

> **Genom bukan sekadar urutan DNA. Genom yang kita analisis adalah hasil pengukuran, rekonstruksi, dan interpretasi.**

Pada organisme ekstrem seperti *Sapria*, memahami proses itu sama pentingnya dengan memahami gen itu sendiri.

---

## Sumber data dalam repository

- [`../00_phase0_published_baseline/`](../00_phase0_published_baseline/)
- [`../02_phase2_cai_mapping_to_guo/`](../02_phase2_cai_mapping_to_guo/)
- [`../03_phase3_harmonized_comparison/`](../03_phase3_harmonized_comparison/)

Materi ini memakai hasil sampai Phase 3 dan akan diperbarui setelah analisis repeat dan anotasi selesai.
