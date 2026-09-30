# RE-SAPRIA untuk SD 🌺🧬
## Bagaimana cara menyusun “buku DNA” yang sangat berantakan?

Bayangkan kamu menemukan sebuah buku raksasa.

Masalahnya: bukunya sudah **disobek menjadi jutaan potongan kecil**, beberapa kalimat muncul berulang-ulang, dan ada bagian yang hilang.

Tugasmu adalah menyusun buku itu kembali.

Itulah salah satu pekerjaan ahli genomik.

Bedanya, “bukunya” adalah **DNA**.

Dan tumbuhan yang sedang kami pelajari bernama ***Sapria himalayana***.

---

## 🌺 Siapa *Sapria*?

*Sapria himalayana* adalah tumbuhan parasit dari keluarga Rafflesiaceae.

Tumbuhan ini sangat bergantung pada tumbuhan inangnya. Sebagian besar kehidupannya berlangsung tersembunyi di dalam jaringan inang.

Karena cara hidupnya sangat tidak biasa, genomnya juga menarik untuk dipelajari.

---

## 🧩 Kejutan pertama: satu spesies, ukuran “buku DNA” yang berbeda-beda

Ilmuwan pernah menyusun genom *Sapria* dari dua sampel yang berbeda.

Kemudian kami juga menyusun ulang salah satunya.

Hasilnya:

| Versi genom | Panjang hasil penyusunan |
|---|---:|
| Guo published | **2,061 miliar huruf DNA** |
| Cai published | **1,276 miliar huruf DNA** |
| Cai Flye–HyPo | **0,966 miliar huruf DNA** |

Itu aneh.

Versi terbesar dan terkecil berbeda lebih dari **1 miliar huruf DNA**!

Apakah berarti satu tumbuhan punya genom dua kali lebih besar?

**Belum tentu.**

Mungkin sebagian perbedaannya terjadi karena cara komputer menyusun potongan DNA.

---

## 🔍 Bagaimana kami memeriksanya?

Kami kembali ke potongan-potongan DNA asli dari Cai.

Lalu kami bertanya:

> “Apakah potongan DNA Cai masih bisa menemukan tempat yang cocok di genom Guo?”

Ternyata, iya.

- Sekitar **92,68%** long reads Cai dapat dipetakan ke Guo.
- Sekitar **97,87%** short reads Cai dapat dipetakan ke Guo.

Jadi walaupun ukuran dua hasil penyusunan itu sangat berbeda, banyak potongan DNA Cai masih mengenali genom Guo.

Itulah misterinya. 🤯

---

## 📚 Analogi buku yang lebih seru

Bayangkan dua kelompok menyusun buku yang sama.

Kelompok A menghasilkan buku **1.000 halaman**.

Kelompok B menghasilkan buku **2.000 halaman**.

Kamu mungkin berpikir:

> “Wah, pasti bukunya berbeda!”

Tapi ketika kamu memeriksa kalimat-kalimatnya, ternyata banyak sekali yang sama.

Lalu kamu menemukan bahwa buku itu penuh dengan:

- kalimat yang berulang;
- potongan yang sulit ditempatkan;
- bagian kosong;
- paragraf yang mirip satu sama lain.

Sekarang masalahnya berubah.

Bukan hanya:

> “Buku mana yang benar?”

Tetapi:

> **“Bagian mana yang benar-benar berbeda, dan bagian mana yang berbeda karena cara kita menyusunnya?”**

Itulah RE-SAPRIA.

---

## 🧬 Apa itu gen?

Gen adalah bagian DNA yang membawa informasi untuk membantu sel membuat sesuatu, misalnya protein.

Tetapi genom tidak hanya berisi gen.

Ada juga banyak bagian lain.

Sebagian DNA bahkan dapat berulang berkali-kali.

Bayangkan kalimat:

> BUNGA BUNGA BUNGA BUNGA BUNGA BUNGA...

Kalau komputer melihat ribuan bagian yang hampir sama, menyusunnya kembali menjadi jauh lebih sulit.

---

## 🕵️‍♀️ Ilmuwan harus menjadi detektif

Dalam RE-SAPRIA, kami tidak langsung percaya satu hasil komputer.

Kami membandingkan:

- DNA asli;
- beberapa hasil penyusunan genom;
- gen-gen yang dapat dikenali;
- RNA yang menunjukkan bagian genom yang sedang digunakan.

Setiap jenis data menjadi **petunjuk**.

Semakin banyak petunjuk yang cocok, semakin yakin kita bahwa suatu kesimpulan benar.

---

## ⭐ Hal yang paling keren

Genom *Sapria* mengajarkan satu pelajaran penting:

> **Melihat angka besar belum tentu berarti kita sudah memahami biologinya.**

Kadang-kadang tugas ilmuwan justru dimulai ketika dua jawaban terlihat tidak cocok.

---

## 🤔 Coba pikirkan

1. Kalau dua puzzle dibuat dari gambar yang sama tetapi jumlah kepingnya berbeda, apakah gambarnya pasti berbeda?
2. Mengapa bagian DNA yang berulang akan menyulitkan komputer?
3. Mengapa ilmuwan sebaiknya memakai lebih dari satu jenis bukti?

Kalau kamu sudah mulai bertanya seperti itu, selamat:

**kamu sudah berpikir seperti seorang bioinformatikawan.** 🧬💻

---

## Dari mana angka-angka ini berasal?

Data teknis lengkap ada di repository RE-SAPRIA:

- [`../00_phase0_published_baseline/`](../00_phase0_published_baseline/)
- [`../02_phase2_cai_mapping_to_guo/`](../02_phase2_cai_mapping_to_guo/)
- [`../03_phase3_harmonized_comparison/`](../03_phase3_harmonized_comparison/)

> Catatan: panjang assembly di atas adalah panjang hasil rekonstruksi DNA oleh komputer, bukan otomatis ukuran genom biologis sebenarnya.
