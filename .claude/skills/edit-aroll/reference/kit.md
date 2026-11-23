# Kit: skrip, project Remotion, arsitektur (Bagian 2 guide, tanpa blok kode)

Kode kit TIDAK ditempel di sini. Sumber kebenarannya adalah file di `/home/user/editkit/` (di repo: `editkit/`), yang
disalin ke setiap folder job. Kalau butuh detail sebuah skrip, baca filenya langsung; komentar di dalamnya menjelaskan tiap field.

## 2.1 Menyiapkan job (cloud)

```bash
bash /home/user/editkit/new_job.sh <job-id>     # membuat /home/user/jobs/<job-id>/ dan menyambungkannya ke kit bersama
cd /home/user/jobs/<job-id> && source .venv/bin/activate && python3 tools/doctor.py | tail -1    # harus RESULT: READY
```

- `.venv` dan `video/node_modules` adalah symlink ke kit bersama: jangan `pip install`/`npm install` per job, jangan jalankan `tools/setup.sh`.
- `tools/`, `video/src`, dan `video/public/sfx` adalah SALINAN: komponen visual baru ditulis di `video/src` job itu saja.
  Kalau sebuah komponen layak dipakai ulang, laporkan ke lead supaya dimasukkan ke kit di repo.
- `video/public/` harus berisi file asli, bukan symlink.
- Kalau `doctor.py` tidak READY: lapor ke lead (lead menjalankan `setup/install.sh` dari repo). Lihat `troubleshooting.md`.

Aturan menjalankan perintah:

- **Python selalu lewat venv.** Tiap panggilan shell bisa berupa shell baru, jadi awali setiap perintah Python dengan `source .venv/bin/activate && `. Contoh: `source .venv/bin/activate && python3 tools/sheet.py ...`. Skrip `.sh` mengaktifkan venv sendiri. Perintah `python3 ...` di guide ini ditulis tanpa awalan itu supaya ringkas.
- **Perintah lama dijalankan di background dengan log ke file.** Transkrip dan render bisa lebih dari 10 menit. Contoh: `nohup bash tools/render.sh v1 > work/render_v1.log 2>&1 &`, lalu cek berkala dengan `tail -c 400 work/render_v1.log`. Jangan menampilkan log render penuh ke percakapan.
- **Kalau ada yang gagal karena lingkungan** (modul tidak ditemukan, browser tidak bisa dibuka, tidak ada jaringan), jalankan `python3 tools/doctor.py` dulu, baru cari sebab lain.

Variabel lingkungan yang dikenali (semuanya opsional):

| Variabel | Bawaan | Fungsi |
|---|---|---|
| `WHISPER_MODEL` | `large-v3` | `medium` untuk mesin dengan RAM kecil. Akurasi waktu kata turun sedikit |
| `WHISPER_DEVICE`, `WHISPER_COMPUTE` | `cpu`, `int8` | `cuda` dan `float16` kalau ada GPU NVIDIA |
| `CONCURRENCY` | setengah jumlah core | Jumlah tab browser saat render. Kecilkan (`2`) kalau RAM habis |
| `CROP_X`, `SUFFIX` | `0.5`, kosong | Bagian lebar yang diambil dari sumber 16:9 (Bagian 6.4) |
| `HF_HOME` | `~/.cache/huggingface` | Lokasi model Whisper |
| `OPENAI_API_KEY` | tidak ada | Hanya kalau user ingin image generation lewat API. Jangan pernah ditulis ke file atau log |

### 2.2 Struktur folder

```
project/
  raw/                 klip asli dari user. Tidak pernah diubah
  work/                semua hasil berpikir: brief, transkrip, naskah, rencana visual, edit.json, gambar QA, STATE.md
    tx/                transkrip per klip (.json untuk mesin, .txt untuk dibaca)
    cand/              kandidat aset dari tools/stock.py
    ref/               video referensi gaya (kalau ada)
  tools/               skrip di 2.3
  video/               project Remotion
    src/               kode komposisi + data.json (dibuat otomatis, jangan diedit tangan)
    public/            klip yang sudah dinormalisasi + semua aset. Harus file asli, bukan symlink
      shots/ photos/ broll/ logos/ gen/ music/ sfx/
    out/               still dan master render
  out/                 file final untuk dikirim: final_v1.mp4, final_v2.mp4, ...
  .venv/               lingkungan Python (dibuat setup.sh)
```

Satu-satunya file yang diedit tangan untuk mengubah video adalah `work/edit.json` (keputusan edit dan tampilan) dan, kalau butuh visual baru, `video/src/Visuals.tsx`.

## 2.3 Isi kit

Baca `tools/build_timeline.py`, `video/src/Main.tsx`, dan `video/src/Visuals.tsx` sekali sebelum tahap 7. Komentar di dalamnya menjelaskan setiap field.

| File | Fungsi |
|---|---|
| `tools/doctor.py` | cek kesiapan mesin. Dijalankan sebelum edit pertama dan setiap kali ada yang gagal. |
| `tools/normalize.sh` | semua klip menjadi 1080x1920, 30 fps, suara dibersihkan dan diratakan. |
| `tools/transcribe.py` | transkrip per kata. |
| `tools/envelope.py` | mencari sunyi yang sebenarnya di sekitar titik potong. |
| `tools/build_timeline.py` | mengubah `work/edit.json` menjadi `video/src/data.json`. |
| `tools/make_sfx.sh` | empat efek suara pelan, dibuat dengan ffmpeg (tanpa unduhan, tanpa lisensi). |
| `tools/shot.py` | screenshot halaman asli, plus koordinat teks untuk stabilo dan klik. |
| `tools/stock.py` | mencari dan mengunduh foto, footage, dan logo asli tanpa API key. |
| `tools/sheet.py` | contact sheet untuk dilihat. |
| `tools/scene_check.py` | mencari perubahan gambar mendadak yang tidak direncanakan. |
| `tools/render.sh` | render penuh, encode untuk dikirim, cek teknis. |
| `tools/verify_audio.py` | transkrip ulang hasil render, kata di sekitar tiap sambungan. |
| `video/package.json` | versi paket yang dikunci. |
| `video/tsconfig.json` | konfigurasi TypeScript. |
| `video/stills.mjs` | render frame tunggal tanpa render video. |
| `video/src/index.ts` | titik masuk Remotion. |
| `video/src/Root.tsx` | komposisi `Edit`, 1080x1920. |
| `video/src/theme.ts` | membaca `theme` dari `data.json` (tampilan diputuskan per video di `work/edit.json`, `edit-json.md` 4.5) dan menyediakan token warna, font, dan gerak untuk komponen. Tidak berisi nilai tampilan. |
| `video/src/Main.tsx` | susunan layer: pembicara, panel layar terbagi, overlay, insert layar penuh, gradasi, efek suara, musik, subtitle. |
| `video/src/Visuals.tsx` | semua jenis visual dan satu pembungkus transisi. |
| `work/edit.example.json` | contoh `edit.json` lengkap (dijelaskan di Bagian 4). Blok kodenya ada di Bagian 4.1 dan ikut terekstrak. |
| `tools/install_fonts.sh` | (cloud) memasang font di `/home/user/editkit/fonts` sebagai font sistem. |

`video/src/theme.ts` di kit ini sudah versi cloud (font sistem, tanpa `loadFont`, nilai dari `theme` di `edit.json`). Jangan dikembalikan ke versi guide asli dan jangan menulis warna atau font di sana.

### 2.4 Kenapa arsitekturnya begini

- **Data terpisah dari tampilan.** `work/edit.json` berisi keputusan (potongan, teks, visual). `build_timeline.py` menghitung frame. Komponen React hanya menggambar apa yang ada di `data.json`. Revisi menjadi perubahan beberapa baris JSON, bukan menulis ulang kode.
- **Satu pembungkus transisi (`Insert`).** Semua insert layar penuh masuk dan keluar dengan cara yang sama, jadi tidak ada transisi yang berbeda-beda atau terlupa.
- **Zoom pembicara dihitung otomatis** dan hanya berubah di dua tempat yang tidak terlihat sebagai glitch: saat pembicara tertutup insert, atau tepat di sambungan potongan yang terlihat (punch-in).
- **Insert berurutan saling menyambung.** Kalau insert B mulai di frame yang sama dengan berakhirnya insert A, B menggeser masuk di atas A dan pembicara tidak muncul sekilas di antaranya.
- **Tiga tata letak dalam satu sistem.** Pembicara penuh dengan overlay kecil, insert layar penuh, dan layar terbagi (`split`: visual di atas, pembicara di bawah). Subtitle, zoom, dan efek suara menyesuaikan sendiri di ketiganya, sehingga tata letak bisa berganti dari scene ke scene tanpa kode baru.
- **Subtitle menyesuaikan latar.** Di atas insert terang (`light`), teks berubah gelap dan gradasi gelap di bawah dimatikan. Di layar terbagi, subtitle ikut turun supaya tetap di bawah dagu.

### 2.5 Perilaku tampilan bawaan kit (fakta, bukan standar gaya)

Yang dilakukan komponen sekarang, supaya rencana visual tidak mengandalkan sesuatu yang tidak ada (daftar teknik lengkap: `visual-craft.md` 9):

- **Subtitle:** pita di sekitar dua pertiga sampai empat perlima tinggi layar, tengah; baris kecil = frasa yang diucapkan (kata yang belum diucapkan
  setengah transparan), baris besar = kata bertanda `*`. Maksimal `sub_max_words`/`sub_max_chars` per potong. Di atas insert `light: true` teks
  berubah gelap dan penggelapan bawah dimatikan. Di layar terbagi, subtitle ikut turun.
- **Insert layar penuh** (`Insert`): masuk fade 7 frame dengan skala sedikit mengecil, keluar fade 6 frame; dua insert berantai = yang baru
  menggeser masuk 12 frame. Semua insert sama, jadi gerak masuk/keluar konsisten. Butiran halus di atas semua insert.
- **Foto** selalu didorong pelan (zoom kecil terus-menerus). **Screenshot** tampil sebagai kartu bersudut bulat dengan bayangan di atas versi buram
  gambarnya; stabilo menyapu 14 frame.
- **Overlay** (`title`, `bubbles`, `chips`) di sepertiga atas, muncul dengan pegas (pop), keluar fade 7 frame.
- **Split:** panel turun dari atas dan pembicara turun bersamaan (`shift`); `shift: 0` = pembicara tidak bergerak.
- **Zoom pembicara** berganti otomatis hanya saat tertutup insert atau di sambungan potongan yang terlihat (punch-in); tidak ada punch-in di kata pilihan.
- **Efek suara** otomatis: `whoosh` insert masuk, `swish` rantai dan split, `pop` overlay, `click` kursor.
