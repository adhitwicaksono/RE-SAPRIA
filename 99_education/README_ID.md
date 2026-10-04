# 99_education — RE-SAPRIA untuk Semua 🌺🧬

Folder ini adalah pintu masuk pendidikan untuk proyek RE-SAPRIA.

Tujuannya: **membuat genomik ekstrem *Sapria himalayana* terasa menakjubkan tanpa mengorbankan ketepatan ilmiah.**


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

## Pilih tingkatmu

| Pembaca | File |
|---|---|
| **SD** | [`README_SD.md`](README_SD.md) |
| **SMP** | [`README_SMP.md`](README_SMP.md) |
| **SMA** | [`README_SMA.md`](README_SMA.md) |
| **Pembaca umum** | [`README_UMUM.md`](README_UMUM.md) |
| **English index** | [`README.md`](README.md) |

## Status materi

Set materi pendidikan ini telah diperbarui mengikuti **sintesis analitik
RE-SAPRIA yang dibekukan sampai Phase 7 (2026-10-04)**.

Proyek ini bermula dari perbedaan besar antara assembly Cai dan Guo, tetapi
fokus biologis akhirnya lebih luas: **arsitektur genom *Sapria himalayana*
yang tetap muncul ketika genom direpresentasikan dengan beberapa cara berbeda.**

## Apa yang akhirnya ditemukan RE-SAPRIA?

Pada representasi genom utama, sekitar **84–90% sequence non-N terdeteksi
sebagai repeat**. Sekitar **94–98% perbedaan besar dalam panjang genom yang
direpresentasikan berkaitan dengan sequence yang kaya repeat**.

Repeat juga masuk jauh ke dalam daerah gen. Hanya sekitar **9–11% intron
representatif yang panjangnya ≥10 kb**, tetapi intron-intron panjang tersebut
menampung sekitar **67–72% seluruh sequence intronik**. Sequence intron jauh
lebih banyak bertumpang tindih dengan repeat dibandingkan CDS.

Karena itu, gene prediction sangat sensitif terhadap cara repeat diperlakukan.
Soft-masking didukung sebagai pendekatan utama untuk structural gene annotation
*S. himalayana*, sementara annotation pada genom unmasked lebih cocok sebagai
kontrol sensitivitas.

Walaupun panjang assembly dan jumlah gen prediksi berubah besar, recovery
protein-coding genes yang konservatif relatif stabil antar-representasi.

## Satu kalimat inti

> **Pada *Sapria himalayana*, DNA kaya repeat membuat rekonstruksi genom dan prediksi gen sangat sensitif terhadap metode, tetapi inti protein-coding yang konservatif tetap relatif stabil.**


## Sumber utama

- Cai L, Arnold BJ, Xi Z, et al. (2021). *Deeply Altered Genome Architecture in the Endoparasitic Flowering Plant Sapria himalayana Griff. (Rafflesiaceae).* **Current Biology** 31:1002–1011.e9.  
  https://doi.org/10.1016/j.cub.2020.12.045
- Guo X, Hu X, Li J, et al. (2023). *The Sapria himalayana genome provides new insights into the lifestyle of endoparasitic plants.* **BMC Biology** 21:134.  
  https://doi.org/10.1186/s12915-023-01620-3
- Harvard Plant Biology Initiative (2021). *Genetic sequence for parasitic flowering plant Sapria.*  
  https://pbi.oeb.harvard.edu/news/genetic-sequence-parasitic-flowering-plant-sapria

## Sintesis proyek RE-SAPRIA

- [Phase 7 — sintesis analitikal akhir](../07_phase7_manuscript_outputs/README.md)
- Arsip anotasi *repeat* fase 4: https://doi.org/10.5281/zenodo.23105473
- Arsip anotasi terstandar fase 5A: https://doi.org/10.5281/zenodo.23072450
