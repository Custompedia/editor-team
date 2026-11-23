# Pertanyaan untuk pemilik, risiko, dan uji lintas model

## 1. Keputusan yang harus diambil pemilik

| # | Pertanyaan | Kenapa penting | Usul default |
|---|---|---|---|
| 1 | Permintaan khusus job01 (pertanyaan pelanggan sebagai gelembung kiri/kanan, beat gelap di "nggak bisa", penutup Pinterest layar penuh): berlaku untuk **semua** video, hanya untuk **Parcelin**, atau hanya job01? | Permintaan ini benar-benar dari user, bukan dari editor referensi. Kalau dihapus, keinginan user hilang; kalau umum, semua video mirip Parcelin | Profil brand `docs/brands/parcelin.md`, dibaca hanya untuk job Parcelin |
| 2 | Tampilan aplikasi berlogin (IG, WA) saat user tidak mengirim rekaman: boleh **dibangun ulang** dengan kode asal sama persis dengan screenshot asli, atau **tidak pernah**? | Pemilik berkata "show the real Instagram". Bangun ulang yang rapi kadang sulit dibedakan; yang jelek langsung terlihat palsu dan merusak kepercayaan | Tidak pernah membangun ulang UI. Kode hanya menggerakkan screenshot asli dari user (kursor, ketik di kolomnya) |
| 3 | Image generation untuk foto konsep (mis. "makro foil emas") boleh? Lewat siapa (user membuat di aplikasi lain)? | Studi referensi menduga sebagian foto konsep editor referensi adalah gambar generatif atau stok premium. Tanpa itu, beberapa konsep tidak punya foto nyata yang bersih dari container ini | Boleh untuk benda/tekstur tanpa foto nyata, tidak untuk orang, logo, UI, bukti; prompt dikumpulkan di `work/gen_prompts.md` dan diminta sekali di Tahap 0/6 |
| 4 | Lisensi Openverse: lisensi BY (butuh atribusi) boleh di video brand? Atribusi ditulis di mana (caption postingan)? NC dilarang? | Openverse adalah satu-satunya bank foto yang terjangkau dari sini | BY boleh, atribusi di laporan untuk caption; NC dan ND tidak dipakai di video brand |
| 5 | Apakah pemilik mau **meminta aset di awal setiap job** (rekaman layar, foto produk, logo) sebagai kebiasaan? | Bagian 4 bergantung pada ini. Tanpa aset user, CTA dan aksi aplikasi akan selalu jatuh ke cadangan | Lead menanyakan daftar standar di awal (sudah ada di CLAUDE.md repo "What to ask the user for"); tambahkan "rekaman layar 10 dtk untuk aksi aplikasi yang disebut" |
| 6 | Perlukah tetap ada **alarm angka** (mis. "kalau layar penuh di bawah 15% di video jualan, lead menolak")? | Bukti job01: 15% dengan rentang wajah 16 dtk dinilai kurang. Tanpa alarm, model lemah bisa kembali sepi | Tidak ada angka minimum di skill; lead memakai angka kalibrasi saat review, dan worker wajib menjelaskan selisih besar |
| 7 | Komponen generik mana yang dibangun di kit sekarang (`grade`, callout/label di aset, coret, split berisi daftar, `invsplit`, galeri)? | Dengan komponen generik, worker menggerakkan aset nyata alih-alih menggambar. Tanpanya, tiap job menulis kode sendiri (spam kode per job) | Bangun `grade`, callout, coret, `invsplit`, galeri dulu (lihat skill-changes E) |
| 8 | Look bawaan kit: tetap ada nilai netral, atau worker **wajib** memilih (tanpa bawaan)? | Tanpa bawaan, model lemah bisa memilih palet acak. Dengan bawaan, model malas tidak memutuskan apa pun | Tetap ada bawaan netral, tetapi gate Tahap 0 meminta keputusan + alasan tertulis (memilih bawaan pun harus beralasan) |
| 9 | Ganti nama `design.md` → `roll-types.md`? | Isi tinggal struktur cerita; nama lama mengundang model mencari "standar desain" di sana | Ganti, bersamaan dengan rujukan di SKILL/README/CLAUDE |
| 10 | `/home/user/CLAUDE.md` (di luar repo, basi, dimuat ke worker) dihapus atau disamakan dengan repo? | Ia memuat template lama sebagai instruksi yang "mengalahkan" skill | Disamakan dengan `CLAUDE.md` repo (atau dihapus) sebelum job berikutnya |

---

## 2. Risiko rewrite ini

| Risiko | Paling terasa pada | Mitigasi di draf |
|---|---|---|
| **Kembali sepi.** Tanpa angka target, model memilih "tetap di pembicara" lebih sering (persis kegagalan job01) | Model lebih lemah, dan model yang hati-hati | Pertanyaan 2 menolak "tetap di pembicara" sebagai tempat berlindung; lintasan 2.2 memeriksa rentang wajah panjang; kalibrasi wajib dibandingkan; uji diri 9 |
| **Terlalu ramai.** "Kalimat konkret harus divisualkan" dibaca sebagai "setiap kata benda dapat gambar" | Model yang patuh literal | Pertanyaan 2 (apakah pemahaman bertambah), pertanyaan 6 (hapus kalau tidak ada yang hilang), uji diri 10 |
| **Pertanyaan dijawab "ya" tanpa dikerjakan.** Uji diri berbentuk pertanyaan lebih mudah dicentang palsu daripada aturan berangka | Semua model, terutama di konteks panjang | Jawaban wajib dengan bukti (nomor baris, nomor frame); lead memeriksa 2–3 jawaban secara acak di still |
| **Kehilangan selera yang sudah diketahui.** Gelembung, beat gelap, penutup layar penuh disukai user; sebagai "salah satu jawaban" mungkin jarang dipilih | Semua model | Contoh 9.2/9.3 tetap menyebutnya; profil brand menyimpan permintaan eksplisit; keputusan pemilik #1 |
| **Tabel situasi dibaca sebagai tabel aturan baru.** Kolom "Biasanya paling jelas" bisa disalin seperti tabel 6.1 lama | Model lebih lemah | Kalimat pembuka Bagian 3 ("titik awal penalaran"), kolom "yang dipikirkan" dan "ditolak, kenapa"; uji lintas model memakai transkrip non-Parcelin untuk mendeteksi penyalinan |
| **Penurunan mutu gambar demi "nyata".** Worker memilih foto Openverse buram daripada diagram bersih | Semua model | "Nyata DAN memperlihatkan konsep"; uji diri 4 (terbaca dalam satu detik); kebijakan kode mengizinkan diagram bila tidak ada gambar yang bagus |
| **Job macet menunggu aset user** | Lead dan user | Satu daftar permintaan di Tahap 0; lanjut dengan cadangan `ASUMSI` (sesuai LESSONS: user ingin hasil sekali jalan) |
| **Biaya token naik.** `visual_plan.md` per kalimat dengan 8 kolom lebih panjang | Semua job | Baris "tetap di pembicara" cukup 3 kolom; file panduan lebih pendek dari style-notes + design + 6.1 digabung |
| **Masa transisi tidak konsisten.** Brief template, CLAUDE.md (dua versi), LESSONS masih merujuk style-notes | Worker job berikutnya | Daftar lengkap rujukan di skill-changes I; terapkan sekaligus dalam satu commit |
| **Bukti hanya dari satu editor sampai benchmark masuk.** Beberapa "dibuang" mungkin sebenarnya prinsip umum | Mutu panduan | Slot `<!-- BENCHMARK -->`; tinjau ulang tabel D setelah catatan editor kedua |

---

## 3. Uji lintas model yang murah (rencana saja, tanpa render)

**Tujuan:** memastikan panduan baru dipahami sebagai cara berpikir oleh Opus, Sonnet, dan Haiku, dan lebih baik dari panduan
lama, sebelum dipakai di job nyata.

**Bahan (tanpa video, tanpa render):**
- Transkrip A: job01 Parcelin (`work/script.md` + `footage.md` + bagian brief tanpa keputusan visual). Ada jawaban
  pembanding: tabel per kalimat referensi vs v4 di case study.
- Transkrip B: konten **berbeda jenis** tanpa brand Parcelin, idealnya salah satu transkrip benchmark editor kedua
  (<!-- BENCHMARK: pilih transkrip yang paling berbeda dari Parcelin, mis. berita/opini/tutorial aplikasi -->), atau transkrip
  sintetis pendek (±60 dtk) yang menyebut berita, aksi DM Instagram, angka, dan opini.
- Tabel kemampuan container (Bagian 4) sebagai fakta.

**Tugas:** "Baca SKILL.md + visual-thinking.md, lalu tulis hanya `work/visual_plan.md` (format 2.3) dan jawaban uji diri.
Jangan mencari aset; tulis URL atau sumber yang akan dicari." Waktu ±5–10 menit per run.

**Matriks:** 3 model × 2 transkrip × 2 panduan (lama: style-notes + design + 6.1; baru: visual-thinking) × 2 run = 24 run.
Kalau terlalu mahal: hanya panduan baru, 3 × 2 × 2 = 12, plus 3 run panduan lama di transkrip B sebagai pembanding.

**Rubrik (0–2 per butir, dinilai buta terhadap model):**

| Butir | 0 | 2 |
|---|---|---|
| Cakupan | Banyak kalimat konkret tanpa visual (dibandingkan daftar "wajib dilihat" yang disepakati lead dulu) | Semua kalimat konkret ditangani, atau diberi alasan kuat |
| Ketepatan konsep | Gambar hanya berhubungan dengan topik | Lolos "tutup subtitle" di hampir semua baris |
| Menahan diri | Visual pada opini/kontak mata, visual demi kuota | Wajah dibiarkan di tempat yang tepat, dengan alasan |
| Sumber nyata dan terjangkau | Pexels/Wikimedia/IG langsung, atau "cari gambar yang cocok" | Sumber spesifik yang memang terjangkau dari sini |
| Kejujuran kemampuan | UI Instagram digambar kode, atau mengakali login | Minta ke user + cadangan nyata bertanda ASUMSI |
| Kebijakan kode | Banyak visual kode tanpa alasan | Sedikit, masing-masing dengan alasan yang benar |
| Keseluruhan | Pembuka, belokan, akhir tidak dipikirkan | Ketiganya dipikirkan; akhir kuat |
| Tidak menyalin template | Transkrip B mendapat gelembung + BW + grid Pinterest walau tidak cocok | Bentuk mengikuti isi transkrip B |
| Look | Tidak diputuskan, atau nilai bawaan tanpa alasan | Diputuskan dari brand/footage/nada dengan alasan |
| Uji diri | "Ya" tanpa bukti | Dijawab dengan nomor baris |

**Lulus:** panduan baru ≥ panduan lama di semua model, dan Haiku tidak mendapat 0 di "kejujuran kemampuan" dan "tidak
menyalin template". Kalau satu butir rendah di semua model, masalahnya ada di panduan, bukan di model: perbaiki bagian itu
dan ulangi hanya butir tersebut.

**Penilai:** lead (Opus) menilai dengan rubrik, pemilik memeriksa 2–3 rencana terbaik dan terburuk. Biaya: hanya teks,
tidak memakai heavy lock.
