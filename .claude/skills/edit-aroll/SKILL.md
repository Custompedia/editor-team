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
| `reference/style-notes.md` | Standar kualitas user (18 prinsip dari video referensinya) + "Quality bar" | Sebelum Tahap 6; checklist bagian 4 sebelum render |
| `reference/design.md` | Standar desain bawaan + penyesuaian per jenis roll (struktur cerita, kepadatan) | Sebelum Tahap 3 (bagian 6) dan Tahap 6 (bagian 5) |
| `reference/troubleshooting.md` | Masalah khusus cloud + masalah umum | Saat ada yang gagal, sebelum mencari sebab lain |

Kode skrip dan komponen tidak ditempel di skill ini: sumbernya file di folder job (`tools/`, `video/src/`).
Guide asli utuh (termasuk instalasi di komputer lokal) diarsipkan di repo `docs/GUIDE-original.md`; tidak perlu dibaca.

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

- **Tidak ada satu gaya tetap.** Kuning `#FFD60A`, font, dan UI bawaan kit hanya titik awal. Warna, aksen, pola warna teks, dan
  font mengikuti brief, brand, dan footage; tulis pilihan + alasannya di `work/brief.md`, atur di `video/src/theme.ts`.
- **Bersih tidak sama dengan sepi.** Rapi dan konsisten, tetapi visual harus cukup banyak dan jelas, di momen yang tepat
  (patokan: ±1 beat visual tiap ±5 dtk, layar penuh ±30–40%, wajah tanpa visual paling lama ±7 dtk). Rinciannya di `reference/style-notes.md`.
- **Gambarkan konsep yang diucapkan**, dengan aset nyata yang bagus (halaman asli, foto asli, logo asli brand) lebih dulu
  daripada gambar buatan kode. Catat URL sumber + lisensi tiap aset.
- **Prinsip, bukan cetakan.** Referensi dipakai untuk memahami kenapa sebuah edit bagus, bukan untuk ditiru di semua video.

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
3. **Visual menggambarkan kalimat yang sedang diucapkan.** Untuk setiap visual harus bisa dijawab: kata mana yang digambarkan, dan kenapa penonton terbantu? Kalau tidak bisa dijawab, visualnya dibuang.
4. **Sumber nyata dulu.** Urutannya: screenshot halaman atau aplikasi asli, foto/footage/logo asli, lalu SVG buatan sendiri untuk angka dan diagram, lalu gambar hasil image generation. Kotak berisi teks yang dianimasikan adalah pilihan terakhir, bukan gaya utama. Tampilan aplikasi atau situs dibuat dari tampilan aslinya, bukan dikarang.
5. **Sedikit cut.** Yang dibuang hanya take ulang, salah ucap, jeda mati, dan kalimat yang tidak menambah apa-apa. Tidak ada potongan di tengah kalimat.
6. **Lihat hasil sendiri sebelum menyerahkan.** Setiap tahap yang menghasilkan gambar diakhiri dengan membuka gambarnya.
7. **Revisi hanya menyentuh yang diminta.** Bagian yang sudah disetujui tidak diubah.
8. **Bersih dan sesuai dunia nyata.** Tampilan rapi dan tidak ramai. Gaya visual mengikuti hal nyata yang sedang dibicarakan (aplikasinya, situsnya, brand-nya), bukan satu gaya tetap. Tata letak berganti dari scene ke scene, dan gerak hanya di tempat yang membantu memahami ucapan.

### 1.3 Cara kerja bertahap

Kerjakan tahap 0 sampai 10 berurutan (Bagian 3). Setiap tahap menulis hasilnya ke file di `work/`, dan punya **gate**: daftar cek yang harus lolos sebelum lanjut. Setelah setiap tahap, perbarui `work/STATE.md` (tahap terakhir yang selesai, keputusan, asumsi, hal yang belum beres). Kalau konteks percakapan terpotong, baca `work/STATE.md` dan file tahap terakhir, lalu lanjutkan dari sana. Jangan mulai ulang.

## Peta 11 tahap (detail dan gate lengkap: `reference/workflow.md`)

| Tahap | Isi | Hasil | Gate singkat |
|---|---|---|---|
| Pra | Kesiapan | `doctor.py` → `RESULT: READY` | READY |
| 0 | Brief dan bahan | `work/brief.md`, klip di `raw/` | Jenis konten, durasi, CTA terisi; asumsi ditandai `ASUMSI`; ejaan nama brand dicek |
| 1 | Normalisasi, melihat footage | `video/public/*.mp4`, `work/look_*.jpg`, `work/footage.md` | Semua contact sheet DIBUKA; benda yang ditunjukkan dicatat dengan waktunya |
| 2 | Transkrip, peta roll | `work/tx/*`, `work/roll_map.md` | Tiap kalimat bertanda; tiap kelompok take ulang punya satu pemenang |
| 3 | Naskah final | `work/script.md` | Hook ≤3 dtk; uji sambungan lolos; yang dibuang punya alasan |
| 4 | Titik potong presisi (envelope) | `segments` di `work/edit.json` | Tiap in/out di titik < −30 dB; tidak ada potong di tengah kata |
| 5 | Teks subtitle | `text`/`script`/`timing` | Daftar subtitle terbaca sebagai naskah utuh; nama benar |
| 6 | Rencana visual dan aset | `work/visual_plan.md`, aset di `video/public/` | Tiap visual menjawab "kata mana yang digambarkan"; aset sudah DILIHAT; ≥2 tata letak |
| 7 | Bangun timeline | `events`, `video/src/data.json` | 0 error; tiap warning dijelaskan |
| 8 | Loop still | `work/qa_stills.jpg` | Tiap event punya still yang lolos; Quality bar (style-notes §4) lolos; QA 5 dicek lebih dulu |
| 9 | Render dan 5 QA | `out/final_vN.mp4`, log QA | Kelima QA lolos PADA FILE YANG DIKIRIM (+ blackdetect 0) |
| 10 | Serah terima, revisi | laporan, `final_v(N+1)` | Revisi hanya menyentuh yang diminta; versi lama disimpan |

## Bagian 8. Batasan yang harus disampaikan dengan jujur

- Agent tidak mendengar. Sambungan audio dicek lewat transkrip ulang dan angka kenyaringan. Intonasi, rasa musik, dan bunyi efek belum dinilai telinga. Minta user menonton sekali dengan suara.
- Agent melihat frame, bukan gerak. Kelancaran gerak dinilai dari strip frame berurutan. Itu menangkap frame yang salah, tetapi rasa tempo tetap perlu mata manusia.
- Ejaan nama yang hanya terdengar di audio bisa salah. Selalu laporkan sebagai asumsi.
- Yang sudah dijalankan pada project nyata: output 9:16 (1080x1920 dan skala lebih besar), Linux. Yang belum: output 16:9, macOS dan Windows/WSL2, GPU. Di sana, jalankan `doctor.py` dan loop still lebih teliti.
- Pencarian stok lewat browser bergantung pada tampilan situs saat ini. Kalau situsnya berubah, pakai sumber cadangan atau aset dari user.
- Selera (warna, font, seberapa ramai) berbeda tiap orang. Versi pertama adalah usulan. Revisi dikerjakan dengan aturan tahap 10.
- Guide ini membuat prosesnya bisa diulang. Kualitas akhir tetap bergantung pada apakah setiap gate benar-benar dikerjakan dan setiap gambar QA benar-benar dibuka.

## Bagian 9. Checklist akhir dan format laporan

Sebelum mengirim, semua harus tercentang:

- [ ] Hook di 3 detik pertama, CTA di akhir.
- [ ] Naskah nyambung di setiap sambungan. Tidak ada take ulang atau salah ucap yang lolos.
- [ ] Setiap potongan di titik sunyi. `verify_audio.py` bersih di semua sambungan.
- [ ] Subtitle sama dengan ucapan, nama dieja benar, kata besar seperlunya.
- [ ] Setiap visual menggambarkan kalimatnya dan sumbernya dicatat.
- [ ] Sebagian besar visual dari sumber nyata. Tidak ada tiga jenis visual sama berturut-turut. Minimal dua tata letak.
- [ ] Tampilan bersih. Logo dan tampilan aplikasi atau situs memakai bahan asli dan terlihat seperti aslinya. Gerak hanya yang membantu.
- [ ] Insert menutup 20 sampai 45% durasi. Tidak ada 8 detik tanpa perubahan visual.
- [ ] Semua strip transisi sudah dilihat. `scene_check.py`: 0 yang tidak terjelaskan.
- [ ] Teknis: 1080x1920 (atau 1440x2560), 30 fps, `yuv420p` BT.709, sekitar -15 LUFS, file bisa diputar.
- [ ] Semua pemeriksaan dilakukan pada file yang dikirim.

Format laporan ke user:

```
Video: out/final_v1.mp4 (durasi, ukuran)
Potongan: klip yang dipakai, klip atau bagian yang dibuang dan alasannya
Visual sumber nyata: daftar singkat + URL
Visual lain: foto stok (dengan lisensi yang butuh atribusi), diagram, gambar buatan
Asumsi yang perlu dikonfirmasi: ejaan nama, CTA, dan sebagainya
Belum diverifikasi: belum didengarkan langsung; apa pun yang gagal atau dilewati
```
