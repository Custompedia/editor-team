# Editor Team

Kit untuk mengedit video A-roll (orang bicara) menjadi video pendek siap publish dengan Claude Code di cloud:
Whisper (transkrip per kata) + Remotion (render) + QA frame per frame, mengikuti skill `edit-aroll`.

## Cara pakai di chat baru
1. Buka chat Claude Code baru dengan repo **Custompedia/editor-team** dipilih.
2. Ketik saja "cloud editor team" (atau langsung kirim link Drive + brief). Claude membaca `CLAUDE.md`, mengecek kit,
   dan menjalankan `setup/install.sh` sendiri kalau belum terpasang.
3. Kirim link Google Drive (akses "siapa saja yang memiliki link") + brief.

### Opsional: instal otomatis sebelum chat dimulai
Di pengaturan environment (menu environment di judul sesi -> Edit):
- tambahkan repo ini di bagian Repositories (kalau ditawarkan),
- tempel isi `setup/cloud-setup-script.sh` ke **Setup script**.
Kalau setup script tidak jalan / repo belum ter-clone saat itu, Claude tetap menginstal di awal chat (langkah 2).

## Yang terinstal (sama di setiap chat)
- Kit di `/home/user/editkit`: skrip edit-aroll, template Remotion 4.0.290, efek suara, font sistem (Plus Jakarta Sans,
  Playfair Display, Poppins), `new_job.sh`.
- Python venv: faster-whisper 1.2.1 (model large-v3), av<17, numpy, pillow, playwright (versi = browser bawaan), gdown, yt-dlp.
- Node: Remotion + Chrome Headless Shell (versi dikunci di package-lock.json).
- Skill `edit-aroll` dari repo (path stabil untuk worker: `/home/user/editkit/skill`), folder job `/home/user/jobs` + registry worker.

## Struktur repo
```
CLAUDE.md                      aturan untuk lead (pendek, dimuat di setiap chat)
LESSONS.md                     pelajaran per job (makin ke kanan makin improve)
.claude/skills/edit-aroll/
  SKILL.md                     peta kerja + aturan worker (dimuat hanya saat dipakai)
  reference/
    workflow.md                11 tahap lengkap dengan gate
    edit-json.md               format work/edit.json dan jenis event
    visual-thinking.md         kapan/apa/dari mana visual, aturan kode, look per video, uji diri
    visual-craft.md            berita, kapan memotong, posisi, timing, gerak, kemampuan kit
    design.md                  struktur cerita per jenis roll, suara, format
    kit.md                     menyiapkan job, struktur folder, daftar skrip
    troubleshooting.md         masalah cloud + masalah umum
editkit/                       skrip, template Remotion, font, efek suara, new_job.sh (satu-satunya tempat kode)
setup/install.sh               instalasi idempoten;  setup/cloud-setup-script.sh  untuk Setup script environment
docs/worker-brief-template.md  template instruksi worker
docs/review-tests.md           uji yang dijalankan lead sebelum hasil dikirim
docs/brands/                   profil per brand (ejaan, akun, permintaan pemilik)
docs/reference-studies/        arsip studi referensi dan benchmark
docs/GUIDE-original.md         arsip guide asli (tidak dibaca secara default)
```

Prinsip: satu skill dengan file referensi yang dibaca saat dibutuhkan (hemat token), kode hanya di `editkit/`
(tidak ditempel di dokumen), aturan lead di `CLAUDE.md`, aturan worker di skill.
