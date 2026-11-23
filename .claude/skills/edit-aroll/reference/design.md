# Bagian 5. Standar desain

> Ini default netral dari guide. **Tidak ada satu gaya wajib**: warna, aksen, pola warna teks, dan font mengikuti brief, brand,
> dan footage tiap video (tulis pilihan + alasannya di `work/brief.md`, atur di `video/src/theme.ts`).
> Standar kualitas visual dari user ada di `style-notes.md`; kalau bertentangan dengan file ini, style-notes.md yang menang.

Ini default yang sudah dipakai. Ganti kalau user punya brand kit atau referensi, tetapi tetap satu sistem untuk seluruh video.

**Subtitle**

- Baris kecil: Plus Jakarta Sans 700, 56 px (50 px kalau ada kata besar di bawahnya), putih, bayangan gelap, huruf kecil semua. Kata yang belum diucapkan tampil 50% transparan, lalu penuh saat diucapkan.
- Kata besar: Playfair Display italic 800, 112 px, warna aksen, muncul dengan pegas kecil.
- Posisi: tengah, y 1270 sampai 1530 dari tinggi 1920. Maksimal 4 kata atau 24 karakter per potong, dipecah di jeda, akhir kalimat, dan setelah kata besar.
- Subtitle tetap tampil di atas insert. Di atas insert gelap ada gradasi gelap di bagian bawah supaya terbaca. Di atas insert terang, teksnya menjadi gelap dan gradasi dimatikan.
- Di layar terbagi, subtitle turun sampai 120 px mengikuti pembicara.

**Prinsip tampilan**

- **Bersih.** Sedikit elemen, banyak ruang kosong, perataan yang konsisten, satu sistem warna dan font dalam satu video.
- **Sesuai dunia nyata.** Logo resmi, screenshot asli, foto asli. Kalau yang dibahas sebuah aplikasi, tampilannya seperti aplikasi itu. Kalau situs berita, seperti situs itu. Kalau sebuah brand, pakai logo dan warna brand itu. Tidak ada satu gaya yang wajib: gaya visual mengikuti topik, brand, dan lingkungan nyata yang dibicarakan.
- **Tata letak berganti.** Pembicara penuh dengan overlay, layar terbagi, dan layar penuh dipakai bergantian sesuai isi kalimat. Jangan satu tata letak untuk semua scene.
- **Gerak seperlunya.** Elemen bergerak saat membantu memahami ucapan (kursor mengklik, batang tumbuh, poin muncul saat disebut). Sisanya diam atau bergerak sangat pelan.
- **Yang tidak dipakai:** UI karangan yang tidak menyerupai apa pun yang nyata, ikon generik sebagai pengganti logo asli, dekorasi yang tidak berhubungan dengan isi, dan banyak warna sekaligus.
- Warna dan font bawaan kit hanya titik awal yang netral. Ganti di `theme.ts` mengikuti brand atau suasana footage.

**Warna dan bentuk**

- Subtitle di atas footage: putih dengan satu warna kata besar (`ACCENT`, default kuning `#FFD60A`). Ganti dengan warna brand kalau ada. Di atas insert terang, subtitle otomatis berwarna `INK`.
- Diagram: abu netral untuk data biasa dan satu warna penekanan (default biru `#0A84FF`, atau warna brand lewat field `color`) untuk hal yang paling penting.
- Kartu screenshot: sudut 28 px, bayangan lembut, latar dari gambar yang sama yang diburamkan.
- Butiran halus (grain) di semua insert supaya foto dari sumber berbeda terasa satu keluarga.

**Gerak**

- Masuk insert: fade 7 frame dengan skala 1,06 ke 1. Keluar: fade 6 frame. Berantai: geser 12 frame.
- Foto dan screenshot selalu bergerak pelan (zoom 1,1 ke 1,22, atau scroll). Tidak ada gambar yang diam total.
- Pembicara: zoom 1,0 / 1,07 / 1,09 bergantian, ditambah drift pelan 3,5% per shot.
- Elemen kecil muncul dengan pegas (`sp`), tidak linear.
- Layar terbagi: panel turun dari atas dan pembicara turun bersamaan dengan pegas yang sama. Kembali dalam 12 frame.
- Yang dihindari: garis berdenyut atau berkedip terus-menerus di sekitar tombol, teks yang berputar atau memantul berlebihan, transisi yang berbeda di setiap insert, emoji besar, efek glitch, dan semua elemen dianimasikan sekaligus.
- Untuk menunjukkan aksi di layar (klik, DM, follow): kursor bergerak ke tombol dan mengklik sekali, tombol tertekan sedikit.

**Suara**

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

### 6.2 Kepadatan dan jenis visual

| Jenis | Insert layar penuh | Visual utama | Catatan |
|---|---|---|---|
| Tutorial | 30 sampai 45% | Chip langkah, rekaman layar, foto alat dan bahan | Saat pembicara memperagakan sesuatu, jangan ditutup |
| Opini / edukasi | 25 sampai 40% | Screenshot sumber, diagram angka | Setiap klaim faktual sebaiknya punya sumber yang terlihat |
| Review | 20 sampai 35% | Produk di tangan pembicara, klip close-up, screenshot halaman resmi untuk harga dan spesifikasi | Chip untuk kelebihan dan kekurangan |
| Podcast | 10 sampai 25% | Kata besar, panel `split` untuk orang atau hal yang disebut | Wajah dan ekspresi adalah isinya, jadi layar terbagi lebih cocok daripada layar penuh |
| Storytelling | 10 sampai 25% | Foto tempat dan waktu, sedikit sekali teks | Potongan paling sedikit. Jeda adalah bagian dari cerita |
| Jualan | 30 sampai 45% | Bukti (berita, profil, ulasan), produk, CTA dengan kursor | Kartu penutup berlogo |

### 6.3 Roll panjang menjadi beberapa video

Kalau roll berisi beberapa topik, tulis `roll_map.md` dulu, lalu usulkan pembagian (satu topik satu video) ke user sebelum mengedit. Tiap video memakai folder project sendiri dengan `raw/` yang sama.

### 6.4 Sumber 16:9 dan dua pembicara

- Satu orang di tengah frame horizontal: `normalize.sh` biasa (memotong bagian tengah).
- Dua orang kiri dan kanan: buat dua versi potong dari file yang sama, `CROP_X=0.2 SUFFIX=_L bash tools/normalize.sh` dan `CROP_X=0.8 SUFFIX=_R bash tools/normalize.sh`. Buka contact sheet keduanya dan atur `CROP_X` sampai tiap wajah berada di tengah. Transkrip salah satunya, salin `work/tx/<nama>_L.json` menjadi `<nama>_R.json`, lalu daftarkan sebagai dua klip (`A` dan `B`). Di `segments`, ganti klip setiap kali pembicara berganti, dengan `out` segmen satu sama dengan `in` segmen berikutnya.
- Whisper tidak memberi tahu siapa yang bicara. Tentukan dari isi kalimat (penanya dan penjawab) dan dari contact sheet (mulut siapa yang bergerak pada detik itu).
- Hasil akhir 16:9 (YouTube): kit ini dikunci untuk 9:16, termasuk tata letak `split`. Untuk 16:9, ubah ukuran di `normalize.sh` dan `Root.tsx` dan semua posisi di `Main.tsx` dan `Visuals.tsx`. Ini belum pernah diuji, jadi jalankan loop still lebih teliti.

### 6.5 Bahasa lain

Ganti kode bahasa di `transcribe.py` dan `verify_audio.py`. Label `SUMBER` di komponen `Screenshot` diganti sesuai bahasa video.
