# Editor Team

Kit untuk mengedit video A-roll (orang bicara) menjadi video pendek siap publish dengan Claude Code di cloud:
Whisper (transkrip per kata) + Remotion (render) + QA frame per frame, mengikuti skill `edit-aroll`.

## Cara pakai di chat baru
1. Buka chat Claude Code baru dengan repo ini terpasang.
2. Claude membaca `CLAUDE.md`, mengecek kit, dan menjalankan `setup/install.sh` kalau belum terpasang (5–15 menit).
3. Kirim link Google Drive (akses "siapa saja yang memiliki link") + brief.

Agar instalasi otomatis sebelum chat dimulai, tempel ini di Setup script environment:
`bash /home/user/editor-team/setup/install.sh || true`
(sesuaikan path dengan lokasi repo di container)

## Isi
- `CLAUDE.md`: peran lead/worker, aturan job, preferensi gaya, catatan environment cloud.
- `.claude/skills/edit-aroll/SKILL.md`: guide lengkap 11 tahap.
- `editkit/`: skrip, template Remotion, font, efek suara (sudah dites di cloud).
- `setup/install.sh`: instalasi idempoten.
