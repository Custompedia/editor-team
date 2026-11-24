# Studi referensi: podcast "Cerita Perintis" Eps 001 (Custompedia) — BELUM LENGKAP (2026-11-24)

> **Arsip untuk lead.** Pemilik meminta desain podcast berikutnya disamakan dengan video ini. Studi ini baru berisi yang terlihat di
> empat gambar diam publik; bagian yang bergerak (teaser, subtitle, perkenalan, bumper, zoom) BELUM dilihat siapa pun di tim.
> Jangan menulis brief worker dari file ini sebelum bagian 3 terisi dari video aslinya.

## 0. Bahan
- Video: `https://www.youtube.com/watch?v=PJ9LDlZ7XUQ` — "Dari Nol Bareng Istri "Jalanin Dulu Aja" | Cerita Perintis Eps 001
  (ft. Prahendita Putri)", kanal Custompedia (`@CustompediaCreative`). Sumber judul dan kanal: YouTube oEmbed.
- `yt-dlp` dan halaman YouTube ditolak dari container (bot check, HTTP 429). Tidak diakali. File mp4 diminta ke pemilik.
- Yang bisa dibuka tanpa login: oEmbed dan `https://i.ytimg.com/vi/<id>/{maxresdefault,maxres1,maxres2,maxres3}.jpg`
  (thumbnail + tiga frame otomatis, 1280x720). Tiga frame itu bertanda waktu 00:00:55:18, 00:07:35:03, 00:15:27:09.

## 1. Yang terlihat (diukur di frame 1280x720; dikali 1,5 untuk 1920x1080)
| Elemen | Posisi dan bentuk | Catatan |
|---|---|---|
| Logo acara "Cerita Perintis / with @radhytam" | Kiri atas, x 54–221, y 41–81 (lebar ±13% layar; margin kiri ±4%, atas ±5,5%). Putih, garis tipis berbentuk gelembung bicara di sekelilingnya, ikon mik kecil sebagai titik huruf "i" | Ada di ketiga frame, tempat sama |
| Tanda Custompedia (dua gelembung bicara, tanpa tulisan) | Kanan atas, x 1190–1238, y 34–86; margin kanan ±3,3%. Putih | Ada di ketiga frame |
| Timecode | Tengah bawah, y 659–686 (tinggi angka ±3,7% layar, pusat di ±93% tinggi). Format `JJ:MM:DD:FF`, putih tipis, tembus pandang (kira-kira setengah), angka sama lebar | Ada di ketiga frame. Belum diketahui: mulai dari 0 di awal video atau setelah bumper |
| Subtitle | Tidak ada di ketiga frame (0:55, 7:35, 15:27) | Cocok dengan permintaan pemilik: setelah bumper tanpa subtitle |
| Ikon aplikasi "dP" (kotak sudut bulat, bingkai biru) | Di atas meja, kiri tengah, x 400–485, y 522–607, pada 0:55 | Diduga logo yang muncul saat sebuah nama disebut. Brand apa: BELUM DIKETAHUI |
| Sudut kamera | Lebar dua orang (meja marmer, latar biru gradasi) dan dekat satu orang (tamu) | Belum diketahui: kamera kedua atau potongan dari gambar lebar; ada gerak zoom atau tidak |

Thumbnail: logo acara di tengah atas, judul kuning huruf besar "EP 01 NEKAT MERINTIS BARENG" di sepertiga bawah ("EP 01" kecil dan
tipis di kiri baris pertama), logo Custompedia lengkap di tengah bawah di atas gradasi gelap.

## 2. Permintaan pemilik untuk job ini (kata-katanya, 2026-11-24)
- Pahami: desain subtitle dan animasinya, font, zoom, letak logo, letak judul "Cerita Perintis", desain dan animasi saat
  memperkenalkan diri, "ada detik-an di bawah".
- Susunan: teaser di awal, lalu bumper, lalu podcast biasa. Setelah bumper tidak ada subtitle.
- Intro awal disamakan dengan video YouTube ini.
- Grading tipis untuk membetulkan skin tone.

## 3. BELUM DILIHAT (isi dari file mp4)
- Teaser: panjang, jumlah potongan, subtitle (font, ukuran, posisi, warna, per kata atau per baris, animasi masuk), musik.
- Perkenalan diri: bentuk lower third, isi teks, animasi masuk/keluar, berapa lama.
- Bumper: file siap pakai atau dibuat ulang; durasi; suara.
- Zoom: ada punch-in atau hanya ganti kamera; seberapa sering; halus atau langsung.
- Timecode: font pastinya, mulai dari mana, fps.
- Logo yang muncul di meja: kapan, animasinya, berapa lama.
- Penutup episode.

## 4. Kesenjangan kit untuk jenis job ini
- Kit dikunci 9:16 dan untuk video pendek; 16:9 belum pernah diuji (`reference/design.md`).
- Render Remotion ±25 menit per 125 detik: episode 15–20 menit tidak layak dirender penuh lewat Remotion. Rencana yang masuk akal:
  Remotion hanya untuk bagian bergrafis (teaser, perkenalan) dan lapisan transparan; badan podcast digabung dengan ffmpeg
  (logo, timecode, grading). Belum dibuktikan.
