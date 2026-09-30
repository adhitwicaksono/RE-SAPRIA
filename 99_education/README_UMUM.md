# RE-SAPRIA untuk Pembaca Umum 🌺🧬
## Ketika satu tanaman menghasilkan beberapa “genom” yang sangat berbeda

Ada satu hal yang mudah disalahpahami tentang genom.

Kita sering membayangkan bahwa ilmuwan memasukkan DNA ke mesin, lalu mesin mengeluarkan genom lengkap seperti membuka sebuah file.

Kenyataannya, mesin sequencing biasanya menghasilkan **potongan-potongan DNA**.

Komputerlah yang harus menyusunnya kembali.

Dan pada organisme tertentu, pekerjaan itu bisa berubah menjadi mimpi buruk.

Salah satunya adalah ***Sapria himalayana***.

---

# Bunga aneh, genom yang sama anehnya

*Sapria* termasuk Rafflesiaceae, keluarga tumbuhan parasit yang terkenal karena cara hidupnya yang ekstrem.

Sebagian besar kehidupannya berlangsung tersembunyi di dalam jaringan inang.

Dalam RE-SAPRIA, kami mempelajari apa yang terjadi ketika biologi ekstrem bertemu dengan masalah rekonstruksi genom ekstrem.

Dua studi sebelumnya menerbitkan assembly *S. himalayana* dari dua accession berbeda.

Lalu kami menyusun ulang data Cai secara independen.

Hasilnya:

| Representasi genom | Panjang assembly |
|---|---:|
| **Guo published** | **2,061 Gb** |
| **Cai published** | **1,276 Gb** |
| **Cai Flye–HyPo** | **0,966 Gb** |

Satu spesies.

Tiga representasi.

Selisih terbesar sekitar **1,09 miliar pasangan basa**.

---

# Jadi… genom yang benar yang mana?

Itu justru pertanyaan yang salah.

Pertanyaan yang lebih baik adalah:

> **Bagian mana dari perbedaan itu benar-benar biologis, dan bagian mana yang muncul karena cara kita menyusun dan menganalisis genom?**

Genome assembly bukan organisme itu sendiri.

Ia adalah **model komputasi dari DNA yang berhasil direkonstruksi**.

Pada genom yang penuh sequence berulang, potongan-potongan DNA dapat memiliki banyak lokasi yang tampak sama.

Bayangkan mencoba menyusun puzzle langit biru berisi satu juta keping.

Banyak keping terlihat hampir identik.

---

# Kami menguji dengan kembali ke data mentah

Jika Guo benar-benar memiliki hampir satu miliar pasangan basa tambahan yang sama sekali tidak ada pada Cai, reads Cai seharusnya kesulitan mengenali Guo.

Tetapi:

- **92,68%** primary ONT reads Cai memetakan ke Guo;
- **97,87%** primary Illumina reads Cai memetakan ke Guo;
- short reads Cai mencakup sekitar **92,93%** breadth assembly Guo.

Jadi sebagian besar representasi Guo tetap dikenali oleh data Cai.

Perbedaan ukuran assembly tidak dapat dibaca secara sederhana sebagai perbedaan ukuran genom biologis.

---

# Dan ya, mereka memang berbeda

RE-SAPRIA juga mendeteksi lebih dari:

- **4,5 juta** high-confidence small sequence differences;
- **54 ribu** long-read structural discrepancies.

Tetapi kami sengaja berhati-hati dengan bahasa.

Hanya ada dua accession.

Sebagian structural discrepancy juga dapat berasal dari perbedaan assembly atau repeat.

Jadi kami tidak mengubah semua angka itu menjadi cerita evolusi sebelum ada bukti tambahan.

---

# Salah satu eksperimen favorit kami: “ubah hurufnya, jangan ubah bukunya”

Kami membuat genome representation bernama **Cai fixed-on-Guo**.

Bayangkan kita mengambil buku Guo, mempertahankan susunan halamannya, tetapi mengganti kata-kata tertentu dengan versi Cai yang didukung kuat oleh data.

Dengan demikian kita bisa bertanya:

> Apakah masalahnya terutama karena huruf DNA berbeda, atau karena keseluruhan genom disusun dengan cara berbeda?

Hasil RNA-seq:

| Genome | Mean alignment |
|---|---:|
| Guo | **96,92%** |
| Cai fixed-on-Guo | **96,79%** |
| Cai Flye–HyPo | **95,88%** |
| Cai published | **95,24%** |

Mengganti banyak alel Cai pada backbone Guo hanya memberi perubahan kecil.

Perbedaan lebih besar terlihat ketika struktur assembly juga berubah.

---

# Lalu datang BUSCO

BUSCO adalah salah satu cara untuk bertanya:

> “Berapa banyak gen konservatif yang biasanya ada pada tumbuhan masih dapat kita temukan?”

Yang menarik, assembly dengan panjang sangat berbeda memberi hasil yang cukup mirip.

Dengan Miniprot:

- Guo: **51,2% complete**
- Cai fixed-on-Guo: **51,4%**
- Cai published: **49,3%**
- Cai Flye–HyPo: **50,5%**

![BUSCO comparison](../03_phase3_harmonized_comparison/assembly_qc/busco/busco_miniprot_stacked_bar.png)

Jadi perbedaan assembly lebih dari satu miliar pasangan basa hanya menghasilkan perbedaan kecil dalam conserved gene recovery.

Itu tidak membuktikan bahwa semua DNA tambahan adalah repeat atau artefak.

Tetapi itu memberi petunjuk sangat kuat bahwa:

> **“lebih banyak DNA dalam assembly” tidak sama dengan “lebih banyak gene space biologis yang dapat dikenali.”**

---

# Bahkan N50 bisa menipu

Published Cai memiliki:

- scaffold N50 sekitar **952 kb**;
- tetapi contig N50 hanya sekitar **19 kb**;
- gap content sekitar **7,319%**.

Artinya scaffold terlihat panjang karena beberapa bagian dihubungkan melewati gap.

Reassembly Cai Flye–HyPo, sebaliknya:

- 10.435 contigs;
- N50 sekitar **1,056 Mb**;
- **0 Ns**.

Jadi dua angka N50 yang tampak mirip dapat menggambarkan assembly yang secara struktural sangat berbeda.

---

# Kenapa proyek ini menarik di luar *Sapria*?

Karena genomik modern semakin sering berhadapan dengan organisme yang:

- sangat repeat-rich;
- sangat heterozigot;
- memiliki genome architecture yang tidak biasa;
- sulit diwakili oleh satu assembly tunggal.

RE-SAPRIA mencoba satu prinsip sederhana:

> **Jangan hanya bertanya “assembly mana yang terbaik?”  
> Tanyakan “kesimpulan biologis mana yang tetap benar di berbagai representasi?”**

Itu jauh lebih berguna.

---

# Apa yang belum selesai?

Saat ini hasil sampai **Phase 3** sudah cukup stabil.

Berikutnya:

- **Phase 4:** repeat annotation;
- **Phase 5:** gene annotation dan sensitivity terhadap repeat masking;
- **Phase 6:** apa yang sebenarnya terdapat dalam gen-gen dan intron ekstrem tersebut.

Jadi folder pendidikan ini akan berubah seiring proyek berkembang.

Sains yang masih hidup memang begitu. 🙂

---

# Kalau hanya ingat satu kalimat

> **Satu organisme dapat memiliki beberapa representasi genom yang berbeda—dan tugas ilmuwan adalah menemukan bagian biologinya yang tetap bertahan ketika cara rekonstruksinya berubah.**

---

## Lihat data aslinya

- [`../README.md`](../README.md)
- [`../00_phase0_published_baseline/`](../00_phase0_published_baseline/)
- [`../02_phase2_cai_mapping_to_guo/`](../02_phase2_cai_mapping_to_guo/)
- [`../03_phase3_harmonized_comparison/`](../03_phase3_harmonized_comparison/)
