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
  Playfair Display, Poppins), `STYLE_NOTES.md`, `new_job.sh`.
- Python venv: faster-whisper 1.2.1 (model large-v3), av<17, numpy, pillow, playwright (versi = browser bawaan), gdown, yt-dlp.
- Node: Remotion + Chrome Headless Shell (versi dikunci di package-lock.json).
- Skill `edit-aroll` (global + di repo), folder job `/home/user/jobs` + registry worker.

## Isi
- `CLAUDE.md`: peran lead/worker, aturan job, preferensi gaya, catatan environment cloud.
- `.claude/skills/edit-aroll/SKILL.md`: guide lengkap 11 tahap.
- `editkit/`: skrip, template Remotion, font, efek suara (sudah dites di cloud).
- `setup/install.sh`: instalasi idempoten.
- `setup/cloud-setup-script.sh`: isi untuk Setup script environment.
- `LESSONS.md`: pelajaran per job (makin ke kanan makin improve).
- `editkit/STYLE_NOTES.md`: standar kualitas dari video referensi user.
