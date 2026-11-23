---
name: edit-aroll
description: Mengedit A-roll (video orang bicara / talking head, jenis konten apa pun) menjadi 1 video pendek siap publish. Memilih take, memotong, subtitle per kata, visual dari sumber nyata yang mengikuti isi omongan, render dengan Remotion, lalu QA frame per frame. Pakai saat user memberi klip mentah atau link Google Drive dan minta diedit, atau minta revisi video hasil edit.
---

# Edit A-roll menjadi 1 video siap publish (Editor Team, cloud)

File ini adalah peta kerja. Detail tiap bagian ada di `reference/` dan WAJIB dibaca pada titik yang disebut di tabel tahap:
jangan mengerjakan sebuah tahap dari ingatan. Catat di `work/STATE.md` file referensi mana yang sudah dibaca.

| File | Isi | Dibaca kapan |
|---|---|---|
| `reference/kit.md` | Menyiapkan job, struktur folder, daftar skrip, arsitektur | Sebelum Tahap 0 |
| `reference/workflow.md` | 11 tahap (0–10) lengkap dengan perintah dan gate | Sebelum Tahap 0; baca ulang bagian tahapnya saat mengerjakan |
| `reference/edit-json.md` | Format `work/edit.json`, jangkar waktu, jenis event, cara menambah visual | Sebelum Tahap 4 |
| `reference/visual-thinking.md` | Kapan memberi visual dan kapan tidak, aset nyata dan yang bisa dijangkau dari sini, kebijakan kode, look per video, kalibrasi, uji diri, contoh penalaran | Bagian 4 dan 6 sebelum menulis brief (Tahap 0); seluruhnya sebelum Tahap 6; Bagian 8 sebelum render penuh |
| `reference/visual-craft.md` | Menyajikan berita/dokumen, kapan memotong, posisi, timing, gerak, caption, terlalu jarang vs terlalu ramai, apa yang kit bisa sekarang | Sebelum Tahap 6; Bagian 5–6 lagi di Tahap 8 |
| `reference/design.md` | Struktur cerita per jenis roll, suara, sumber 16:9, bahasa lain | Sebelum Tahap 3 |
| `reference/troubleshooting.md` | Masalah khusus cloud + masalah umum | Saat ada yang gagal, sebelum mencari sebab lain |

Kode skrip dan komponen tidak ditempel di skill ini: sumbernya file di folder job (`tools/`, `video/src/`).
Guide asli utuh (termasuk instalasi di komputer lokal) diarsipkan di repo `docs/GUIDE-original.md`; tidak perlu dibaca.

## Berlaku untuk siapa saja: perusahaan mana pun, atau tanpa perusahaan

Skill ini bukan untuk satu brand. Contoh yang menyebut nama brand (Parcelin, video benchmark) adalah **bukti dan ilustrasi cara
menimbang**, bukan isi yang dibawa ke video lain. Aturan di sini berlaku untuk tiga keadaan, dan Tahap 0 dimulai dengan memutuskan
video ini termasuk yang mana (`workflow.md` Tahap 0, "Pemilik video"):

| Keadaan | Tandanya | Dari mana nama, akun, logo, warna, penutup |
|---|---|---|
| **Brand yang sudah punya profil** | Lead menyebut `docs/brands/<brand>.md` di brief DAN footage/user membenarkannya | Profil itu, setelah dicek ulang terhadap footage dan jawaban user |
| **Perusahaan atau brand baru** | Pembicara atau user menyebut usaha yang belum punya profil | User (ditanya di awal) + bahan resmi usaha itu (situs, akun publik). Tidak ada yang dipinjam dari brand lain |
| **Tanpa perusahaan** (kreator pribadi, edukasi, opini, cerita, tutorial umum) | Tidak ada usaha yang dijual atau diwakili | Tidak ada logo, warna brand, atau closing brand. Look dari footage dan nada isi; penutup dari kalimat terakhir |

Tiga hal yang tidak pernah dilakukan: (1) memakai nama, akun, logo, warna, slogan, atau penutup dari profil brand lain karena "biasanya
begitu"; (2) mengarang brand, akun, atau logo untuk video yang tidak punya; (3) menganggap video milik sebuah brand hanya karena
user yang sama pernah mengirim video brand itu. Kalau pemilik video tidak jelas dari footage dan brief: tulis `ASUMSI`, tanyakan ke
lead, dan sementara itu jangan menampilkan nama atau akun apa pun di layar.

Seluruh alur (tahap 0 sampai 10, gate, QA) sama untuk ketiganya. Yang berbeda hanya sumber identitas dan bentuk penutup.

## Aturan environment cloud (mengalahkan guide bila bertentangan)

- Kit sudah terpasang di `/home/user/editkit`. Buat job dengan `bash /home/user/editkit/new_job.sh <job-id>`; semua perintah
  dijalankan dari `/home/user/jobs/<job-id>/`. Jangan jalankan `tools/setup.sh`, `pip install`, `npm install`, atau `playwright install`.
- Python selalu lewat venv: `source .venv/bin/activate && ...`.
- Perintah BERAT (`transcribe.py`, `verify_audio.py`, `node stills.mjs`, `render.sh`) wajib antre:
  `flock /home/user/jobs/.heavy.lock <perintah>`. Render: `CONCURRENCY=2 flock /home/user/jobs/.heavy.lock bash tools/render.sh vN`.
  Perintah lama dijalankan di background dengan log ke `work/`.
- Font hanya font SISTEM (web font membuat render macet): lihat `reference/troubleshooting.md`. Jangan menambah `loadFont`/google-fonts.
- Sumber yang diblokir (Pexels, Wikimedia, YouTube, halaman berlogin) tidak diakali: pakai halaman publik resmi, Openverse, atau minta ke user.
- Jangan mengubah file di `raw/`, kit bersama `/home/user/editkit`, atau job lain.

## Preferensi user (berlaku di setiap video)

Dari pemilik langsung; ini syarat, bukan gaya satu editor. Detail dan alasannya di `visual-thinking.md` dan `visual-craft.md`.

- **Putuskan per kalimat, dengan alasan tertulis:** visual atau tidak, layar penuh atau tidak, kapan muncul dan berapa lama. Bukan
  bawaan, bukan kuota. Alasan: video yang bagus memberi gambar tepat di saat penonton butuh melihat, dan wajah saat isinya pendapat.
- **Aset nyata dulu, selalu.** Berita → potongan situs beritanya; DM Instagram → Instagram yang asli (dari user kalau terkunci login);
  brand → logo aslinya. Gambar buatan kode hanya dengan alasan tertulis kenapa tidak ada aset nyata. Alasan: yang nyata dikenali sekejap
  dan dipercaya; banyak gambar kode tidak pernah terlihat rapi. Tampilan aplikasi atau artikel palsu sebagai bukti tidak pernah boleh.
- **Visualnya cocok:** memperlihatkan konsep yang diucapkan (uji: tutup subtitle-nya).
- **Tidak pernah lama sepi, tidak terlalu ramai.** Rentang panjang tanpa perubahan gambar ditolak build (`max_quiet_s`); pemilik menolak
  job01 v4 yang punya 16 detik. Tetapi satu fokus per frame, dan visual yang tidak menambah apa pun dihapus.
- **Gunakan setiap momen dengan kreatif:** ucapan orang lain → gelembung chat kiri/kanan; nama → bendanya; belokan → perubahan seluruh gambar.
- **Potong dengan alasan, posisi rapi, gerak halus dan bermakna:** audio tidak pernah dipotong di tengah kalimat; wajah tidak tertutup;
  gerak dicek di frame berurutan.
- **Gambar mengalir, sedikit cut** (masukan job02: "kebanyakan cut… jangan cuma fokus di voice/subtitle… jangan patah-patah atau
  ke-skip"). Satu take utuh sebagai dasar; potong hanya kalau perlu; pembicara tidak pernah terlihat meloncat di sambungan. Sambungan
  yang terdengar bersih belum tentu terlihat bersih. Build menolak sambungan terbuka tanpa alasan (CUT CHECK, `cut_ok`). Detail:
  `workflow.md` Tahap 2 sampai 4.
- **Backsound sesuai momen.** Setiap video punya musik latar yang dipilih dari nada isinya dan mengikuti belokan naskah; lisensinya
  dicatat. Detail: `workflow.md` Tahap 6.2 (Musik).
- **Durasi tiap visual pas:** tidak terlalu panjang, tidak terlalu pendek. Visual yang terjepit tetangganya direncanakan ulang,
  bukan dipendekkan (`visual-craft.md` 5).
- **Momen ditunjukkan sebagai momennya; halaman sebagai halaman.** Nama hari raya atau peristiwa → foto nyata momen itu, layar penuh,
  bukan produk brand. Situs yang dituju penonton → satu halaman penuh, bukan kartu kecil di tengah (`visual-thinking.md` 3).
- **Penutup mengikuti kalimat terakhir dan pemilik video:** video sebuah brand yang ditutup slogan/kesimpulan/ajakan memesan →
  animasi closing brand itu (logo aslinya dan tanda brand lain yang diminta user); kartu profil/kontak hanya kalau pembicara menutup
  dengan "hubungi aku"; video tanpa perusahaan tidak diberi logo: penutupnya ajakan yang diucapkan atau berhenti di kalimat terakhir
  (`visual-thinking.md` 3).
- **Tanya di awal:** semua aset dan konfirmasi yang dibutuhkan dilaporkan ke lead di awal dalam satu daftar (`workflow.md` Tahap 0 dan 3).
- **Tidak ada gaya tetap.** Look diputuskan per video dari brand, footage, dan nada isi, ditulis di `work/brief.md` dan blok `theme`
  di `work/edit.json` (build menolak job tanpa `theme`). Kalau ada profil brand (`/home/user/editor-team/docs/brands/<brand>.md`, disebut lead di brief), ikuti.

## Bagian 1. Cara berpikir

### 1.1 Agent tidak menonton dan tidak mendengar

Agent tidak bisa memutar video. Hasil yang flat hampir selalu terjadi karena agent mengedit "buta": menulis kode animasi tanpa pernah tahu apa yang diucapkan pada detik itu, dan tanpa pernah melihat hasilnya. Solusinya: ubah video menjadi bentuk yang bisa dibaca dan dilihat, lalu periksa hasil sendiri dengan cara yang sama.

| Yang harus dipahami | Diubah menjadi | Alat |
|---|---|---|
| Apa yang diucapkan dan kapan persisnya | Transkrip per kata dengan waktu mulai dan selesai | `tools/transcribe.py` (faster-whisper large-v3) |
| Di mana ada sunyi untuk memotong | Angka kenyaringan (dB) tiap 10 ms | `tools/envelope.py` (ffmpeg + numpy) |
| Apa yang terlihat di gambar | Contact sheet: grid frame yang dibuka dan dilihat | `tools/sheet.py` (ffmpeg + Pillow) |
| Aset mana yang cocok | Contact sheet kandidat foto, footage, logo | `tools/stock.py` |
| Apakah desain sesuai rencana | Still frame dari komposisi, tanpa render penuh | `video/stills.mjs` (Remotion renderStill) |
| Apakah transisi mulus | Strip 12 frame berurutan di setiap transisi, ditambah daftar perubahan gambar mendadak | `tools/sheet.py strips`, `tools/scene_check.py` |
| Apakah audio hasil potong utuh | Transkrip ulang dari video hasil render | `tools/verify_audio.py` |

"Melihat" berarti membuka file gambarnya dengan tool pembaca gambar (Claude Code: tool Read pada file .jpg atau .png; Codex: `view_image`; agent lain: tool sejenis) dan menilai isinya. Perintah yang selesai tanpa error bukan bukti bahwa gambarnya benar.

### 1.2 Delapan aturan yang tidak boleh dilanggar

1. **Cerita dulu, baru potong.** Naskah final ditulis dan dicek sebelum ada satu pun keputusan visual.
2. **Semua waktu ditambatkan ke kata.** Setiap subtitle, visual, dan efek suara menunjuk indeks kata di transkrip, bukan angka frame yang diketik tangan. Saat titik potong digeser, semuanya ikut bergeser otomatis.
3. **Visual menggambarkan kalimat yang sedang diucapkan.** Untuk setiap visual harus bisa dijawab: kata mana yang digambarkan, dan kenapa penonton terbantu? Kalau tidak bisa dijawab, visualnya dibuang. Uji: tutup subtitle-nya; apakah gambarnya masih menjelaskan kata itu?
4. **Sumber nyata dulu.** Aset nyata dari hal yang dibicarakan (halaman, aplikasi, foto, footage, logo asli); kode untuk menggerakkannya dan untuk hal yang tidak punya gambar, dengan alasan tertulis; image generation hanya untuk benda tanpa foto nyata, tidak pernah untuk orang nyata, logo, tampilan aplikasi, atau bukti. Tampilan aplikasi yang terkunci login tidak digambar ulang: minta rekaman atau screenshot ke user (`visual-thinking.md` 4).
5. **Sedikit cut, gambar mengalir.** Pilih satu take sebagai dasar dan biarkan berjalan. Yang dibuang hanya take ulang, salah ucap, jeda mati, dan kalimat yang tidak menambah apa-apa. Tidak ada potongan di tengah kalimat, dan tidak ada sambungan yang memperlihatkan pembicara meloncat: setiap sambungan dihapus, ditutup visual yang relevan, atau diberi alasan tertulis (`cut_ok`). Menukar satu kalimat dengan take lain demi kalimat yang sedikit lebih rapi bukan alasan untuk memotong.
6. **Lihat hasil sendiri sebelum menyerahkan.** Setiap tahap yang menghasilkan gambar diakhiri dengan membuka gambarnya.
7. **Revisi hanya menyentuh yang diminta.** Bagian yang sudah disetujui tidak diubah.
8. **Bersih dan sesuai dunia nyata.** Satu fokus per frame. Gaya visual mengikuti hal nyata yang dibicarakan (aplikasinya, situsnya, brand-nya), bukan satu gaya tetap. Gerak hanya di tempat yang membantu memahami ucapan.

### 1.3 Cara kerja bertahap

Kerjakan tahap 0 sampai 10 berurutan (Bagian 3). Setiap tahap menulis hasilnya ke file di `work/`, dan punya **gate**: daftar cek yang harus lolos sebelum lanjut. Setelah setiap tahap, perbarui `work/STATE.md` (tahap terakhir yang selesai, keputusan, asumsi, hal yang belum beres). Kalau konteks percakapan terpotong, baca `work/STATE.md` dan file tahap terakhir, lalu lanjutkan dari sana. Jangan mulai ulang. **Perbarui `work/STATE.md` juga sebelum setiap render dan setiap putaran revisi dimulai** (versi yang sedang dibuat, apa yang diubah, alasan): sesi worker bisa terhenti di tengah render (job02: batas pemakaian), dan lead melanjutkan dari file ini.

## Peta 11 tahap (detail dan gate lengkap: `reference/workflow.md`)

| Tahap | Isi | Hasil | Gate singkat |
|---|---|---|---|
| Pra | Kesiapan | `doctor.py` → `RESULT: READY` | READY |
| 0 | Brief dan bahan | `work/brief.md`, klip di `raw/` | Jenis konten, durasi, CTA terisi; look diputuskan dengan alasan; daftar "Butuh dari user" dilaporkan ke lead; asumsi ditandai `ASUMSI`; ejaan nama brand dicek |
| 1 | Normalisasi, melihat footage | `video/public/*.mp4`, `work/look_*.jpg`, `work/footage.md` | Semua contact sheet DIBUKA; benda yang ditunjukkan dicatat dengan waktunya |
| 2 | Transkrip, peta roll | `work/tx/*`, `work/roll_map.md` | Tiap kalimat bertanda; tiap kelompok take ulang punya satu pemenang |
| 3 | Naskah final | `work/script.md` | Hook ≤3 dtk; satu take dasar; tiap potongan punya alasan DAN rencana gambar di sambungannya; uji sambungan lolos; pertanyaan naskah dilaporkan ke lead |
| 4 | Titik potong presisi (envelope) | `segments` di `work/edit.json` | Tiap in/out di titik < −30 dB; tidak ada potong di tengah kata |
| 5 | Teks subtitle | `text`/`script`/`timing` | Daftar subtitle terbaca sebagai naskah utuh; nama benar |
| 6 | Rencana visual dan aset | `work/visual_plan.md`, aset di `video/public/` | Tiap kalimat punya keputusan + alasan; tiap visual punya kata jangkar, durasi, aset yang sudah DILIHAT dan terjangkau; tiap visual kode punya alasan |
| 7 | Bangun timeline | `theme`, `events`, `video/src/data.json` | 0 error (termasuk `theme`, QUIET CHECK, CUT CHECK); tiap warning, tiap `quiet_ok`, dan tiap `cut_ok` dijelaskan |
| 8 | Loop still | `work/qa_stills.jpg` | Tiap event punya still yang lolos; posisi rapi; transisi baru lolos cek frame berurutan; uji diri (`visual-thinking.md` 8) dijawab dengan bukti; QA 5 dicek lebih dulu |
| 9 | Render dan 5 QA | `out/final_vN.mp4`, log QA | Kelima QA lolos PADA FILE YANG DIKIRIM (+ blackdetect 0) |
| 10 | Serah terima, revisi | laporan, `final_v(N+1)` | Revisi hanya menyentuh yang diminta; versi lama disimpan |

## Bagian 8. Batasan yang harus disampaikan dengan jujur

- Agent tidak mendengar. Sambungan audio dicek lewat transkrip ulang dan angka kenyaringan. Intonasi, rasa musik, dan bunyi efek belum dinilai telinga. Minta user menonton sekali dengan suara.
- Agent melihat frame, bukan gerak. Kelancaran gerak dinilai dari strip frame berurutan. Itu menangkap frame yang salah, tetapi rasa tempo tetap perlu mata manusia.
- Ejaan nama yang hanya terdengar di audio bisa salah. Selalu laporkan sebagai asumsi.
- Yang sudah dijalankan pada project nyata: output 9:16 (1080x1920 dan skala lebih besar), Linux. Yang belum: output 16:9, macOS dan Windows/WSL2, GPU. Di sana, jalankan `doctor.py` dan loop still lebih teliti.
- Dari container ini Instagram/TikTok/Facebook (login), Pexels dan Wikimedia (diblokir), dan YouTube tidak bisa dipakai. Tampilan aplikasi berlogin datang dari rekaman atau screenshot user, bukan digambar ulang (`visual-thinking.md` 4).
- Beberapa teknik editor acuan (masuk langsung tanpa fade, punch-in di kata pilihan, strip judul di bawah dagu, volume musik per momen, halaman penuh dengan kursor) belum ada di kit: lihat `visual-craft.md` 9.
- Selera (warna, font, seberapa ramai) berbeda tiap orang. Versi pertama adalah usulan. Revisi dikerjakan dengan aturan tahap 10.
- Guide ini membuat prosesnya bisa diulang. Kualitas akhir tetap bergantung pada apakah setiap gate benar-benar dikerjakan dan setiap gambar QA benar-benar dibuka.

## Bagian 9. Checklist akhir dan format laporan

Sebelum mengirim, semua harus tercentang:

- [ ] Hook di 3 detik pertama, CTA di akhir.
- [ ] Naskah nyambung di setiap sambungan. Tidak ada take ulang atau salah ucap yang lolos.
- [ ] Setiap potongan di titik sunyi. `verify_audio.py` bersih di semua sambungan.
- [ ] Subtitle sama dengan ucapan, nama dieja benar, kata besar seperlunya.
- [ ] Setiap visual menggambarkan kalimatnya dan sumbernya dicatat.
- [ ] Uji diri `visual-thinking.md` Bagian 8 dijawab dengan bukti. Setiap visual buatan kode punya alasan tertulis.
- [ ] Tampilan bersih. Logo dan tampilan aplikasi atau situs memakai bahan asli dan terlihat seperti aslinya. Gerak hanya yang membantu.
- [ ] CUT CHECK lolos: jumlah potongan dilaporkan, tidak ada sambungan terbuka tanpa `cut_ok` beralasan; strip tiap sambungan sudah dilihat.
- [ ] Musik latar ada, cocok dengan nada isi, mengikuti belokan naskah; sumber dan lisensi dicatat.
- [ ] Penutup cocok dengan kalimat terakhir (slogan → closing brand; "hubungi aku" → kartu profil/kontak).
- [ ] QUIET CHECK lolos; setiap `quiet_ok` punya alasan. Kepadatan dan porsi layar dibandingkan dengan `visual-thinking.md` 7; selisih besar dijelaskan.
- [ ] Semua strip transisi sudah dilihat. `scene_check.py`: 0 yang tidak terjelaskan.
- [ ] Teknis: 1080x1920 (atau 1440x2560), 30 fps, `yuv420p` BT.709, sekitar -15 LUFS, file bisa diputar.
- [ ] Semua pemeriksaan dilakukan pada file yang dikirim.

Format laporan ke user:

```
Video: out/final_v1.mp4 (durasi, ukuran)
Potongan: klip yang dipakai, klip atau bagian yang dibuang dan alasannya
Visual sumber nyata: daftar singkat + URL
Visual lain: foto stok (dengan lisensi yang butuh atribusi), diagram, gambar buatan
Visual buatan kode: daftar + alasan satu kalimat masing-masing
Potongan gambar: angka CUT CHECK (jumlah, satu per berapa detik), take dasar, setiap cut_ok + alasan
Musik: judul, sumber, lisensi, di mana musik berubah mengikuti naskah
Rentang sepi: angka QUIET CHECK, porsi layar, setiap quiet_ok + alasan
Diminta dari user: daftar, dan apa yang dipakai sementara
Asumsi yang perlu dikonfirmasi: ejaan nama, CTA, dan sebagainya
Belum diverifikasi: belum didengarkan langsung; apa pun yang gagal atau dilewati
```
