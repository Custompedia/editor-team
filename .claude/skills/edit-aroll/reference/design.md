# Struktur cerita per jenis roll, suara, dan format

Cara memutuskan visual, tampilan (look), dan kepadatan ada di `visual-thinking.md` dan `visual-craft.md`, tidak di sini.
Perilaku tampilan bawaan kit (posisi subtitle, transisi insert) ada di `kit.md` 2.4.

# Bagian 5. Suara

- Suara pembicara: -15 LUFS, puncak -1,5 dB, fade 2 frame di setiap sambungan.
- Efek: `whoosh` saat insert masuk, `swish` saat berantai dan saat panel `split` masuk, `pop` saat overlay muncul, `click` saat kursor mengklik. Puncak efek -18 sampai -24 dB, jauh di bawah suara.
- Musik hanya kalau diminta, volume 0,05 sampai 0,08.

---

# Bagian 6. Penyesuaian per jenis roll

### 6.1 Struktur cerita

| Jenis | Struktur | Hook yang dicari |
|---|---|---|
| Tutorial / cara | Hasil atau masalah, kenapa penting, langkah 1 sampai n, hasil, CTA | Hasil akhir atau kesalahan yang sering terjadi |
| Opini / edukasi | Klaim, konteks atau data, argumen 1 sampai n, kesimpulan, CTA | Klaim yang berlawanan dengan anggapan umum |
| Review produk | Verdict singkat, apa produknya, kelebihan, kekurangan, cocok untuk siapa, CTA | Verdict atau kejutan terbesar |
| Podcast / interview | Kutipan terkuat, pertanyaan, jawaban inti, punchline | Kalimat narasumber yang paling tajam |
| Storytelling | Momen paling tegang, latar, konflik, titik balik, pelajaran | Satu kalimat dari puncak cerita |
| Jualan / brand | Masalah penonton, kenapa terjadi, solusi, bukti, CTA | Masalah yang langsung dikenali penonton |
| Voice-over di atas rekaman layar | Tujuan, langkah demi langkah, hasil | Hasil akhirnya diperlihatkan dulu |

### 6.2 Catatan per jenis

Alasan, bukan kuota (kepadatan dan jenis visual diputuskan per kalimat dengan `visual-thinking.md`).

- **Tutorial:** saat pembicara memperagakan sesuatu, peragaannya adalah visualnya; jangan ditutup. Rekaman layar asli untuk langkah di aplikasi.
- **Opini / edukasi:** setiap klaim faktual sebaiknya punya sumber yang terlihat; pendapat tetap di wajah.
- **Review:** produk di tangan pembicara dan halaman resmi untuk harga/spesifikasi lebih meyakinkan daripada foto stok.
- **Podcast / dua orang:** wajah dan reaksi adalah isinya, jadi panel atau overlay di ruang kosong lebih cocok daripada layar penuh; perubahan gambar datang dari cut antar orang dan punch-in.
- **Storytelling:** paling sedikit potongan; jeda adalah bagian dari cerita (rentang panjang diberi `quiet_ok` dengan alasan).
- **Jualan:** bukti (berita, ulasan, hasil kerja), produk, dan ajakan ke tempat nyata yang dituju.

### 6.3 Roll panjang menjadi beberapa video

Kalau roll berisi beberapa topik, tulis `roll_map.md` dulu, lalu usulkan pembagian (satu topik satu video) ke user sebelum mengedit. Tiap video memakai folder project sendiri dengan `raw/` yang sama.

### 6.4 Sumber 16:9 dan dua pembicara

- Satu orang di tengah frame horizontal: `normalize.sh` biasa (memotong bagian tengah).
- Dua orang kiri dan kanan: buat dua versi potong dari file yang sama, `CROP_X=0.2 SUFFIX=_L bash tools/normalize.sh` dan `CROP_X=0.8 SUFFIX=_R bash tools/normalize.sh`. Buka contact sheet keduanya dan atur `CROP_X` sampai tiap wajah berada di tengah. Transkrip salah satunya, salin `work/tx/<nama>_L.json` menjadi `<nama>_R.json`, lalu daftarkan sebagai dua klip (`A` dan `B`). Di `segments`, ganti klip setiap kali pembicara berganti, dengan `out` segmen satu sama dengan `in` segmen berikutnya.
- Whisper tidak memberi tahu siapa yang bicara. Tentukan dari isi kalimat (penanya dan penjawab) dan dari contact sheet (mulut siapa yang bergerak pada detik itu).
- Hasil akhir 16:9 (YouTube): kit ini dikunci untuk 9:16, termasuk tata letak `split`. Untuk 16:9, ubah ukuran di `normalize.sh` dan `Root.tsx` dan semua posisi di `Main.tsx` dan `Visuals.tsx`. Ini belum pernah diuji, jadi jalankan loop still lebih teliti.

### 6.5 Bahasa lain

Ganti kode bahasa di `transcribe.py` dan `verify_audio.py`. Label `SUMBER` di komponen `Screenshot` diganti sesuai bahasa video.
