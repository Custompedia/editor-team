---
name: edit-aroll
description: Mengedit A-roll (video orang bicara / talking head, jenis konten apa pun) menjadi 1 video pendek siap publish di komputer lokal. Memilih take, memotong, subtitle per kata, visual dari sumber nyata yang mengikuti isi omongan, render dengan Remotion, lalu QA frame per frame. Pakai saat user memberi klip mentah dan minta diedit.
---

# Guide lengkap: edit A-roll menjadi 1 video siap publish

Dokumen ini adalah instruksi kerja untuk agent AI yang berjalan di komputer lokal (Claude Code, Codex, dan agent sejenis). Isinya semua yang dibutuhkan: daftar instalasi, cara pasang per agent, alat, kode, proses, dan pemeriksaan untuk mengedit video orang bicara menjadi satu video pendek yang rapi: cerita nyambung, subtitle per kata, visual yang searah dengan isi omongan, transisi tidak patah.

Berlaku untuk semua jenis roll: tutorial, opini/edukasi, review produk, podcast/interview, storytelling, jualan/brand, dan voice-over di atas rekaman layar. Topik, brand, warna, dan contoh di dokumen ini hanya contoh. Yang tetap adalah prosesnya.

Susunan dokumen:

| Bagian | Isi | Untuk |
|---|---|---|
| 0 | Pasang di komputer lokal: daftar kebutuhan, instalasi, pasang ke agent, izin | Manusia, sekali saja (agent membacanya saat ada yang gagal) |
| 1 | Cara berpikir dan aturan yang tidak boleh dilanggar | Agent |
| 2 | Kit: skrip, project Remotion, arsitektur | Agent |
| 3 | Alur kerja 11 tahap dengan gate | Agent |
| 4 | Referensi `work/edit.json` | Agent |
| 5 | Standar desain | Agent |
| 6 | Penyesuaian per jenis roll | Agent |
| 7 sampai 9 | Masalah umum, batasan, checklist dan format laporan | Agent |

---

## Bagian 0. Pasang di komputer lokal

### 0.1 Daftar lengkap kebutuhan

**Wajib**

| Kebutuhan | Versi | Dipakai untuk | Catatan |
|---|---|---|---|
| Agent AI dengan akses shell dan file | Claude Code, Codex (CLI, app, atau ekstensi IDE), atau sejenis | Menjalankan seluruh proses | Modelnya **harus bisa melihat gambar**. Semua QA dilakukan dengan membuka file .jpg |
| Sistem operasi | macOS, Linux, atau Windows lewat WSL2 (Ubuntu) | | Diuji di Ubuntu 22.04. macOS dan WSL2 memakai perintah yang sama, tetapi belum diuji langsung |
| ffmpeg dan ffprobe | 4.4 ke atas, build penuh (ada `libx264`) | Normalisasi, audio, frame, encode, efek suara | Diuji dengan 4.4.2 |
| Python | 3.9 ke atas, dengan `venv` dan `pip` | Skrip di `tools/` | Diuji dengan 3.10 |
| Paket Python | `faster-whisper`, `numpy`, `pillow`, `playwright` | Transkrip, analisis suara, contact sheet, screenshot dan pencarian stok | Dipasang `tools/setup.sh` ke `.venv/` |
| Node.js dan npm | Node 20 LTS (minimal 18) | Remotion | |
| Paket npm | `remotion`, `@remotion/cli`, `@remotion/bundler`, `@remotion/renderer`, `@remotion/google-fonts` semuanya 4.0.290; `react` dan `react-dom` 18.3.1; `typescript` **5.5.4**; `@types/react` 18.3.12 | Komposisi dan render | Versi dikunci di `video/package.json`. TypeScript yang lebih baru membuat bundler Remotion gagal |
| Chromium untuk Playwright | Terunduh lewat `playwright install chromium` | Screenshot halaman asli, cari foto dan footage stok tanpa API | Sekitar 700 MB |
| Chrome Headless Shell untuk Remotion | Terunduh lewat `npx remotion browser ensure` | Render still dan video | Sekitar 250 MB. Di Linux butuh pustaka sistem (lihat 0.2) |
| Model Whisper `large-v3` | Terunduh otomatis saat transkrip pertama | Transkrip per kata | Sekitar 3 GB, dari huggingface.co, sekali saja |
| Internet | | Setup, aset, screenshot, dan **saat render** (font diambil dari Google Fonts) | |
| Hardware | CPU 4 core (8 dianjurkan), RAM 8 GB (16 dianjurkan), disk kosong 10 GB | | GPU tidak wajib. Angka waktu ada di 0.7 |

**Opsional**

| Kebutuhan | Dipakai untuk | Catatan |
|---|---|---|
| `gdown` | Mengunduh klip dari folder Google Drive publik | Ikut dipasang `setup.sh` |
| `yt-dlp` | Mengunduh video referensi gaya | Ikut dipasang `setup.sh`. Kalau video diblokir wilayah atau privat, minta file mp4-nya ke user. Jangan diakali |
| Image generation | Gambar untuk benda yang tidak ada foto aslinya | Codex punya bawaan (`$imagegen`). Claude Code tidak punya: buat gambar di aplikasi lain dan taruh di `video/public/gen/`, atau lewati dan pakai foto stok atau diagram |
| Logo, warna, font brand | Kartu penutup dan konsistensi | Dari user |
| Musik latar | Bed musik pelan | File dari user di `video/public/music/`. Tanpa itu video tetap jadi, hanya dengan efek suara |
| GPU NVIDIA (CUDA) | Transkrip lebih cepat | `WHISPER_DEVICE=cuda WHISPER_COMPUTE=float16` |

**Tidak dibutuhkan:** API key Pexels atau stok lain (pencarian lewat browser), akun media sosial, aplikasi editor video (CapCut, Premiere, After Effects), dan layanan berbayar apa pun.

**Lisensi:** Remotion gratis untuk perorangan dan perusahaan sampai 3 orang. Perusahaan yang lebih besar memerlukan lisensi (remotion.dev/license). Foto dan video Pexels bebas dipakai. Gambar dari Wikimedia Commons dan Openverse punya lisensi masing-masing (dicetak oleh `tools/stock.py`), sebagian mewajibkan penyebutan nama pembuat.

### 0.2 Instal prasyarat (sekali per komputer)

**macOS** (dengan Homebrew):

```bash
brew install ffmpeg python@3.11 node@20 git
brew link --force --overwrite node@20
```

**Ubuntu, Debian, atau WSL2:**

```bash
sudo apt update
sudo apt install -y ffmpeg python3 python3-venv python3-pip git curl unzip
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt install -y nodejs
```

Pustaka sistem untuk browser (hanya Linux dan WSL2), dijalankan setelah `tools/setup.sh` membuat `.venv`:

```bash
sudo .venv/bin/python -m playwright install-deps chromium
```

Kalau perintah itu tidak bisa dipakai, pasang manual: `sudo apt install -y libnss3 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libgbm1 libasound2 libxrandr2 libxkbcommon0 libxfixes3 libxcomposite1 libxdamage1 libpango-1.0-0 libcairo2 libcups2` (di Ubuntu 24.04 ganti `libasound2` dengan `libasound2t64`).

**Windows:** pasang WSL2 (`wsl --install -d Ubuntu` di PowerShell sebagai admin), lalu kerjakan semuanya di dalam Ubuntu itu dengan perintah Ubuntu di atas, termasuk memasang agent-nya. Simpan project di dalam WSL (`~/...`), bukan di `/mnt/c`, supaya tidak lambat. Skrip `.sh` di kit ini tidak dibuat untuk PowerShell.

**Agent-nya:**

```bash
npm install -g @anthropic-ai/claude-code     # Claude Code, lalu jalankan: claude
npm install -g @openai/codex                 # Codex CLI, lalu jalankan: codex
```

### 0.3 Pasang guide ke agent

Guide ini dikirim dalam dua bentuk dengan isi yang sama:

- `edit-aroll-skill.zip`: paket skill. Berisi `edit-aroll/SKILL.md` (instruksi) dan `edit-aroll/kit/` (semua skrip dan project Remotion sebagai file). **Ini yang dianjurkan.**
- `GUIDE-edit-aroll.md`: satu file. Semua kode ada di dalamnya dan bisa diekstrak dengan satu perintah (Bagian 2.3). Untuk agent yang hanya bisa diberi satu file.

**Claude Code**

```bash
mkdir -p ~/.claude/skills && unzip -o edit-aroll-skill.zip -d ~/.claude/skills/      # berlaku di semua project
# atau hanya untuk satu project:  mkdir -p .claude/skills && unzip -o edit-aroll-skill.zip -d .claude/skills/
```

Hasilnya `~/.claude/skills/edit-aroll/SKILL.md`. Buka `claude` di folder project, lalu ketik `/edit-aroll` atau langsung kirim prompt di 0.6. Alternatif tanpa skill: simpan `GUIDE-edit-aroll.md` sebagai `CLAUDE.md` di folder project. Itu jalan, tetapi seluruh isinya selalu ikut dimuat, jadi lebih boros.

**Codex**

```bash
mkdir -p ~/.agents/skills && unzip -o edit-aroll-skill.zip -d ~/.agents/skills/      # berlaku di semua project
# atau hanya untuk satu project:  mkdir -p .agents/skills && unzip -o edit-aroll-skill.zip -d .agents/skills/
```

Hasilnya `~/.agents/skills/edit-aroll/SKILL.md`. Buka `codex` di folder project, lalu sebut `$edit-aroll` di prompt (atau pilih lewat `/skills`). **Jangan menempel isi guide ke `AGENTS.md`:** Codex hanya membaca 32 KiB pertama dari file itu, jadi guide ini akan terpotong. `AGENTS.md` cukup berisi penunjuk seperti di bawah.

**Agent lain** (Cursor, Gemini CLI, OpenCode, OpenClaw, Windsurf, dan sejenisnya): kalau agent itu mendukung format skill `SKILL.md`, pakai zip di folder skill-nya. Kalau tidak, taruh `GUIDE-edit-aroll.md` di folder project dan tulis penunjuk ini di file instruksi agent tersebut (`AGENTS.md`, `GEMINI.md`, aturan project, sesuai dokumentasinya):

```
Untuk mengedit video, baca GUIDE-edit-aroll.md sampai habis lalu ikuti tahap demi tahap.
Jangan lewati gate. Buka dan lihat setiap gambar QA sebelum lanjut.
```

### 0.4 Izin yang harus diberikan ke agent

- **Menjalankan perintah shell** `bash`, `python3`, `node`, `npx`, `npm`, `ffmpeg`, `ffprobe`, termasuk yang berjalan lama (transkrip dan render bisa lebih dari 10 menit).
- **Menulis file** di folder project.
- **Internet dari shell.** Di Codex, sandbox bawaan mematikan jaringan. Nyalakan di `~/.codex/config.toml`:

  ```toml
  [sandbox_workspace_write]
  network_access = true
  ```

  atau untuk sekali jalan: `codex -c 'sandbox_workspace_write.network_access=true'`. Di Claude Code, setujui permintaan izin Bash untuk perintah di atas (pilih yang tidak bertanya lagi supaya tidak berhenti di tengah).
- **Membuka gambar.** Claude Code memakai tool Read pada file gambar. Codex memakai `view_image` (aktif secara bawaan).

### 0.5 Siapkan folder project

```bash
mkdir -p ~/video-saya/raw && cd ~/video-saya
# salin klip mentah (.mp4 atau .mov) ke raw/, lalu buka agent di folder ini
```

Satu video satu folder. Setup pertama di folder baru (venv, paket npm, browser) memakan 5 sampai 15 menit dan dikerjakan agent lewat `bash tools/setup.sh`. Pemeriksaan kesiapan: `python3 tools/doctor.py` harus berakhir dengan `RESULT: READY`.

### 0.6 Prompt untuk memulai

```
Edit semua klip di raw/ menjadi 1 video sesuai skill edit-aroll. Kerjakan tahap demi tahap dan jangan lewati gate.
Jenis konten: <tutorial / opini / review / podcast / storytelling / jualan>
Platform dan durasi: <TikTok/Reels 9:16, 60 sampai 120 detik>
Brand / akun / logo: <nama, @akun, file logo kalau ada>
CTA: <apa yang harus dilakukan penonton di akhir>
Referensi gaya: <link atau file, opsional>
Klip: <sudah di raw/, atau link folder Google Drive publik>
```

Semua baris boleh kosong. Agent mengisi sendiri dengan asumsi yang masuk akal dan melaporkannya di akhir.

### 0.7 Waktu dan ukuran yang wajar

Terukur di mesin uji (8 core, 32 GB RAM, tanpa GPU):

| Pekerjaan | Waktu terukur |
|---|---|
| `tools/setup.sh` di folder baru | Sekitar 1 menit kalau unduhan sudah ada di cache. Pertama kali di komputer baru lebih lama: unduhan sekitar 1,5 GB (paket Python, Chromium, Chrome Headless Shell, paket npm) |
| Transkrip pertama | Tambahan unduhan model sekitar 3 GB, sekali saja |
| Normalisasi | 68 detik footage dalam 55 detik |
| Transkrip (`large-v3`, CPU) | 68 detik audio dalam 77 detik |
| 24 still | Sekitar 40 detik |
| Render penuh 1080x1920 | Video 64 detik dalam 5 menit, sudah termasuk encode dan cek teknis |
| Transkrip ulang hasil render | Sekitar 1 menit |

| Ruang disk | Ukuran |
|---|---|
| `.venv/` per project | Sekitar 700 MB |
| `video/node_modules/` per project (termasuk Chrome Headless Shell) | Sekitar 450 MB |
| Chromium Playwright (sekali per komputer, `~/.cache/ms-playwright`) | Sekitar 700 MB |
| Model Whisper (sekali per komputer, `~/.cache/huggingface`) | Sekitar 3 GB |
| File kerja dan hasil per video | 0,5 sampai 2 GB. File final 1 menit sekitar 40 MB |

Mesin dengan 4 core kira-kira dua kali lebih lama. Kalau RAM 8 GB: `WHISPER_MODEL=medium` saat transkrip dan `CONCURRENCY=2 bash tools/render.sh v1` saat render.

### 0.8 Environment acuan

Ini environment tempat guide dan kit ini dibuat dan diuji dari folder kosong sampai video jadi. Untuk hasil yang semirip mungkin, samakan sebisanya.

| Lapisan | Yang dipakai |
|---|---|
| Sistem | Ubuntu 22.04 (x86_64), 8 core, 32 GB RAM, tanpa GPU |
| Media | ffmpeg 4.4.2 |
| Python | 3.10.12 dengan faster-whisper 1.2.1, ctranslate2 4.9.0, numpy 2.2.6, pillow 12.3.0, playwright 1.65.2, gdown 6.5.2, yt-dlp 2026.10.21 |
| Node | 20.18.1 dengan remotion 4.0.290 (cli, bundler, renderer, google-fonts), react 18.3.1, typescript 5.5.4 |
| Browser | Chromium dari Playwright, Chrome Headless Shell dari Remotion |
| Model | Whisper `large-v3` lewat faster-whisper, CPU, int8 |
| Font | Plus Jakarta Sans dan Playfair Display dari Google Fonts |

`tools/setup.sh` memasang versi paket Python terbaru. Kalau suatu saat versi baru bermasalah, kunci ke versi di tabel: `pip install faster-whisper==1.2.1 numpy==2.2.6 pillow==12.3.0 playwright==1.65.2` lalu `python3 -m playwright install chromium`.

Kemampuan agent yang dipakai selama mengedit, dan padanannya:

| Kemampuan | Dipakai untuk | Claude Code | Codex |
|---|---|---|---|
| Menjalankan shell, termasuk proses lama di background | Semua skrip | Bash | shell |
| Membaca dan menulis file | `work/*.md`, `work/edit.json`, komponen visual | Read, Write, Edit | apply_patch |
| Membuka gambar | Semua QA (contact sheet, still, strip) | Read pada file gambar | `view_image` |
| Pencarian web | Mencari artikel, halaman resmi, profil publik untuk screenshot | WebSearch, WebFetch | web search (nyalakan kalau mati) |
| Browser tanpa tampilan | Screenshot halaman, cari stok | `tools/shot.py`, `tools/stock.py` (Playwright) | sama |
| Image generation | Gambar untuk benda tanpa foto asli (opsional) | tidak ada bawaan | `$imagegen` |

Kalau agent tidak punya pencarian web, minta URL sumbernya ke user. Kalau tidak bisa membuka gambar, guide ini tidak bisa dijalankan dengan benar.

---

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

---

## Bagian 2. Kit: skrip, project Remotion, arsitektur

### 2.1 Menyiapkan project (dikerjakan agent, sekali per folder)

1. **Pastikan berada di folder project** (folder yang berisi `raw/`). Semua perintah di guide ini dijalankan dari sini.
2. **Taruh kit di folder project** kalau `tools/build_timeline.py` belum ada. Caranya di 2.3.
3. **Jalankan setup:**

   ```bash
   mkdir -p work && bash tools/setup.sh > work/setup.log 2>&1 ; tail -n 40 work/setup.log
   ```

   Skrip ini membuat `.venv/`, memasang paket Python, mengunduh Chromium untuk Playwright, menjalankan `npm install` di `video/`, mengunduh Chrome Headless Shell untuk Remotion, membuat efek suara, lalu menjalankan `tools/doctor.py`.
4. **Baca hasil doctor.** `tools/doctor.py` memeriksa setiap alat yang dibutuhkan guide ini (ffmpeg dan fiturnya, Python dan modulnya, Node, versi Remotion dan TypeScript, kedua browser, file kit, efek suara, disk, RAM, model Whisper, jaringan). Harus berakhir dengan `RESULT: READY`. Setiap baris `FAIL` menyebut perbaikannya. Yang butuh `sudo` atau instalasi sistem (ffmpeg, Node, pustaka browser di Linux) tidak bisa dikerjakan agent sendiri: sampaikan perintahnya ke user (Bagian 0.2) dan tunggu. Baris `WARN` boleh dilanjutkan kalau memang tidak dipakai.

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

Satu-satunya file yang diedit tangan untuk mengubah video adalah `work/edit.json` (keputusan edit) dan, kalau butuh visual baru, `video/src/Visuals.tsx`.

### 2.3 Isi kit

Semua file kit ada di dokumen ini. Tiap file diawali penanda `<!-- file: path -->` lalu satu blok kode. **Jangan mengetik ulang isinya.** Ekstrak semuanya dengan satu perintah dari folder project. Argumennya adalah path file guide ini (ganti kalau disimpan dengan nama lain, misalnya `CLAUDE.md` atau `~/.agents/skills/edit-aroll/SKILL.md`):

```bash
python3 - "GUIDE-edit-aroll.md" <<'PY'
import re, sys, os
t = open(sys.argv[1], encoding="utf-8").read()
n = 0
for path, body in re.findall(r"<!-- file: (\S+) -->\n```[a-z]*\n(.*?)\n```", t, flags=re.S):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(body + "\n"); n += 1
print(n, "files written")
PY
chmod +x tools/*.sh
```

Harus tercetak `22 files written`. Setelah itu lanjut ke langkah 3 di 2.1. Kalau perlu mengubah perilaku kit, ubah file hasil ekstrak, bukan dokumen ini.

Baca `tools/build_timeline.py`, `video/src/Main.tsx`, dan `video/src/Visuals.tsx` sekali sebelum tahap 7. Komentar di dalamnya menjelaskan setiap field.

**`tools/setup.sh`**: setup sekali per folder: venv, paket, browser, efek suara, lalu doctor.

<!-- file: tools/setup.sh -->
```bash
#!/usr/bin/env bash
# One-time setup of a project folder (safe to run again). Needs: python3 (3.9+), node (18+, 20 recommended), ffmpeg.
# Usage: bash tools/setup.sh
set -euo pipefail
for t in python3 node npm ffmpeg ffprobe; do command -v $t >/dev/null || { echo "MISSING: $t  -> install it first (see the guide, 'Yang harus terpasang')"; exit 1; }; done
mkdir -p raw work/tx video/public/sfx video/out out
[ -d .venv ] || python3 -m venv .venv
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; else . .venv/Scripts/activate; fi
python3 -m pip install --quiet --upgrade pip
python3 -m pip install --quiet faster-whisper numpy pillow playwright gdown yt-dlp
if [ "$(uname -s)" = "Linux" ] && command -v sudo >/dev/null && sudo -n true 2>/dev/null; then python3 -m playwright install --with-deps chromium; else python3 -m playwright install chromium; fi
(cd video && npm install --no-audit --no-fund && npx remotion browser ensure)
bash tools/make_sfx.sh
python3 tools/doctor.py
```

**`tools/doctor.py`**: cek kesiapan mesin. Dijalankan sebelum edit pertama dan setiap kali ada yang gagal.

<!-- file: tools/doctor.py -->
```python
"""Preflight: is this machine ready to edit? Run it before the first edit and whenever something fails.
Usage: python3 tools/doctor.py        (run from the project folder, with the venv active if you use one)
Prints OK / WARN / FAIL per requirement with the fix. Exit code 1 if anything is FAIL."""
import sys, os, shutil, subprocess, json, importlib, platform
bad = 0
def say(level, name, msg=""):
    global bad
    bad += level == "FAIL"
    print(f"[{level:<4}] {name}" + (f": {msg}" if msg else ""))
def run(cmd, **kw):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=180, shell=isinstance(cmd, str), **kw)
    except Exception as ex: return subprocess.CompletedProcess(cmd, 1, "", str(ex))

print(f"system: {platform.system()} {platform.machine()}, python {platform.python_version()}, {os.cpu_count()} cpu threads")
# --- python
say("OK" if sys.version_info >= (3, 9) else "FAIL", "python >= 3.9", platform.python_version())
if os.path.isdir(".venv") and sys.prefix == sys.base_prefix:
    say("WARN", "venv", ".venv exists but is not active: prefix commands with `source .venv/bin/activate &&`")
for mod, pipname, need in [("faster_whisper", "faster-whisper", True), ("numpy", "numpy", True), ("PIL", "pillow", True),
                           ("playwright", "playwright", True), ("gdown", "gdown", False), ("yt_dlp", "yt-dlp", False)]:
    try:
        m = importlib.import_module(mod); say("OK", f"python module {pipname}", getattr(m, "__version__", ""))
    except Exception:
        say("FAIL" if need else "WARN", f"python module {pipname}", f"pip install {pipname}" + ("" if need else "  (optional: Google Drive / reference video download)"))
# --- ffmpeg
for tool in ("ffmpeg", "ffprobe"):
    say("OK" if shutil.which(tool) else "FAIL", tool, "" if shutil.which(tool) else "install ffmpeg (apt install ffmpeg / brew install ffmpeg / winget install Gyan.FFmpeg)")
if shutil.which("ffmpeg"):
    enc, flt = run(["ffmpeg", "-hide_banner", "-encoders"]).stdout, run(["ffmpeg", "-hide_banner", "-filters"]).stdout
    for name, hay in [("libx264", enc), ("aac", enc), ("loudnorm", flt), ("afftdn", flt), ("acompressor", flt), ("anoisesrc", flt), ("aevalsrc", flt)]:
        if name not in hay: say("FAIL", f"ffmpeg feature {name}", "this ffmpeg build is too minimal: install a full build")
    say("OK", "ffmpeg version", run(["ffmpeg", "-version"]).stdout.split("\n")[0][:60])
# --- node / remotion
node = run(["node", "-v"]).stdout.strip()
major = int(node[1:].split(".")[0]) if node.startswith("v") else 0
say("OK" if major >= 18 else "FAIL", "node >= 18 (20 recommended)", node or "not found: install Node 20 LTS")
say("OK" if shutil.which("npx") else "FAIL", "npx", "" if shutil.which("npx") else "comes with Node")
def ver(pkg):
    try: return json.load(open(f"video/node_modules/{pkg}/package.json"))["version"]
    except Exception: return None
if not os.path.exists("video/package.json"): say("FAIL", "video/ project", "kit files are missing: copy or extract the kit first")
elif not ver("remotion"): say("FAIL", "video/node_modules", "run: cd video && npm install")
else:
    say("OK" if ver("remotion") == "4.0.290" else "WARN", "remotion", f"{ver('remotion')} (tested with 4.0.290)")
    say("OK" if ver("typescript") == "5.5.4" else "FAIL", "typescript", f"{ver('typescript')} (must be 5.5.4: newer versions break Remotion's bundler)")
    r = run("npx remotion browser ensure", cwd="video")
    say("OK" if r.returncode == 0 else "FAIL", "remotion browser (Chrome Headless Shell)", "" if r.returncode == 0 else (r.stdout + r.stderr)[-300:] + "  Linux: install the shared libraries listed in the guide")
# --- playwright chromium
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto("about:blank"); b.close()
    say("OK", "playwright chromium launches")
except Exception as ex:
    say("FAIL", "playwright chromium", "run: python3 -m playwright install chromium   (Linux: add --with-deps)  | " + str(ex).split("\n")[0][:120])
# --- kit files, sfx, folders
need = ["tools/normalize.sh", "tools/transcribe.py", "tools/envelope.py", "tools/build_timeline.py", "tools/make_sfx.sh", "tools/shot.py", "tools/stock.py",
        "tools/sheet.py", "tools/scene_check.py", "tools/render.sh", "tools/verify_audio.py", "video/stills.mjs", "video/tsconfig.json",
        "video/src/index.ts", "video/src/Root.tsx", "video/src/theme.ts", "video/src/Main.tsx", "video/src/Visuals.tsx"]
missing = [f for f in need if not os.path.exists(f)]
say("FAIL" if missing else "OK", "kit files", "missing: " + ", ".join(missing) if missing else f"{len(need)} files")
sfx = [f for f in ("whoosh", "swish", "pop", "click") if not os.path.exists(f"video/public/sfx/{f}.wav")]
say("FAIL" if sfx else "OK", "sound effects", "run: bash tools/make_sfx.sh" if sfx else "4 files")
clips = [f for f in os.listdir("raw")] if os.path.isdir("raw") else []
say("OK" if clips else "WARN", "raw/ clips", f"{len(clips)} files" if clips else "put the source clips in raw/ (never edit them)")
# --- resources
free = shutil.disk_usage(".").free / 1e9
say("OK" if free > 10 else "WARN" if free > 5 else "FAIL", "free disk", f"{free:.0f} GB (need ~5 GB once for model + browsers + node_modules, plus ~2 GB per video)")
try:
    ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 1e9
    say("OK" if ram >= 15 else "WARN" if ram >= 7 else "FAIL", "RAM", f"{ram:.0f} GB" + ("" if ram >= 15 else "  (use WHISPER_MODEL=medium and CONCURRENCY=2 tools/render.sh)"))
except Exception: say("WARN", "RAM", "could not read; 16 GB recommended, 8 GB minimum")
hub = os.path.join(os.environ.get("HF_HOME", os.path.expanduser("~/.cache/huggingface")), "hub")
model = os.environ.get("WHISPER_MODEL", "large-v3")
cached = os.path.isdir(hub) and any(f"faster-whisper-{model}" in d for d in os.listdir(hub))
say("OK" if cached else "WARN", f"whisper model {model}", "cached" if cached else "not downloaded yet: the first transcription downloads ~3 GB (needs internet, once)")
# --- network (assets, fonts, model)
import urllib.request
for name, url in [("internet: fonts.googleapis.com", "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans"), ("internet: huggingface.co", "https://huggingface.co"), ("internet: pexels.com", "https://www.pexels.com/robots.txt")]:
    try: urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=15); say("OK", name)
    except Exception as ex: say("WARN", name, f"{str(ex)[:80]}  (agent sandbox without network? enable network access for the agent)")
print("\nRESULT:", "NOT READY: fix every FAIL above, then run this again" if bad else "READY")
sys.exit(1 if bad else 0)
```

**`tools/normalize.sh`**: semua klip menjadi 1080x1920, 30 fps, suara dibersihkan dan diratakan.

<!-- file: tools/normalize.sh -->
```bash
#!/usr/bin/env bash
# Normalize every raw clip: upright 1080x1920, 30 fps, short GOP (fast frame seeking), cleaned + leveled voice.
# Usage: tools/normalize.sh            (reads raw/*.mp4|mov, writes video/public/<name>.mp4)
# Wide (16:9) source: CROP_X=0..1 picks which part of the width to keep (0 = left, 0.5 = centre, 1 = right) and
# SUFFIX names the result, e.g.  CROP_X=0.2 SUFFIX=_L tools/normalize.sh ; CROP_X=0.8 SUFFIX=_R tools/normalize.sh
set -euo pipefail
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; elif [ -f .venv/Scripts/activate ]; then . .venv/Scripts/activate; fi
X=${CROP_X:-0.5}; SUFFIX=${SUFFIX:-}
mkdir -p video/public
for f in raw/*.mp4 raw/*.mov raw/*.MP4 raw/*.MOV; do
  [ -e "$f" ] || continue
  name=$(basename "${f%.*}")$SUFFIX
  # ffmpeg applies rotation metadata automatically; scale+crop fills 9:16 without distortion.
  ffmpeg -loglevel error -y -i "$f" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920:(iw-1080)*$X:0,eq=contrast=1.06:saturation=1.12:brightness=0.01,unsharp=5:5:0.5" \
    -r 30 -c:v libx264 -preset fast -crf 15 -g 10 -pix_fmt yuv420p \
    -af "highpass=f=90,afftdn=nr=10:nf=-28,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=9" \
    -ar 48000 -c:a aac -b:a 192k "video/public/$name.mp4"
  ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of csv=p=0 "video/public/$name.mp4" | tr '\n' ' '; echo " <- $name"
done
```

**`tools/transcribe.py`**: transkrip per kata.

<!-- file: tools/transcribe.py -->
```python
"""Word-level transcription of every clip.
Usage: python3 tools/transcribe.py [language] ["domain vocabulary, brand names, ..."]
Reads video/public/*.mp4 (normalized clips). Writes work/tx/<clip>.json (list of {w,s,e,p})
and work/tx/<clip>.txt (readable: word index, text, start time, gaps, low-confidence marks)."""
import sys, glob, json, os, subprocess
from faster_whisper import WhisperModel
lang = sys.argv[1] if len(sys.argv) > 1 else "id"
prompt = sys.argv[2] if len(sys.argv) > 2 else None
os.makedirs("work/tx", exist_ok=True)
# large-v3 on CPU is the tested default. Weak machine: WHISPER_MODEL=medium. NVIDIA GPU: WHISPER_DEVICE=cuda WHISPER_COMPUTE=float16
model = WhisperModel(os.environ.get("WHISPER_MODEL", "large-v3"), device=os.environ.get("WHISPER_DEVICE", "cpu"),
                     compute_type=os.environ.get("WHISPER_COMPUTE", "int8"), cpu_threads=os.cpu_count() or 4)
for f in sorted(glob.glob("video/public/*.mp4")):
    name = os.path.splitext(os.path.basename(f))[0]
    wav = f"work/tx/{name}.wav"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    # vad_filter off + no conditioning: keeps stumbles and repeated takes visible instead of "cleaning" them away
    segs, _ = model.transcribe(wav, language=lang, word_timestamps=True, vad_filter=False, beam_size=5,
                               condition_on_previous_text=False, initial_prompt=prompt)
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 2)}
             for s in segs for w in s.words]
    json.dump(words, open(f"work/tx/{name}.json", "w"), ensure_ascii=False)
    lines, line = [], []
    for i, w in enumerate(words):
        if i and w["s"] - words[i - 1]["e"] > 0.35:
            lines.append(" ".join(line)); line = []
            lines.append("    -- gap %.2fs --" % (w["s"] - words[i - 1]["e"]))
        line.append("%d:%s%s[%.2f]" % (i, w["w"], "?" if w["p"] < 0.5 else "", w["s"]))
    lines.append(" ".join(line) + "   (end %.2f)" % (words[-1]["e"] if words else 0))
    open(f"work/tx/{name}.txt", "w").write("\n".join(lines) + "\n")
    print(name, len(words), "words")
```

**`tools/envelope.py`**: mencari sunyi yang sebenarnya di sekitar titik potong.

<!-- file: tools/envelope.py -->
```python
"""Loudness envelope around a candidate cut point, to place cuts in real silence.
Usage: python3 tools/envelope.py <clip name> <t0> <t1> [window_sec=0.01]
Prints time:dB pairs. Speech is roughly > -25 dB, pauses < -35 dB (after normalize.sh)."""
import sys, subprocess, numpy as np
name, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
win = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f"video/public/{name}.mp4", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
t, out = t0, []
while t < t1:
    s = x[int(t * 16000):int((t + win) * 16000)]
    out.append("%.2f:%d" % (t, 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-6)))
    t += win
print(" ".join(out))
```

**`tools/build_timeline.py`**: mengubah `work/edit.json` menjadi `video/src/data.json`.

<!-- file: tools/build_timeline.py -->
```python
"""Turn the edit decisions (work/edit.json) + word timestamps (work/tx/*.json) into video/src/data.json.
Everything in the video is anchored to WORDS, never to hand-typed frame numbers, so moving a cut
re-times every subtitle, visual and sound effect automatically.
Usage: python3 tools/build_timeline.py"""
import json, re, sys
E = json.load(open("work/edit.json"))
FPS = E.get("fps", 30)
FULL_TYPES = set(E.get("full_types", ["photo", "clip", "screenshot", "custom", "outro"]))  # cover the whole frame
W = {k: json.load(open(f"work/tx/{v}.json")) for k, v in E["clips"].items()}

# 1) manual word-timing fixes: {"A": {"39": [15.08, 15.60]}}
for k, fixes in E.get("timing", {}).items():
    for i, (s, e) in fixes.items():
        W[k][int(i)]["s"], W[k][int(i)]["e"] = s, e

# 2) segments -> output frames
segs, f = [], 0
for s in E["segments"]:
    d = round((s["out"] - s["in"]) * FPS)
    segs.append({"k": s["clip"], "src": E["clips"][s["clip"]] + ".mp4", "in": s["in"], "out": s["out"], "start": f, "dur": d})
    f += d
total = f + E.get("outro_frames", 0)

def T(k, t):
    """source time in clip k -> output frame (time inside a removed part snaps to the next kept segment)"""
    for s in segs:
        if s["k"] == k and s["in"] - 0.05 <= t <= s["out"] + 0.05:
            return s["start"] + round((t - s["in"]) * FPS)
    for s in segs:
        if s["k"] == k and t < s["in"]:
            return s["start"]
    raise SystemExit(f"time {t} of clip {k} is after the last kept segment")

def anchor(a):
    """int = absolute frame | "end" = last frame | [clip, wordIndex, frameOffset=0, side="s"|"e"]"""
    if isinstance(a, int): return a
    if a == "end": return total
    k, i = a[0], a[1]
    off = a[2] if len(a) > 2 else 0
    side = a[3] if len(a) > 3 else "s"
    return max(0, min(total, T(k, W[k][i][side]) + off))

# 3) words that survive the cut, with text overrides: {"A": {"39": "*NamaBrand", "40": ""}}
#    "*word" = emphasised keyword (big style), "" = hide the word (stumble that stays in the audio)
#    "script": {"A": [{"from": 0, "text": "Nah, aku tuh ... *harganya *berapa?"}]} rewrites a run of words in one go:
#    one token per Whisper word starting at index "from"; "_" hides a word; "~" is a space inside one token.
words = []
for k in E["clips"]:
    ov = dict(E.get("text", {}).get(k, {}))
    for block in E.get("script", {}).get(k, []):
        toks = block["text"].split()
        if block["from"] + len(toks) > len(W[k]): raise SystemExit(f"script block for clip {k} from {block['from']} has {len(toks)} tokens but only {len(W[k]) - block['from']} words remain")
        for n, tok in enumerate(toks):
            ov.setdefault(str(block["from"] + n), "" if tok == "_" else tok.replace("~", " "))
    for i, w in enumerate(W[k]):
        mid = (w["s"] + w["e"]) / 2      # a word belongs to the segment that contains its middle
        seg = next((s for s in segs if s["k"] == k and s["in"] <= mid < s["out"]), None)
        t = ov.get(str(i), w["w"])
        if seg is None:
            if t and any(s["k"] == k and w["s"] < s["out"] and w["e"] > s["in"] for s in segs):
                print(f"WARNING: word {k}{i} '{w['w']}' ({w['s']}-{w['e']}) only partly inside a segment -> no subtitle. If it is audible, fix its time in \"timing\"; if not, ignore.")
            continue
        if not t: continue
        words.append({"k": k, "t": t, "f": T(k, max(w["s"], seg["in"])), "e": T(k, min(w["e"], seg["out"]))})
words.sort(key=lambda w: w["f"])

# 4) subtitle chunks: short phrases; a trailing run of *emphasised* words becomes the big line
MAXC, MAXW = E.get("sub_max_chars", 24), E.get("sub_max_words", 4)
subs, cur = [], []
def flush():
    global cur
    if not cur: return
    j = len(cur)
    while j > 0 and cur[j - 1]["t"].startswith("*"): j -= 1
    strip = lambda ws: [{"t": w["t"].replace("*", ""), "f": w["f"]} for w in ws]
    subs.append({"f": cur[0]["f"], "t": cur[-1]["e"], "small": strip(cur[:j]), "big": strip(cur[j:])})
    cur = []
for w in words:
    if cur:
        prev = cur[-1]; ln = sum(len(x["t"]) for x in cur) + len(cur)
        if (w["f"] - prev["e"] > 9                                   # pause
                or (prev["t"].startswith("*") and not w["t"].startswith("*"))  # keyword ends the chunk
                or re.search(r'[.?!"”]$', prev["t"])                # sentence end
                or ln + len(w["t"]) > MAXC or len(cur) >= MAXW
                or (prev["t"].endswith(",") and ln > 12)
                or w["k"] != prev["k"] or w["f"] < prev["f"]):
            flush()
    cur.append(w)
flush()
for a, b in zip(subs, subs[1:]):
    a["t"] = min(max(a["t"] + 4, a["f"] + 8), b["f"])     # hold a little, never overlap the next chunk
if subs: subs[-1]["t"] = min(total, subs[-1]["t"] + 10)

# 5) events (visuals) -> frames
events = []
for ev in E.get("events", []):
    e = dict(ev); e["f"], e["t"] = anchor(ev["start"]), anchor(ev["end"])
    del e["start"], e["end"]
    for key, val in list(e.items()):                 # any other "*_at" field is an anchor too (e.g. "tap_at")
        if key.endswith("_at"): e[key] = anchor(val)
    for it in e.get("items", []):
        for key in list(it):
            if key == "at": it["f"] = anchor(it.pop("at"))
            elif key.endswith("_at"): it[key] = anchor(it[key])
    if e["type"] == "custom": e.setdefault("light", True)   # diagrams are bright by default -> dark subtitles over them
    if e["t"] - e["f"] < 20: print("WARNING: event shorter than 20 frames:", e["type"], e["f"], e["t"])
    events.append(e)
events.sort(key=lambda e: e["f"])
fulls = [e for e in events if e["type"] in FULL_TYPES]
for a, b in zip(fulls, fulls[1:]):
    if b["f"] < a["t"]: raise SystemExit(f"full-screen events overlap: {a['type']}@{a['f']}-{a['t']} and {b['type']}@{b['f']}")
    if 0 < b["f"] - a["t"] < 24: print(f"WARNING: speaker visible only {b['f'] - a['t']} frames between two inserts at {a['t']}: chain them (same frame) or widen the gap")
# split panels (visual on top, speaker below): may touch a full-screen insert or another split, never overlap one
splits = [e for e in events if e["type"] == "split"]
for e in splits:
    if e.get("shift", 300) > e.get("h", 760): raise SystemExit(f"split@{e['f']}: shift must be <= h, or black shows above the speaker")
    for x in fulls + splits:
        if x is not e and x["f"] < e["t"] and e["f"] < x["t"]: raise SystemExit(f"split@{e['f']}-{e['t']} overlaps {x['type']}@{x['f']}-{x['t']}: make them touch (same frame) or separate them")
    e["pre"] = any(x["t"] == e["f"] for x in fulls); e["post"] = any(x["f"] == e["t"] for x in fulls)
    e["chainPrev"] = any(x["t"] == e["f"] for x in splits); e["chainNext"] = any(x["f"] == e["t"] for x in splits)
    for x in events:
        if x["type"] not in FULL_TYPES and x["type"] != "split" and x["f"] < e["t"] and e["f"] < x["t"]:
            print(f"WARNING: overlay {x['type']}@{x['f']} is on screen during split@{e['f']}: both use the top of the frame, move one")

# 6) speaker zoom levels ("shots"): change ONLY where it cannot look like a glitch:
#    - while a full-screen insert hides the speaker, or
#    - exactly on an exposed jump cut (a segment join with no insert over it) = classic punch-in
groups = []
for e in fulls:
    if groups and groups[-1][-1]["t"] == e["f"]: groups[-1].append(e)
    else: groups.append([e])
hidden = [g[0]["f"] + 12 for g in groups if g[-1]["t"] < total]
joins = [s["start"] for s in segs[1:] if not any(e["f"] + 7 <= s["start"] < e["t"] - 6 for e in fulls)]
shots, z = [], 1.0
for c in sorted(set([0] + hidden + joins)):
    if c: z = 1.0 if z > 1.03 else (1.09 if c in joins else 1.07)
    shots.append({"f": c, "z": z})

# 7) sound effects
sfx = []
for e in fulls:
    chained = any(x["t"] == e["f"] for x in fulls)
    sfx.append({"f": e["f"] + (2 if chained else 0), "k": "swish" if chained else "whoosh"})
    if "click_at" in e: sfx.append({"f": e["click_at"], "k": "click"})
for e in events:
    if e["type"] == "split":
        sfx.append({"f": e["f"], "k": "swish"})
        if "click_at" in e: sfx.append({"f": e["click_at"], "k": "click"})
    elif e["type"] not in FULL_TYPES:
        sfx += [{"f": it["f"], "k": "pop"} for it in e.get("items", []) if "f" in it] or [{"f": e["f"], "k": "pop"}]

json.dump({"fps": FPS, "total": total, "segs": segs, "framing": E.get("framing", {}), "subs": subs, "events": events,
           "fullTypes": sorted(FULL_TYPES), "shots": shots, "sfx": sfx, "keepCase": E.get("keep_case", []), "music": E.get("music")},
          open("video/src/data.json", "w"), ensure_ascii=False, indent=1)

# report: read it every time
covered = sum(e["t"] - e["f"] for e in fulls)
print(f"total {total} frames = {total / FPS:.1f}s | {len(segs)} segments | {len(subs)} subtitle chunks | full-screen inserts cover {100 * covered / total:.0f}%"
      f" | split panels {100 * sum(e['t'] - e['f'] for e in splits) / total:.0f}%")
print("exposed jump cuts (speaker visible across a cut) at frames:", joins or "none")
for e in events: print(f"  {e['type']:<11}{e['f']:>5} -> {e['t']:<5} {(e['t'] - e['f']) / FPS:.1f}s")
for s in subs: print(f"  {s['f']:>5} {' '.join(w['t'] for w in s['small'])} | {' '.join(w['t'] for w in s['big'])}")
```

**`tools/make_sfx.sh`**: empat efek suara pelan, dibuat dengan ffmpeg (tanpa unduhan, tanpa lisensi).

<!-- file: tools/make_sfx.sh -->
```bash
#!/usr/bin/env bash
# Synthesize four quiet sound effects with ffmpeg (no downloads, no licences): video/public/sfx/*.wav
set -euo pipefail
mkdir -p video/public/sfx && cd video/public/sfx
ffmpeg -loglevel error -y -f lavfi -i "anoisesrc=d=0.55:c=pink:a=0.5:s=7" -af "bandpass=f=900:w=700,lowpass=f=3500,volume=30dB,afade=t=in:d=0.26:curve=qsin,afade=t=out:st=0.26:d=0.29:curve=qsin" -ar 48000 -ac 2 whoosh.wav
ffmpeg -loglevel error -y -f lavfi -i "anoisesrc=d=0.3:c=pink:a=0.5:s=3" -af "bandpass=f=1800:w=1200,volume=32dB,afade=t=in:d=0.1:curve=qsin,afade=t=out:st=0.1:d=0.2:curve=qsin" -ar 48000 -ac 2 swish.wav
ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='0.5*sin(2*PI*(520+1400*t)*t)*exp(-28*t)':d=0.16:s=48000" -af "afade=t=in:d=0.004,volume=-14dB" -ac 2 pop.wav
ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='(0.6*sin(2*PI*2200*t)+0.4*sin(2*PI*900*t))*exp(-140*t)':d=0.06:s=48000" -af "afade=t=in:d=0.001,volume=-13dB" -ac 2 click.wav
# every effect must peak around -18..-24 dB: far below the voice (-1.5 dB peak), audible but never distracting
for f in *.wav; do printf "%s " "$f"; ffmpeg -hide_banner -i "$f" -af volumedetect -f null - 2>&1 | grep -o "max_volume.*"; done
```

**`tools/shot.py`**: screenshot halaman asli, plus koordinat teks untuk stabilo dan klik.

<!-- file: tools/shot.py -->
```python
"""Screenshot a REAL web page (article, profile, search result, product page) as a phone-width PNG for a "screenshot" insert.
Usage: python3 tools/shot.py <url> <out.png> [--height 2000] [--find "text to locate" ...] [--desktop]
Output is 1080 px wide (540 css px at 2x; --desktop = 1280 css px at 1x). Prints the PNG size (-> img_w, img_h)
and, for every --find text, its box in IMAGE pixels (-> "highlights" or "click" in work/edit.json).
Public pages only: never log in, never bypass a private page. Login/cookie pop-ups are removed before the shot."""
import sys, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--height", type=int, default=2000); ap.add_argument("--find", action="append", default=[]); ap.add_argument("--desktop", action="store_true")
a = ap.parse_args()
cssw, scale = (1280, 1) if a.desktop else (540, 2)
UA = None if a.desktop else "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_context(viewport={"width": cssw, "height": a.height // scale}, device_scale_factor=scale, user_agent=UA, locale="id-ID").new_page()
    page.goto(a.url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(3500)
    # remove overlays that cover the content: dialogs, cookie bars, sticky ad/login banners
    page.evaluate("""() => { for (const el of document.querySelectorAll('[role=dialog],[aria-modal=true],[id*=cookie i],[class*=cookie i],[class*=consent i],[class*=popup i],[class*=modal i],[class*=overlay i]')) el.remove();
        document.documentElement.style.overflow = 'auto'; document.body.style.overflow = 'auto'; }""")
    page.wait_for_timeout(400)
    page.screenshot(path=a.out)
    print(f"{a.out}: img_w={cssw * scale} img_h={a.height // scale * scale}")
    for t in a.find:
        loc, box = page.get_by_text(t), None
        for i in range(min(loc.count(), 20)):          # first match that is actually visible inside the shot
            bb = loc.nth(i).bounding_box()
            if bb and bb["width"] > 0 and 0 <= bb["y"] < a.height // scale: box = bb; break
        print(f'  "{t}":', {"x": round(box["x"] * scale), "y": round(box["y"] * scale), "w": round(box["width"] * scale), "h": round(box["height"] * scale)}
              if box else "NOT FOUND in the shot (check the spelling; it may be inside an image or below --height)")
    b.close()
```

**`tools/stock.py`**: mencari dan mengunduh foto, footage, dan logo asli tanpa API key.

<!-- file: tools/stock.py -->
```python
"""Find and download REAL stock photos / footage / logos without any API key.
Usage:
  python3 tools/stock.py photo "hands counting cash" [-n 6] [--landscape]   Pexels photos   -> work/cand/<slug>/*.jpg
  python3 tools/stock.py video "barista pouring coffee" [-n 4]               Pexels videos   -> work/cand/<slug>/*.mp4
  python3 tools/stock.py commons "TikTok logo" [-n 6]                        Wikimedia Commons (logos, people, places, objects)
  python3 tools/stock.py open "night market jakarta" [-n 6]                  Openverse (CC-licensed photos, fallback)
Prints one line per file with its source URL and licence (copy the ones you use into work/visual_plan.md), then
writes a contact sheet work/cand/<slug>.jpg: OPEN IT and pick. Search in English, name the concrete object.
Pexels is searched through a headless browser (public search page). If it shows a bot check, use `open`/`commons`,
or let the user download the files by hand into video/public/."""
import sys, os, re, json, time, argparse, subprocess, urllib.request, urllib.parse, urllib.error
ap = argparse.ArgumentParser()
ap.add_argument("kind", choices=["photo", "video", "commons", "open"]); ap.add_argument("query")
ap.add_argument("-n", type=int, default=6); ap.add_argument("--landscape", action="store_true")
a = ap.parse_args()
slug = re.sub(r"[^a-z0-9]+", "-", a.query.lower()).strip("-")
out = f"work/cand/{slug}"; os.makedirs(out, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
BOT_UA = "aroll-edit-kit/1.0 (local video editing; python-urllib)"   # Wikimedia/Openverse want an honest, descriptive agent
def get(url, path=None):
    ua = UA if "pexels.com" in url else BOT_UA
    for attempt in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": ua}), timeout=60).read(); break
        except urllib.error.HTTPError as ex:
            if ex.code != 429 or attempt == 2: raise
            time.sleep(4 * (attempt + 1))       # rate limited: wait and retry
    time.sleep(0.6)
    if path: open(path, "wb").write(data)
    return data
def pexels_page(url):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
        pg = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 2400}).new_page()
        pg.goto(url, wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
        html = pg.content(); b.close()
    return html
files = []
q = urllib.parse.quote(a.query)
if a.kind == "photo":
    html = pexels_page(f"https://www.pexels.com/search/{q}/?orientation={'landscape' if a.landscape else 'portrait'}")
    for pid in list(dict.fromkeys(re.findall(r"images\.pexels\.com/photos/(\d+)/", html)))[:a.n]:
        path = f"{out}/pexels_{pid}.jpg"
        try: get(f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=1600", path)
        except Exception as ex: print("  skip", pid, ex); continue
        files.append(path); print(f"{path}  <- https://www.pexels.com/photo/{pid}/  (Pexels licence: free to use)")
elif a.kind == "video":
    html = pexels_page(f"https://www.pexels.com/search/videos/{q}/?orientation={'landscape' if a.landscape else 'portrait'}")
    urls = {}
    for u in re.findall(r"https://videos\.pexels\.com/video-files/\d+/[^\"'\\ ]+?\.mp4", html):
        urls.setdefault(re.search(r"video-files/(\d+)/", u).group(1), u)
    for vid, u in list(urls.items())[:a.n]:
        path = f"{out}/pexels_{vid}.mp4"
        try: get(u, path)
        except Exception as ex: print("  skip", vid, ex); continue
        files.append(path); print(f"{path}  <- https://www.pexels.com/video/{vid}/  (Pexels licence: free to use)")
elif a.kind == "commons":
    # Wikimedia throttles originals and odd thumbnail sizes (HTTP 429): ask for the standard sizes 1280 / 960 / 500 only.
    cand = {}
    for w in (1280, 960, 500):
        api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6"
               f"&gsrlimit={a.n}&gsrsearch={q}&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth={w}")
        for p in json.loads(get(api)).get("query", {}).get("pages", {}).values():
            ii = p["imageinfo"][0]
            c = cand.setdefault(p["title"], {"ii": ii, "tries": []})
            if ii.get("thumburl") and ii["thumburl"] not in c["tries"]: c["tries"].append(ii["thumburl"])
    for title, c in cand.items():
        ii = c["ii"]; name = re.sub(r"[^A-Za-z0-9.]+", "_", title[5:]); svg = name.lower().endswith(".svg")
        path = f"{out}/{name}.png" if svg else f"{out}/{name}"; ok = False   # an SVG is fetched as its PNG render (transparent)
        for src in c["tries"]:
            try: get(src, path); ok = True; break
            except Exception as ex: err = ex
        if not ok: print("  skip", name, err); continue
        if svg:                                                               # plus the vector itself when the server allows it
            try: get(ii["url"], f"{out}/{name}")
            except Exception: pass
        files.append(path); print(f"{path}  <- {ii['descriptionurl']}  ({ii['extmetadata'].get('LicenseShortName', {}).get('value', '?')})")
else:
    api = f"https://api.openverse.org/v1/images/?q={q}&page_size={a.n * 2}"
    for r in json.loads(get(api))["results"]:
        if len(files) >= a.n: break
        if max(r.get("width") or 0, r.get("height") or 0) < 900: continue
        path = f"{out}/openverse_{r['id'][:8]}.jpg"
        try: get(r["url"], path)
        except Exception as ex: print("  skip", r["id"][:8], ex); continue
        files.append(path); print(f"{path}  <- {r['foreign_landing_url']}  (CC {r['license']} {r.get('license_version', '')}, by {r.get('creator')})")
if not files: sys.exit("nothing found: try other English keywords, another source (open / commons), or ask the user for the asset")
if a.kind == "video":     # one mid frame per video so the candidates can be looked at
    thumbs = []
    for f in files:
        t = f[:-4] + ".jpg"; subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "1", "-i", f, "-frames:v", "1", t]); thumbs.append(t)
    files = [t for t in thumbs if os.path.exists(t)]
imgs = [f for f in files if not f.lower().endswith(".svg")]
if imgs: subprocess.run([sys.executable, "tools/sheet.py", "assets", f"work/cand/{slug}.jpg"] + imgs)
```

**`tools/sheet.py`**: contact sheet untuk dilihat.

<!-- file: tools/sheet.py -->
```python
"""Contact sheets you can LOOK at (the agent must open the resulting jpg files).
  python3 tools/sheet.py stills <out.jpg> [frame ...]     grid of video/out/f*.jpg (all, or the listed frames)
  python3 tools/sheet.py video <file.mp4> <prefix> [every_sec=1]   one frame per N seconds -> <prefix>_0.jpg, _1.jpg ...
  python3 tools/sheet.py strips <file.mp4> <prefix>       12 consecutive frames around EVERY transition in data.json
  python3 tools/sheet.py assets <out.jpg> <img> [img ...]  grid of candidate images with their file names"""
import sys, glob, json, os, subprocess
from PIL import Image, ImageDraw

def grid(items, out, cols, W, H):
    """items: list of (PIL image, label)"""
    rows = (len(items) + cols - 1) // cols
    sh = Image.new("RGB", (cols * W, rows * H), "black"); d = ImageDraw.Draw(sh)
    for i, (im, label) in enumerate(items):
        if im.mode in ("RGBA", "LA", "P"):                      # transparent logos: show them on light grey, not black
            im = im.convert("RGBA"); bg = Image.new("RGBA", im.size, (225, 225, 228, 255)); bg.alpha_composite(im); im = bg
        im = im.convert("RGB"); im.thumbnail((W, H))
        x, y = (i % cols) * W, (i // cols) * H
        sh.paste(im, (x, y)); d.rectangle([x, y, x + 8 * len(label) + 8, y + 16], fill="black"); d.text((x + 4, y + 2), label, fill="yellow")
    sh.save(out, quality=85); print(out, sh.size)

def grab(video, frame, fps=30, W=216, H=384):
    tmp = "/tmp/_frame.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "%.4f" % (frame / fps + 0.5 / fps), "-i", video, "-frames:v", "1",
                    "-vf", f"scale={W}:{H}", "-q:v", "4", tmp], check=True)
    return Image.open(tmp).copy()

mode = sys.argv[1]
if mode == "stills":
    fs = sorted(glob.glob("video/out/f*.jpg")) if len(sys.argv) < 4 else ["video/out/f%05d.jpg" % int(x) for x in sys.argv[3:]]
    grid([(Image.open(f), os.path.basename(f)[1:6]) for f in fs], sys.argv[2], min(6, len(fs)), 360, 640)
elif mode == "assets":
    grid([(Image.open(f), os.path.basename(f)[:26]) for f in sys.argv[3:]], sys.argv[2], 6, 300, 460)
elif mode == "video":
    video, prefix = sys.argv[2], sys.argv[3]; every = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video], capture_output=True, text=True).stdout)
    times = [i * every for i in range(int(dur / every) + 1)]
    for part in range(0, len(times), 44):
        grid([(grab(video, round(t * 30), W=270, H=480), "%.0fs" % t) for t in times[part:part + 44]], f"{prefix}_{part // 44}.jpg", 11, 270, 480)
elif mode == "strips":
    video, prefix = sys.argv[2], sys.argv[3]
    d = json.load(open("video/src/data.json"))
    fulls = [e for e in d["events"] if e["type"] in d["fullTypes"]]
    points = [("in  " + e["type"], e["f"]) for e in fulls] + [("out " + e["type"], e["t"]) for e in fulls if e["t"] < d["total"]]
    points += [(n + " split", e[k]) for e in d["events"] if e["type"] == "split" for n, k in (("in ", "f"), ("out", "t")) if e[k] < d["total"]]
    points += [("join", s["start"]) for s in d["segs"][1:]] + [("zoom", s["f"]) for s in d["shots"][1:]]
    points = sorted(set(points), key=lambda p: p[1])
    rows = [[(grab(video, f), f"{name} {f}") for f in range(max(0, c - 5), min(d["total"], c + 7))] for name, c in points]
    for part in range(0, len(rows), 8):
        grid([x for r in rows[part:part + 8] for x in (r + [(Image.new("RGB", (216, 384)), "")] * (12 - len(r)))], f"{prefix}_{part // 8}.jpg", 12, 216, 384)
```

**`tools/scene_check.py`**: mencari perubahan gambar mendadak yang tidak direncanakan.

<!-- file: tools/scene_check.py -->
```python
"""Find every abrupt picture change in the rendered video and compare with the planned ones.
Any hard change that is NOT explained by the plan is a bug (flash, popped zoom, wrong frame).
Usage: python3 tools/scene_check.py <file.mp4> [threshold=0.08]"""
import sys, re, json, subprocess
video = sys.argv[1]; th = sys.argv[2] if len(sys.argv) > 2 else "0.08"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vf",
                f"scale=270:480,select='gt(scene,{th})',metadata=print:file=/tmp/_scene.txt", "-an", "-f", "null", "-"], check=True)
found = [(round(float(a) * 30), float(b)) for a, b in re.findall(r"pts_time:([\d.]+)\n.*?scene_score=([\d.]+)", open("/tmp/_scene.txt").read())]
d = json.load(open("video/src/data.json"))
fulls = [e for e in d["events"] if e["type"] in d["fullTypes"]]
planned = {}
for e in fulls: planned[e["f"]] = "insert in: " + e["type"]; planned[e["t"]] = "insert out: " + e["type"]
for s in d["segs"][1:]: planned[s["start"]] = "segment join"
for e in d["events"]:
    for it in e.get("items", []): planned[it.get("f", -99)] = "overlay item"
    planned.setdefault(e["f"], "event start: " + e["type"])
    if e["type"] == "split": planned.setdefault(e["t"], "split out")
bad = 0
for f, score in found:
    why = next((planned[p] for p in planned if -8 <= f - p <= 14), None)   # fade-outs start ~7 frames before, slides last up to ~14 frames after
    if why is None: bad += 1
    print(f"frame {f:>5} ({f / 30:6.2f}s) score {score:.2f}  {why or '<<< UNEXPLAINED: look at this frame'}")
print(f"{len(found)} hard changes, {bad} unexplained")
```

**`tools/render.sh`**: render penuh, encode untuk dikirim, cek teknis.

<!-- file: tools/render.sh -->
```bash
#!/usr/bin/env bash
# Full render + delivery encode + technical checks.
# Usage: tools/render.sh v1            1080x1920
#        tools/render.sh v1 1.3334     1440x2560 (sharper upload; ~1.8x slower). Any Remotion --scale value works.
# CONCURRENCY=2 tools/render.sh v1     fewer parallel browser tabs on a machine with little RAM
set -euo pipefail
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; elif [ -f .venv/Scripts/activate ]; then . .venv/Scripts/activate; fi
V=${1:-v1}; SCALE=${2:-1}
mkdir -p out work
python3 tools/build_timeline.py > work/timeline_$V.log
(cd video && npx tsc --noEmit -p . && npx remotion render src/index.ts Edit out/master_$V.mp4 --codec=h264 --crf=16 --audio-bitrate=256k --color-space=bt709 --scale=$SCALE ${CONCURRENCY:+--concurrency=$CONCURRENCY} --log=error)
# Delivery file. --color-space=bt709 above makes Remotion write limited-range yuv420p tagged BT.709 (its default is
# full-range yuvj420p, which some phones and upload pipelines show washed out or too dark). Keep those tags here.
MAXRATE=$(awk "BEGIN{printf \"%d\", 6000 * $SCALE * $SCALE}")
ffmpeg -loglevel error -y -i video/out/master_$V.mp4 -c:v libx264 -preset medium -crf 22 -maxrate ${MAXRATE}k -bufsize $((MAXRATE * 2))k \
  -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart out/final_$V.mp4
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate,pix_fmt,color_range,color_space -of default=nw=1 out/final_$V.mp4
ffmpeg -hide_banner -i out/final_$V.mp4 -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input Integrated|Input True Peak"
# expected: h264 + aac, 1080x1920 (or scaled), 30/1, yuv420p, tv, bt709, loudness about -14..-16 LUFS, true peak below -1 dBTP
```

**`tools/verify_audio.py`**: transkrip ulang hasil render, kata di sekitar tiap sambungan.

<!-- file: tools/verify_audio.py -->
```python
"""Re-transcribe the RENDERED video and show the words around every cut, to prove no word was clipped or doubled.
Usage: python3 tools/verify_audio.py <file.mp4> [language=id]"""
import sys, json, subprocess, os
from faster_whisper import WhisperModel
video = sys.argv[1]; lang = sys.argv[2] if len(sys.argv) > 2 else "id"
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", "/tmp/_final.wav"], check=True)
m = WhisperModel(os.environ.get("WHISPER_MODEL", "large-v3"), device=os.environ.get("WHISPER_DEVICE", "cpu"),
                 compute_type=os.environ.get("WHISPER_COMPUTE", "int8"), cpu_threads=os.cpu_count() or 4)
segs, _ = m.transcribe("/tmp/_final.wav", language=lang, word_timestamps=True, beam_size=5, condition_on_previous_text=False)
ws = [(w.word.strip(), w.start) for s in segs for w in s.words]
d = json.load(open("video/src/data.json"))
print("FULL TEXT:\n" + " ".join(w for w, _ in ws) + "\n")
for s in d["segs"][1:]:
    j = s["start"] / d["fps"]
    print("cut at %.2fs: " % j + " ".join(w for w, t in ws if j - 2.2 < t < j) + "  ||  " + " ".join(w for w, t in ws if j <= t < j + 2.2))
```

**`video/package.json`**: versi paket yang dikunci.

<!-- file: video/package.json -->
```json
{
  "name": "aroll-edit",
  "private": true,
  "type": "commonjs",
  "dependencies": {
    "@remotion/bundler": "4.0.290",
    "@remotion/cli": "4.0.290",
    "@remotion/google-fonts": "4.0.290",
    "@remotion/renderer": "4.0.290",
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "remotion": "4.0.290"
  },
  "devDependencies": {
    "@types/react": "18.3.12",
    "typescript": "5.5.4"
  }
}
```

**`video/tsconfig.json`**: konfigurasi TypeScript.

<!-- file: video/tsconfig.json -->
```json
{"compilerOptions":{"target":"ES2020","module":"ESNext","moduleResolution":"node","jsx":"react-jsx","strict":false,"esModuleInterop":true,"resolveJsonModule":true,"skipLibCheck":true,"lib":["DOM","ES2020"]},"include":["src"]}
```

**`video/stills.mjs`**: render frame tunggal tanpa render video.

<!-- file: video/stills.mjs -->
```js
// Render single frames WITHOUT rendering the video: the fast design loop.
// Usage: cd video && node stills.mjs 120 480 900 ...   -> video/out/f00120.jpg ...
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition, openBrowser} from '@remotion/renderer';
import path from 'path';
import fs from 'fs';
const frames = process.argv.slice(2).map(Number);
fs.mkdirSync('out', {recursive: true});
const serveUrl = await bundle({entryPoint: path.resolve('src/index.ts'), publicDir: path.resolve('public')});
const composition = await selectComposition({serveUrl, id: 'Edit'});
const browser = await openBrowser('chrome');
for (const f of frames) {
  await renderStill({composition, serveUrl, frame: f, output: `out/f${String(f).padStart(5, '0')}.jpg`, imageFormat: 'jpeg', jpegQuality: 80, puppeteerInstance: browser, scale: 0.5});
}
await browser.close({silent: true});
console.log('rendered', frames.length, 'stills');
```

**`video/src/index.ts`**: titik masuk Remotion.

<!-- file: video/src/index.ts -->
```ts
import {registerRoot} from 'remotion';
import {Root} from './Root';
registerRoot(Root);
```

**`video/src/Root.tsx`**: komposisi `Edit`, 1080x1920.

<!-- file: video/src/Root.tsx -->
```tsx
import {Composition} from 'remotion';
import {Main} from './Main';
import data from './data.json';
export const Root = () => (
  <Composition id="Edit" component={Main} width={1080} height={1920} fps={(data as any).fps} durationInFrames={(data as any).total} />
);
```

**`video/src/theme.ts`**: satu tempat untuk font, warna, dan gerak. Ganti di sini kalau user punya brand kit.

<!-- file: video/src/theme.ts -->
```tsx
import {loadFont as loadSans} from '@remotion/google-fonts/PlusJakartaSans';
import {loadFont as loadSerif} from '@remotion/google-fonts/PlayfairDisplay';
import {Easing, spring} from 'remotion';
// One place for the look. Swap fonts/colours here when the user has a brand kit.
export const SANS = loadSans('normal', {weights: ['500', '600', '700', '800'], subsets: ['latin']}).fontFamily;
export const SERIF = loadSerif('italic', {weights: ['700', '800'], subsets: ['latin']}).fontFamily;
export const ACCENT = '#FFD60A';                 // keyword colour on dark footage; use the brand colour when there is one
export const LIGHT = '#F5F5F7', INK = '#1D1D1F';  // bright, clean default for diagrams and panels
export const FPS = 30;
export const cl = {extrapolateLeft: 'clamp' as const, extrapolateRight: 'clamp' as const};
export const ease = Easing.bezier(0.2, 0.8, 0.2, 1);
export const sp = (frame: number, at: number, cfg: any = {damping: 15, stiffness: 180, mass: 0.7}) =>
  spring({frame: frame - at, fps: FPS, config: cfg});
```

**`video/src/Main.tsx`**: susunan layer: pembicara, panel layar terbagi, overlay, insert layar penuh, gradasi, efek suara, musik, subtitle.

<!-- file: video/src/Main.tsx -->
```tsx
import React from 'react';
import {AbsoluteFill, Audio, Easing, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import raw from './data.json';
import {Insert, Overlay, SplitPanel} from './Visuals';
import {SANS, SERIF, ACCENT, INK, FPS, cl, sp} from './theme';
const data = raw as any;
const isFull = (e: any) => data.fullTypes.includes(e.type);
const fulls = data.events.filter(isFull);
const splits = data.events.filter((e: any) => e.type === 'split');
const overs = data.events.filter((e: any) => !isFull(e) && e.type !== 'split');
const chainedAfter = (e: any) => fulls.some((x: any) => x.f === e.t); // another insert starts exactly when this one ends
const chainedBefore = (e: any) => fulls.some((x: any) => x.t === e.f);

/* Split layout: a visual panel on top, the speaker pushed down below it. 0 = normal layout, 1 = fully split.
   The move is animated unless a full-screen insert (pre/post) or another split (chainPrev/chainNext) hides or continues it. */
export const splitP = (e: any, frame: number) => {
  const inn = e.pre || e.chainPrev ? (frame >= e.f - (e.pre ? 10 : 0) ? 1 : 0) : sp(frame, e.f, {damping: 20, stiffness: 150, mass: 0.8});
  const out = e.post || e.chainNext ? (frame < e.t + 10 ? 1 : 0) : interpolate(frame, [e.t - 12, e.t], [1, 0], {...cl, easing: Easing.inOut(Easing.cubic)});   // stays under whatever takes over
  return Math.max(0, Math.min(inn, out));
};
const speakerShift = (frame: number) => Math.max(0, ...splits.map((e: any) => splitP(e, frame) * (e.shift ?? 300)));
/* 0..1: how much of the frame is a BRIGHT full-screen insert ("light": true) right now -> dark subtitles, no bottom darkening */
const lightK = (frame: number) => Math.max(0, ...fulls.filter((e: any) => e.light).map((e: any) => Math.min(
  chainedBefore(e) ? interpolate(frame, [e.f, e.f + 12], [0, 1], cl) : interpolate(frame, [e.f, e.f + 7], [0, 1], cl),
  chainedAfter(e) ? interpolate(frame, [e.t, e.t + 12], [1, 0], cl) : interpolate(frame, [e.t - 6, e.t], [1, 0], cl))));

/* Layer 1: the speaker (A-roll), cut into segments, with zoom levels and a slow drift */
const Speaker: React.FC = () => {
  const frame = useCurrentFrame();
  // skip decoding video while an insert fully hides it (keep it during the insert's fade in/out)
  const covered = fulls.some((e: any) => frame >= e.f + (chainedBefore(e) ? 0 : 9) && frame < e.t - (chainedAfter(e) ? 0 : 7));
  let si = 0;
  data.shots.forEach((s: any, i: number) => { if (frame >= s.f) si = i; });
  const shot = data.shots[si];
  const next = data.shots[si + 1]?.f ?? data.total;
  const drift = interpolate(frame, [shot.f, next], [0, 0.035], cl);
  const down = speakerShift(frame);
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {data.segs.map((s: any, i: number) => {
        const fr = data.framing[s.k] || {}; // per-clip reframing so the face sits in the same place in every clip
        const z = (fr.scale || 1) * (shot.z + drift);
        return (
          <Sequence key={i} from={s.start} durationInFrames={s.dur} layout="none">
            <Audio src={staticFile(s.src)} startFrom={Math.round(s.in * FPS)} endAt={Math.round(s.in * FPS) + s.dur}
              volume={(f) => interpolate(f, [0, 2, s.dur - 2, s.dur], [0, 1, 1, 0], cl)} />
            {!covered && (
              <AbsoluteFill style={{transform: `translate(${fr.x || 0}px, ${(fr.y || 0) + down}px) scale(${z})`, transformOrigin: '50% 45%'}}>
                <OffthreadVideo muted src={staticFile(s.src)} startFrom={Math.round(s.in * FPS)} style={{width: 1080, height: 1920}} />
              </AbsoluteFill>
            )}
          </Sequence>
        );
      })}
      <AbsoluteFill style={{background: 'radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.38) 100%)'}} />
    </AbsoluteFill>
  );
};

/* Top layer: subtitles. Small line = spoken phrase (word-by-word highlight), big line = keyword */
const keep = new RegExp('^(' + ['Rp', ...data.keepCase].join('|') + ')');
const clean = (t: string) => {
  const s = t.replace(/["“”]/g, '').replace(/[.,]+$/g, '');
  return keep.test(s) ? s : s.toLowerCase();
};
const shadow = '0 0 14px rgba(0,0,0,0.85), 0 3px 6px rgba(0,0,0,0.9), 0 0 2px rgba(0,0,0,1)';
const Subs: React.FC = () => {
  const frame = useCurrentFrame();
  const c = data.subs.find((s: any) => frame >= s.f && frame < s.t);
  if (!c) return null;
  const inn = interpolate(frame - c.f, [0, 4], [0, 1], cl);
  const ink = lightK(frame) > 0.5;                                  // on a bright insert: dark text, soft white glow
  const sh = ink ? '0 0 16px rgba(255,255,255,0.95)' : shadow;
  const top = 1270 + Math.min(120, speakerShift(frame) * 0.4);      // in split layout the speaker sits lower: keep the text under the chin
  return (
    <AbsoluteFill style={{top, height: 260, justifyContent: 'center', alignItems: 'center', flexDirection: 'column', opacity: 0.25 + 0.75 * inn, transform: `translateY(${(1 - inn) * 10}px)`}}>
      {c.small.length > 0 && (
        <div style={{fontFamily: SANS, fontWeight: 700, fontSize: c.big.length ? 50 : 56, color: ink ? INK : '#fff', textShadow: sh, letterSpacing: -0.5, textAlign: 'center', padding: '0 70px', lineHeight: 1.15}}>
          {c.small.map((w: any, i: number) => (
            <span key={i} style={{opacity: frame >= w.f - 1 ? 1 : 0.5, marginRight: 13, display: 'inline-block'}}>{clean(w.t)}</span>
          ))}
        </div>
      )}
      {c.big.length > 0 && (
        <div style={{fontFamily: SERIF, fontStyle: 'italic', fontWeight: 800, fontSize: 112, color: ink ? INK : ACCENT, textShadow: sh, lineHeight: 1.0, marginTop: c.small.length ? 2 : 0, textAlign: 'center', letterSpacing: -1.5, whiteSpace: 'nowrap', fontVariantNumeric: 'lining-nums'}}>
          {c.big.map((w: any, i: number) => {
            const p = sp(frame, w.f - 2, {damping: 14, stiffness: 220, mass: 0.6});
            return <span key={i} style={{display: 'inline-block', marginRight: 22, opacity: Math.min(1, p * 1.5), transform: `scale(${0.7 + 0.3 * p})`}}>{clean(w.t)}</span>;
          })}
        </div>
      )}
    </AbsoluteFill>
  );
};

export const Main: React.FC = () => {
  const frame = useCurrentFrame();
  return (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <Speaker />
    {overs.map((e: any, i: number) => (
      <Sequence key={'o' + i} from={e.f} durationInFrames={e.t - e.f} layout="none"><Overlay e={e} /></Sequence>
    ))}
    {splits.map((e: any, i: number) => (
      // mounted a little longer when a full-screen insert or the next split panel takes over, so nothing pops
      <Sequence key={'p' + i} from={e.f - (e.pre ? 10 : 0)} durationInFrames={e.t - e.f + (e.pre ? 10 : 0) + (e.post || e.chainNext ? 10 : 0)} layout="none">
        <SplitPanel e={e} p={splitP} />
      </Sequence>
    ))}
    {fulls.map((e: any, i: number) => (
      // a chained insert stays mounted 14 extra frames, underneath the next one sliding in
      <Sequence key={'f' + i} from={e.f} durationInFrames={e.t - e.f + (chainedAfter(e) ? 14 : 0)} layout="none">
        <Insert e={e} chained={chainedAfter(e)} prevChained={chainedBefore(e)} />
      </Sequence>
    ))}
    {/* darken top and bottom so white text stays readable on any footage or insert */}
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0) 14%, rgba(0,0,0,0) 56%, rgba(0,0,0,0.62) 74%, rgba(0,0,0,0.72) 100%)', opacity: 1 - lightK(frame)}} />
    {data.sfx.map((x: any, i: number) => (
      <Sequence key={'s' + i} from={Math.max(0, x.f - (x.k === 'pop' || x.k === 'click' ? 0 : 4))} durationInFrames={20} layout="none">
        <Audio src={staticFile('sfx/' + x.k + '.wav')} volume={0.85} />
      </Sequence>
    ))}
    {/* optional background music, far below the voice, faded in and out */}
    {data.music ? (
      <Audio src={staticFile(data.music.src)} loop volume={(f) => (data.music.volume ?? 0.06) * interpolate(f, [0, 20, data.total - 45, data.total], [0, 1, 1, 0], cl)} />
    ) : null}
    <Subs />
  </AbsoluteFill>
  );
};
```

**`video/src/Visuals.tsx`**: semua jenis visual dan satu pembungkus transisi.

<!-- file: video/src/Visuals.tsx -->
```tsx
import React from 'react';
import {AbsoluteFill, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame, Easing} from 'remotion';
import {SANS, SERIF, ACCENT, LIGHT, INK, FPS, cl, ease, sp} from './theme';

/* ---------- shared pieces ---------- */
const Label: React.FC<{num?: string; label?: string; sub?: string; ink?: boolean}> = ({num, label, sub, ink}) => {   // ink = dark text, for light backgrounds
  const f = useCurrentFrame();
  const p = sp(f, 3);
  if (!label) return null;
  return (
    <div style={{position: 'absolute', left: 64, top: 170, opacity: p, transform: `translateY(${(1 - p) * 30}px)`}}>
      <div style={{display: 'flex', alignItems: 'baseline', gap: 18}}>
        {num ? <span style={{fontFamily: SERIF, fontStyle: 'italic', fontWeight: 800, fontSize: 84, color: ink ? INK : ACCENT, textShadow: ink ? 'none' : '0 4px 20px rgba(0,0,0,.6)'}}>{num}</span> : null}
        <span style={{fontFamily: SANS, fontWeight: 800, fontSize: 68, color: ink ? INK : '#fff', letterSpacing: ink ? -1 : 1, textShadow: ink ? 'none' : '0 4px 24px rgba(0,0,0,.75)'}}>{label}</span>
      </div>
      {sub ? <div style={{marginTop: 10, display: 'inline-block', fontFamily: SANS, fontWeight: 600, fontSize: 32, color: ink ? '#fff' : '#111', background: ink ? INK : 'rgba(255,255,255,0.92)', padding: '8px 18px', borderRadius: 12}}>{sub}</div> : null}
    </div>
  );
};
const Grain: React.FC = () => (
  <AbsoluteFill style={{opacity: 0.07, mixBlendMode: 'overlay', backgroundImage: 'repeating-radial-gradient(circle at 17% 32%, #fff 0, #000 1px, transparent 2px, transparent 5px)'}} />
);
const BlurBg: React.FC<{img: string}> = ({img}) => (
  <AbsoluteFill style={{backgroundColor: '#0c0c0e'}}>
    <Img src={staticFile(img)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(40px) brightness(0.32) saturate(1.2)', transform: 'scale(1.3)'}} />
  </AbsoluteFill>
);

/* ---------- photo: full-screen image or generated image, slow push-in, optional label ----------
   {type:"photo", img, label?, num?, sub?, pos?: "50% 40%" (focus point), dim?: 0..1} */
const Photo: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, e.t - e.f], [1.1, 1.22]);
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Img src={staticFile(e.img)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: e.pos || '50% 50%', transform: `scale(${z})`, transformOrigin: e.pos || '50% 50%', filter: `contrast(1.05) saturate(1.05) brightness(${1 - (e.dim || 0)})`}} />
      <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 30%)'}} />
      <Label num={e.num} label={e.label} sub={e.sub} />
    </AbsoluteFill>
  );
};

/* ---------- clip: full-screen B-roll VIDEO (stock footage, product shot, screen recording), always muted ----------
   {type:"clip", src: "broll/x.mp4", from?: seconds into the file, label?, num?, sub?, pos?, dim?}
   The file must be at least 1 s longer than the time it is on screen. */
const Clip: React.FC<{e: any}> = ({e}) => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <OffthreadVideo muted src={staticFile(e.src)} startFrom={Math.round((e.from || 0) * FPS)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: e.pos || '50% 50%', filter: `brightness(${1 - (e.dim || 0)})`}} />
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 30%)'}} />
    <Label num={e.num} label={e.label} sub={e.sub} />
  </AbsoluteFill>
);

/* ---------- screenshot: a REAL page (article, profile, search result, app) as a card ----------
   {type:"screenshot", img, img_w, img_h (pixel size of the png), source?: "SITE · date",
    highlights?: [{x,y,w,h, at?: frames after start}]  marker-pen boxes in image pixels,
    scroll?: px of the image to scroll through while visible,
    click?: {x,y} in image pixels + click_at: anchor  -> a cursor moves there and clicks} */
const Screenshot: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const CARD_W = 960, CARD_TOP = 230, CARD_H = Math.min(1000, (e.img_h * CARD_W) / e.img_w);
  const S = CARD_W / e.img_w;
  const p = sp(f, 0, {damping: 18, stiffness: 120, mass: 0.8});
  const zoom = interpolate(f, [0, d], [1.0, 1.06]);
  const scroll = interpolate(f, [8, d - 4], [0, e.scroll || 0], {...cl, easing: Easing.inOut(Easing.quad)}) * S;
  const clickF = e.click_at !== undefined ? e.click_at - e.f : null;
  const mv = clickF !== null ? interpolate(f, [clickF - 28, clickF - 4], [0, 1], {...cl, easing: Easing.bezier(0.45, 0, 0.2, 1)}) : 0;
  const press = clickF !== null ? interpolate(f, [clickF, clickF + 3, clickF + 9], [0, 1, 0], cl) : 0;
  const tx = e.click ? e.click.x * S : 0, ty = e.click ? e.click.y * S - scroll : 0;
  return (
    <AbsoluteFill>
      <BlurBg img={e.img} />
      {e.source ? (
        <div style={{position: 'absolute', left: 60, top: 150, opacity: p, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: '#fff', letterSpacing: 3}}>
          <span style={{background: ACCENT, color: '#111', padding: '6px 14px', borderRadius: 8, marginRight: 14}}>SUMBER</span>{e.source}
        </div>
      ) : null}
      <div style={{position: 'absolute', left: 60, top: CARD_TOP, width: CARD_W, height: CARD_H, borderRadius: 28, overflow: 'hidden', background: '#fff', boxShadow: '0 40px 90px rgba(0,0,0,0.6)', transform: `translateY(${(1 - p) * 420}px) rotate(${(1 - p) * -3}deg) scale(${zoom})`, transformOrigin: '50% 20%', opacity: Math.min(1, p * 2)}}>
        <div style={{position: 'absolute', left: 0, top: -scroll, width: CARD_W}}>
          <Img src={staticFile(e.img)} style={{width: CARD_W, display: 'block'}} />
          {(e.highlights || []).map((h: any, i: number) => {
            const at = h.at ?? 20 + i * 26;
            const w = interpolate(f, [at, at + 14], [0, 1], {...cl, easing: ease});
            return <div key={i} style={{position: 'absolute', left: h.x * S, top: h.y * S, height: h.h * S, width: h.w * S * w, background: ACCENT, mixBlendMode: 'multiply'}} />;
          })}
          {e.click ? <div style={{position: 'absolute', left: tx - 150, top: e.click.y * S - 46, width: 300, height: 92, borderRadius: 46, background: '#000', opacity: 0.18 * press}} /> : null}
        </div>
        {clickF !== null && e.click ? (
          <svg width={96} height={96} viewBox="0 0 24 24" style={{position: 'absolute', left: interpolate(mv, [0, 1], [CARD_W + 40, tx]), top: interpolate(mv, [0, 1], [ty + 220, ty]) - Math.sin(mv * Math.PI) * 46, opacity: interpolate(f, [clickF - 30, clickF - 25], [0, 1], cl), transform: `scale(${1 - 0.14 * press})`, transformOrigin: '0% 0%', filter: 'drop-shadow(0 8px 10px rgba(0,0,0,0.45))'}}>
            <path d="M3 2 L3 19.5 L7.6 15.4 L10.7 22.3 L13.6 21 L10.6 14.2 L16.8 14.2 Z" fill="#111" stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
          </svg>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- custom: your own SVG/diagram component for numbers, steps, comparisons ----------
   {type:"custom", name:"chart", ...props}. Register components in CUSTOM. Draw with real SVG
   (paths drawn on with strokeDashoffset, labels that spring in), not boxes of HTML text. */
const Bars: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const max = Math.max(...e.values.map((v: any) => v.n));
  const hi = e.color || '#0A84FF';   // the one bar that matters (the last one); take the colour from the brand or the topic
  return (
    <AbsoluteFill style={{background: LIGHT}}>
      <Label ink label={e.label} sub={e.sub} />
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path d="M130 1120 H950" stroke="#D2D2D7" strokeWidth={4} strokeLinecap="round" />
        {e.values.map((v: any, i: number) => {
          const g = sp(f, 10 + i * 8, {damping: 18, stiffness: 120});
          const last = i === e.values.length - 1;
          const h = (v.n / max) * 560 * g, x = 170 + i * (760 / e.values.length), w = 560 / e.values.length;
          return (
            <g key={i}>
              <rect x={x} y={1118 - h} width={w} height={h} rx={16} fill={last ? hi : '#C7C7CC'} />
              <text x={x + w / 2} y={1118 - h - 24} textAnchor="middle" fontFamily={SANS} fontWeight={800} fontSize={42} fill={last ? hi : INK} opacity={g}>{v.text ?? v.n}</text>
              <text x={x + w / 2} y={1184} textAnchor="middle" fontFamily={SANS} fontWeight={700} fontSize={32} fill="#6E6E73">{v.name}</text>
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};
const CUSTOM: Record<string, React.FC<{e: any}>> = {bars: Bars};

/* ---------- outro: brand/creator end card over an image ----------
   {type:"outro", img, logo?, handle?, cta?} */
const Outro: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const z = interpolate(f, [0, d], [1.06, 1.2]);
  const p = sp(f, Math.max(8, d - 64), {damping: 16, stiffness: 140});
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Img src={staticFile(e.img)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${z})`, transformOrigin: '50% 45%'}} />
      <AbsoluteFill style={{backgroundColor: `rgba(10,8,6,${0.45 * p})`}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 520, textAlign: 'center', opacity: p, transform: `translateY(${(1 - p) * 40}px)`}}>
        {e.logo ? (
          <div style={{display: 'inline-flex', width: 280, height: 280, borderRadius: 140, background: '#fff', alignItems: 'center', justifyContent: 'center', boxShadow: '0 20px 60px rgba(0,0,0,0.5)'}}>
            <Img src={staticFile(e.logo)} style={{width: 200, height: 200, objectFit: 'contain'}} />
          </div>
        ) : null}
        {e.handle ? <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 66, color: '#fff', marginTop: 34, textShadow: '0 4px 24px rgba(0,0,0,.7)'}}>{e.handle}</div> : null}
        {e.cta ? <div style={{marginTop: 18}}><span style={{fontFamily: SANS, fontWeight: 800, fontSize: 40, color: '#111', background: ACCENT, padding: '12px 30px', borderRadius: 16}}>{e.cta}</span></div> : null}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- wrapper for every full-screen insert: owns ALL in/out transitions ---------- */
export const Insert: React.FC<{e: any; chained: boolean; prevChained: boolean}> = ({e, chained, prevChained}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const inn = prevChained ? 1 : interpolate(f, [0, 7], [0, 1], {...cl, easing: ease});          // fade in over the speaker
  const out = chained || e.type === 'outro' ? 1 : interpolate(f, [d - 6, d], [1, 0], cl);          // fade back to the speaker
  const slide = prevChained ? interpolate(f, [0, 12], [1, 0], {...cl, easing: Easing.bezier(0.45, 0, 0.15, 1)}) : 0; // push over the previous insert
  const body = e.type === 'photo' ? <Photo e={e} /> : e.type === 'clip' ? <Clip e={e} /> : e.type === 'screenshot' ? <Screenshot e={e} /> : e.type === 'outro' ? <Outro e={e} /> : React.createElement(CUSTOM[e.name], {e});
  return (
    <AbsoluteFill style={{opacity: Math.min(inn, out), transform: prevChained ? `translateX(${slide * 1080}px)` : `scale(${1 + (1 - inn) * 0.06})`, overflow: 'hidden', boxShadow: prevChained ? '-30px 0 60px rgba(0,0,0,0.5)' : undefined}}>
      {body}
      <Grain />
    </AbsoluteFill>
  );
};

/* ---------- split: the visual sits in a panel on TOP, the speaker stays visible BELOW it ----------
   {type:"split", img | src (video), h?: 760 panel height px, shift?: 300 px the speaker moves down,
    fit?: "cover" | "contain" (contain = logos, app screens, charts: nothing cropped, padded; pad?: CSS padding), bg?: panel colour, pos?, from?,
    caption?: "short label", click?: {x,y} in PANEL pixels + click_at: anchor -> cursor moves there and clicks}
   Use it when the viewer should keep seeing the speaker (reaction, demo, eye contact) while looking at the thing.
   Main.tsx moves the speaker; `p` is its 0..1 progress so panel and speaker move as one. */
export const SplitPanel: React.FC<{e: any; p: (e: any, frame: number) => number}> = ({e, p}) => {
  const f = useCurrentFrame();                       // local frame of this panel's <Sequence>
  const lead = e.pre ? 10 : 0;
  const abs = e.f - lead + f;                        // absolute frame
  const H = e.h ?? 760;
  const k = p(e, abs);
  const fade = e.chainPrev ? interpolate(abs, [e.f, e.f + 10], [0, 1], cl) : 1;   // a chained panel dissolves over the previous one
  const z = interpolate(abs, [e.f, e.t], [1.0, e.fit === 'contain' ? 1.0 : 1.06], cl);
  const media: React.CSSProperties = {width: '100%', height: '100%', objectFit: e.fit || 'cover', objectPosition: e.pos || '50% 50%', transform: `scale(${z})`,
    boxSizing: 'border-box', padding: e.fit === 'contain' ? (e.pad ?? '130px 110px 90px') : 0};   // contain: breathing room, clear of the app's top bar
  const clickF = e.click_at !== undefined ? e.click_at - e.f + lead : null;
  const mv = clickF !== null ? interpolate(f, [clickF - 26, clickF - 4], [0, 1], {...cl, easing: Easing.bezier(0.45, 0, 0.2, 1)}) : 0;
  const press = clickF !== null ? interpolate(f, [clickF, clickF + 3, clickF + 9], [0, 1, 0], cl) : 0;
  return (
    <div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: H, overflow: 'hidden', background: e.bg || (e.fit === 'contain' ? LIGHT : '#000'), transform: `translateY(${-(1 - k) * H}px)`, opacity: fade, boxShadow: '0 14px 40px rgba(0,0,0,0.35)'}}>
      {e.src ? <OffthreadVideo muted src={staticFile(e.src)} startFrom={Math.round((e.from || 0) * FPS)} style={media} /> : <Img src={staticFile(e.img)} style={media} />}
      {e.caption ? (
        <div style={{position: 'absolute', left: 44, bottom: 36, fontFamily: SANS, fontWeight: 700, fontSize: 34, color: INK, background: 'rgba(255,255,255,0.94)', padding: '10px 22px', borderRadius: 16, opacity: interpolate(f, [lead + 6, lead + 14], [0, 1], cl)}}>{e.caption}</div>
      ) : null}
      {clickF !== null && e.click ? (
        <svg width={88} height={88} viewBox="0 0 24 24" style={{position: 'absolute', left: interpolate(mv, [0, 1], [1080 + 20, e.click.x]), top: interpolate(mv, [0, 1], [e.click.y + 200, e.click.y]) - Math.sin(mv * Math.PI) * 40, transform: `scale(${1 - 0.14 * press})`, transformOrigin: '0% 0%', filter: 'drop-shadow(0 8px 10px rgba(0,0,0,0.45))'}}>
          <path d="M3 2 L3 19.5 L7.6 15.4 L10.7 22.3 L13.6 21 L10.6 14.2 L16.8 14.2 Z" fill="#111" stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
        </svg>
      ) : null}
    </div>
  );
};

/* ---------- overlays: sit on top of the speaker, in the top third (never over the face or subtitles) ----------
   {type:"title", line1, line2}
   {type:"bubbles", items:[{at: anchor, text, img?, side?: "l"|"r", x_at?: anchor}]}  chat/quote bubbles
   {type:"chips",   items:[{at: anchor, n?: "1", text}]}                               numbered key points */
export const Overlay: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const out = interpolate(f, [d - 7, d], [1, 0], cl);
  if (e.type === 'title') {
    const p = sp(f, 0, {damping: 14, stiffness: 160, mass: 0.7});
    const hl = interpolate(f, [8, 20], [0, 1], {...cl, easing: ease});
    return (
      <AbsoluteFill style={{opacity: out}}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 120, textAlign: 'center', transform: `translateY(${(1 - p) * -60}px) scale(${0.9 + 0.1 * p})`, opacity: p}}>
          <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 50, color: '#fff', letterSpacing: 5, textShadow: '0 4px 20px rgba(0,0,0,.8)'}}>{e.line1}</div>
          <div style={{display: 'inline-block', position: 'relative', marginTop: 6, padding: '0 34px'}}>
            <div style={{position: 'absolute', left: 0, top: 22, bottom: 10, width: `${hl * 100}%`, background: ACCENT, borderRadius: 14, transform: 'skewX(-8deg)'}} />
            <span style={{position: 'relative', fontFamily: SERIF, fontStyle: 'italic', fontWeight: 800, fontSize: 132, color: hl > 0.5 ? '#111' : '#fff', lineHeight: 1.15}}>{e.line2}</span>
          </div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{opacity: out}}>
      {e.items.map((it: any, i: number) => {
        const at = it.f - e.f;
        if (f < at) return null;
        const p = sp(f, at, {damping: 13, stiffness: 190, mass: 0.6});
        if (e.type === 'chips') {
          return (
            <div key={i} style={{position: 'absolute', left: 50, top: 140 + i * 138, display: 'flex', alignItems: 'center', gap: 22, background: 'rgba(14,14,18,0.86)', borderRadius: 60, padding: it.n ? '16px 44px 16px 16px' : '22px 44px', transform: `translateX(${(1 - p) * -80}px) scale(${0.85 + 0.15 * p})`, opacity: Math.min(1, p * 1.4), transformOrigin: '0% 50%', boxShadow: '0 16px 40px rgba(0,0,0,0.4)', border: '3px solid rgba(255,255,255,0.14)'}}>
              {it.n ? <div style={{width: 84, height: 84, borderRadius: 42, background: ACCENT, color: '#111', fontFamily: SANS, fontWeight: 800, fontSize: 50, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{it.n}</div> : null}
              <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 48, color: '#fff'}}>{it.text}</div>
            </div>
          );
        }
        const right = it.side === 'r';
        const xp = it.x_at !== undefined && f >= it.x_at - e.f ? sp(f, it.x_at - e.f, {damping: 9, stiffness: 220, mass: 0.6}) : 0;
        return (
          <div key={i} style={{position: 'absolute', top: 130 + i * 210, left: right ? undefined : 44, right: right ? 44 : undefined, maxWidth: 800, transformOrigin: right ? '100% 100%' : '0% 100%', transform: `scale(${p}) rotate(${(1 - p) * (right ? 6 : -6)}deg)`}}>
            <div style={{display: 'flex', alignItems: 'center', gap: 22, background: '#fff', borderRadius: 40, borderBottomLeftRadius: right ? 40 : 10, borderBottomRightRadius: right ? 10 : 40, padding: it.img ? '18px 34px 18px 18px' : '24px 36px', boxShadow: '0 18px 44px rgba(0,0,0,0.42)'}}>
              {it.img ? <Img src={staticFile(it.img)} style={{width: 132, height: 132, objectFit: 'cover', borderRadius: 26, flexShrink: 0}} /> : null}
              <div style={{fontFamily: SANS, fontWeight: 700, fontSize: 40, lineHeight: 1.22, color: '#15151a', letterSpacing: -0.4}}>{it.text}</div>
            </div>
            {xp ? (
              <div style={{position: 'absolute', right: -26, top: -30, width: 118, height: 118, borderRadius: 59, background: '#FF3B30', display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${xp}) rotate(${(1 - xp) * -40}deg)`, boxShadow: '0 12px 28px rgba(0,0,0,0.45)', border: '6px solid #fff'}}>
                <svg width={60} height={60} viewBox="0 0 60 60"><path d="M12 12 L48 48 M48 12 L12 48" stroke="#fff" strokeWidth={10} strokeLinecap="round" /></svg>
              </div>
            ) : null}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
```

**`work/edit.example.json`**: contoh `edit.json` lengkap (dijelaskan di Bagian 4). Blok kodenya ada di Bagian 4.1 dan ikut terekstrak.

### 2.4 Kenapa arsitekturnya begini

- **Data terpisah dari tampilan.** `work/edit.json` berisi keputusan (potongan, teks, visual). `build_timeline.py` menghitung frame. Komponen React hanya menggambar apa yang ada di `data.json`. Revisi menjadi perubahan beberapa baris JSON, bukan menulis ulang kode.
- **Satu pembungkus transisi (`Insert`).** Semua insert layar penuh masuk dan keluar dengan cara yang sama, jadi tidak ada transisi yang berbeda-beda atau terlupa.
- **Zoom pembicara dihitung otomatis** dan hanya berubah di dua tempat yang tidak terlihat sebagai glitch: saat pembicara tertutup insert, atau tepat di sambungan potongan yang terlihat (punch-in).
- **Insert berurutan saling menyambung.** Kalau insert B mulai di frame yang sama dengan berakhirnya insert A, B menggeser masuk di atas A dan pembicara tidak muncul sekilas di antaranya.
- **Tiga tata letak dalam satu sistem.** Pembicara penuh dengan overlay kecil, insert layar penuh, dan layar terbagi (`split`: visual di atas, pembicara di bawah). Subtitle, zoom, dan efek suara menyesuaikan sendiri di ketiganya, sehingga tata letak bisa berganti dari scene ke scene tanpa kode baru.
- **Subtitle menyesuaikan latar.** Di atas insert terang (`light`), teks berubah gelap dan gradasi gelap di bawah dimatikan. Di layar terbagi, subtitle ikut turun supaya tetap di bawah dagu.

---
## Bagian 3. Alur kerja: 11 tahap dengan gate

Ringkasan urutan dan file yang dihasilkan:

| Tahap | Isi | Hasil |
|---|---|---|
| Pra | Kesiapan mesin (Bagian 2.1) | `doctor.py` berakhir `RESULT: READY` |
| 0 | Brief dan bahan | `work/brief.md`, klip di `raw/` |
| 1 | Normalisasi dan melihat footage | `video/public/*.mp4`, `work/look_*.jpg`, `work/footage.md` |
| 2 | Transkrip dan peta roll | `work/tx/*`, `work/roll_map.md` |
| 3 | Naskah final | `work/script.md` |
| 4 | Titik potong presisi | `segments` di `work/edit.json` |
| 5 | Teks subtitle | `text`, `script`, `timing` di `work/edit.json` |
| 6 | Rencana visual dan aset | `work/visual_plan.md`, aset di `video/public/` |
| 7 | Bangun timeline | `events` di `work/edit.json`, `video/src/data.json` |
| 8 | Loop still | `work/qa_stills.jpg` |
| 9 | Render dan QA | `out/final_v1.mp4`, gambar dan log QA |
| 10 | Serah terima dan revisi | laporan, `out/final_v2.mp4`, ... |

### Tahap 0. Brief dan bahan

**Klip.** Kalau klip belum ada di `raw/` dan user memberi link folder Google Drive publik:

```bash
gdown --folder "https://drive.google.com/drive/folders/<id>" -O raw/
```

Folder privat tidak bisa diunduh: minta user membuka aksesnya ("siapa saja yang memiliki link") atau menyalin filenya sendiri ke `raw/`. Jangan pernah mengubah atau menimpa file di `raw/`.

**Brief.** Tulis `work/brief.md` sebelum menyentuh video:

- Jenis konten (lihat Bagian 6) dan satu kalimat: apa yang harus dibawa pulang penonton.
- Platform, rasio, dan durasi target. Default: 9:16, 45 sampai 150 detik, 1080x1920. Kalau user minta lebih tajam, render dengan skala 1.3334 (1440x2560, tahap 9).
- Siapa penontonnya.
- Nama brand, orang, akun, dan istilah khusus beserta ejaan yang benar. Daftar ini dipakai sebagai kosakata untuk Whisper.
- CTA di akhir, logo, warna brand kalau ada.
- Referensi gaya kalau ada. Referensi adalah patokan rasa (kepadatan visual, gaya subtitle), bukan untuk ditiru persis.
- Apa pun yang tidak disebut user: isi dengan default dan tandai `ASUMSI`.

Kalau user memberi video referensi:

```bash
mkdir -p work/ref && yt-dlp -f "mp4/best" -o "work/ref/ref.%(ext)s" "<url>"
python3 tools/sheet.py video work/ref/ref.mp4 work/ref/sheet 1
```

Buka `work/ref/sheet_*.jpg` dan catat: posisi dan gaya subtitle, seberapa sering visual muncul, jenis visualnya, tata letaknya (layar penuh atau terbagi), cara masuk dan keluarnya. Kalau unduhan gagal karena video diblokir wilayah, privat, atau butuh login: **jangan diakali** (tanpa VPN, proxy, cookie pinjaman). Minta user mengirim file mp4-nya, dan lanjutkan dulu dengan default di guide ini.

Preferensi desain yang pernah dinyatakan user (di percakapan ini, di file catatan project, atau di memori agent) dicatat di brief dan berlaku untuk seluruh video.

**Gate:** klip ada di `raw/`. Jenis konten, durasi target, dan CTA terisi. Semua asumsi ditandai.

### Tahap 1. Normalisasi dan melihat footage

```bash
bash tools/normalize.sh
for f in video/public/*.mp4; do n=$(basename "$f" .mp4); python3 tools/sheet.py video "$f" "work/look_$n" 1; done
```

Buka setiap `work/look_*.jpg` dan tulis `work/footage.md`. Per klip, catat:

- Framing: posisi dan ukuran wajah. Kalau berbeda antar klip, catat klip mana yang perlu digeser atau diperbesar supaya wajah berada di tempat yang sama (dipakai di `framing`).
- Benda yang ditunjukkan ke kamera dan pada detik berapa. **Saat pembicara memperlihatkan sesuatu, gambar pembicara adalah visualnya. Jangan ditutup insert.**
- Gestur kuat (menunjuk, menghitung dengan jari), perubahan posisi, gangguan (orang lewat, kamera goyang, fokus hilang).
- Ruang kosong di frame: area mana yang aman untuk overlay tanpa menutupi wajah.

Sumber 16:9 (podcast, kamera horizontal): lihat Bagian 6.4 sebelum menjalankan normalisasi.

**Gate:** semua contact sheet sudah dibuka. `work/footage.md` ada dan menyebut waktu setiap benda yang ditunjukkan.

### Tahap 2. Transkrip dan peta roll

```bash
python3 tools/transcribe.py id "Nama Brand, nama orang, istilah khusus dari brief" > work/transcribe.log 2>&1
```

Argumen pertama adalah kode bahasa (`id`, `en`, ...). Argumen kedua adalah kosakata dari brief, supaya nama dieja benar.

Baca setiap `work/tx/<klip>.txt`. Formatnya `indeks:kata[waktu mulai]`. Tanda `?` berarti Whisper ragu, dan baris `-- gap --` berarti jeda di atas 0,35 detik.

Tulis `work/roll_map.md`. Per klip:

- Ringkasan isi dalam dua kalimat.
- Daftar kalimat: indeks kata awal sampai akhir, waktu, dan teksnya.
- Tanda untuk setiap kalimat: `TAKE ULANG dari <klip> kalimat <n>`, `SALAH UCAP`, `MULAI ULANG` (kalimat yang dihentikan lalu diulang dari awal), `FILLER`, `JEDA PANJANG`, atau `BERSIH`.
- Untuk setiap kelompok take ulang: take mana yang terbaik dan kenapa.

Cara mengenali take ulang: dua kalimat dengan awal yang sama atau makna yang sama, baik di klip yang sama maupun klip lain. Satu klip pendek yang seluruh isinya mengulang bagian klip lain adalah take cadangan utuh.

Cara memilih take: (1) kalimatnya selesai tanpa tersendat, (2) tidak ada kata yang diulang atau dikoreksi, (3) energi dan kecepatan bicaranya cocok dengan kalimat sebelum dan sesudahnya, (4) kalau setara, pilih yang lebih pendek. Jangan otomatis memilih take terakhir.

Kata yang ditandai `?`, nama brand, angka, dan istilah asing jangan dipercaya begitu saja. Cocokkan dengan brief. Kalau masih ragu, potong 3 sampai 5 detik bagian itu dan transkrip ulang bagian pendek tersebut, atau tandai sebagai `ASUMSI` untuk dikonfirmasi user.

**Gate:** setiap kalimat di setiap klip punya tanda. Setiap kelompok take ulang punya satu pemenang. Ejaan nama sudah dicek terhadap brief.

### Tahap 3. Naskah final

Tulis `work/script.md`: naskah video dari awal sampai akhir, satu baris per kalimat, dengan kolom klip, indeks kata awal dan akhir, dan teks. Di bawahnya, daftar yang dibuang beserta alasannya.

Urutan berpikir:

1. Tentukan satu pesan utama dari brief.
2. Pilih struktur sesuai jenis konten (Bagian 6).
3. Pilih hook: kalimat paling kuat yang membuat orang mau mendengar lanjutannya. Hook berada di 3 detik pertama. Hook boleh diambil dari tengah roll dan dipindah ke depan, asal kalimat itu berdiri sendiri dan tidak terdengar janggal saat diulang nanti. Kalau roll sudah dibuka dengan kuat, jangan dipindah-pindah.
4. Susun sisanya mengikuti urutan bicara asli sebisa mungkin. Memindahkan kalimat hanya kalau membuat cerita lebih jelas.
5. Buang: take ulang yang kalah, salah ucap, mulai ulang, basa-basi pembuka, kalimat yang mengulang isi kalimat sebelumnya, dan menyimpang dari pesan utama.
6. Pertahankan: jeda napas wajar, kata sambung yang membuat kalimat terdengar alami, dan gaya bicara pembicara. Ini video orang bicara, bukan teks yang dibacakan.

Uji sambungan: baca naskah final dari atas ke bawah. Di setiap pergantian segmen, cek tiga hal. Pertama, kalimat sesudah potongan tidak merujuk ke sesuatu yang ikut terbuang ("yang tadi", "itu", "kedua" tanpa "pertama"). Kedua, tata bahasanya nyambung, tidak ada kata sambung menggantung. Ketiga, tidak ada informasi yang disebut dua kali.

Jumlah potongan: untuk satu pembicara yang lancar, biasanya 3 sampai 8 segmen per 2 menit. Roll yang banyak tersendat boleh lebih. Lebih baik satu segmen panjang yang utuh daripada tiga potongan kecil yang masing-masing menghemat setengah detik.

**Gate:** hook di 3 detik pertama. Uji sambungan lolos di setiap pergantian segmen. Durasi perkiraan masuk target brief. Setiap bagian yang dibuang punya alasan.

### Tahap 4. Titik potong presisi

Waktu kata dari Whisper bisa meleset sampai 0,3 detik, terutama di awal dan akhir kalimat. Titik potong ditentukan dari kenyaringan audio, bukan dari Whisper.

Untuk setiap awal dan akhir segmen di `script.md`:

```bash
python3 tools/envelope.py <nama klip> <t0> <t1>      # contoh: python3 tools/envelope.py take1 14.2 15.4
```

Setelah normalisasi, suara bicara berada di atas kira-kira -25 dB dan jeda di bawah -35 dB. Aturan penempatan:

- **Awal segmen (`in`)**: 0,05 sampai 0,10 detik sebelum kenyaringan naik untuk kata pertama. Jangan mulai tepat di kata, karena konsonan awalnya terpotong.
- **Akhir segmen (`out`)**: 0,10 sampai 0,20 detik setelah kata terakhir turun ke bawah -35 dB, supaya ekor suaranya utuh. Kalau kata berikutnya (yang dibuang) mulai sebelum itu, potong di titik paling sunyi di antara keduanya.
- **Jeda di sambungan**: jumlah sunyi di akhir segmen dan awal segmen berikutnya kira-kira 0,2 sampai 0,4 detik untuk pergantian kalimat. Lebih pendek terdengar terburu-buru, lebih panjang terasa macet.
- **Potong di awal kalimat, bukan di tengah gerakan.** Lihat frame di kedua sisi sambungan. Kalau di tengah kalimat pembicara tiba-tiba memegang benda yang sebelumnya tidak ada, geser potongan ke awal kalimat supaya gerakannya terlihat utuh.

Tulis hasilnya ke `work/edit.json` bagian `clips` dan `segments` (format di Bagian 4). `segments` ditulis dalam urutan tampil di video.

Kalau sebuah kata tersendat ada di tengah segmen dan terlalu pendek untuk dipotong tanpa terdengar, biarkan di audio dan sembunyikan dari subtitle (tahap 5).

**Gate:** setiap `in` dan `out` berada di titik yang envelope-nya di bawah -30 dB, atau ada catatan kenapa tidak bisa. Tidak ada segmen yang mulai atau berakhir di tengah kata.

### Tahap 5. Teks subtitle

Subtitle dibuat otomatis dari kata transkrip yang lolos potongan. Tugas di tahap ini adalah membetulkan teks dan memilih kata penting.

- **Ejaan dan salah dengar**: perbaiki lewat `text` (per kata) atau `script` (satu rentang kalimat sekaligus). Subtitle harus sama dengan yang diucapkan. Jangan memperhalus bahasa pembicara.
- **Kata penting**: beri awalan `*`. Kata bertanda tampil besar dengan font serif miring berwarna aksen. Pilih 1 sampai 2 kata per kalimat, dan hanya kata yang membawa makna: angka, nama, kata kunci topik, kata yang ditekan pembicara. Kalau semua ditandai, tidak ada yang menonjol.
- **Kata yang disembunyikan**: isi `""` di `text`, atau `_` di `script`, untuk kata tersendat yang masih terdengar tapi tidak perlu dibaca.
- **Waktu kata yang salah**: kalau subtitle muncul terlalu cepat atau lambat dibanding suaranya (biasanya kata pertama setelah potongan), betulkan waktunya di `timing` berdasarkan envelope.
- **Huruf besar**: subtitle ditampilkan huruf kecil semua kecuali kata yang diawali entri `keep_case` (nama brand, singkatan). Kalau user ingin huruf besar normal, ubah fungsi `clean` di `Main.tsx`.

Jalankan `python3 tools/build_timeline.py` dan baca seluruh daftar subtitle yang dicetak, dari atas ke bawah, sebagai penonton. Perhatikan juga setiap `WARNING`: kata yang separuhnya terpotong berarti titik potong atau `timing` perlu dibetulkan.

**Gate:** daftar subtitle terbaca sebagai naskah yang utuh. Tidak ada salah eja nama. Kata besar tidak lebih dari kira-kira satu per 2 sampai 3 detik.

### Tahap 6. Rencana visual dan aset

#### 6.1 Putuskan per kalimat

Tulis `work/visual_plan.md` sebagai tabel: kalimat, indeks kata, keputusan, jenis visual, sumber aset, alasan. Untuk setiap kalimat pilih satu dari empat:

- **Tetap di pembicara.** Untuk hook, opini pribadi, emosi, kalimat penghubung, dan saat pembicara menunjukkan benda. Ini pilihan default.
- **Overlay kecil di atas pembicara** (judul, gelembung kutipan, chip poin bernomor). Untuk kutipan orang lain, daftar poin, dan penanda bagian. Wajah tetap terlihat.
- **Layar terbagi** (`split`: visual di panel atas, pembicara tetap terlihat di bawah). Untuk hal yang perlu dilihat **sambil** melihat pembicara: ia bereaksi, menjelaskan sambil menunjuk, atau kontak matanya penting. Juga untuk logo, tampilan aplikasi, dan foto yang tidak perlu memenuhi layar.
- **Insert layar penuh** (screenshot, foto, klip B-roll, diagram). Untuk hal yang lebih jelas dilihat daripada didengar.

Tabel pemetaan isi kalimat ke visual:

| Yang diucapkan | Visual | Sumber |
|---|---|---|
| Fakta, berita, klaim, tren, statistik dari pihak lain | Screenshot artikel atau halaman asli, kalimat pentingnya distabilo | `tools/shot.py` |
| Menyebut aplikasi, website, platform, akun | Screenshot halaman aslinya, layar penuh atau di panel `split`. Kalau ada aksi (cari, klik, DM, WhatsApp, follow), kursor bergerak ke tombol lalu klik | `tools/shot.py` dengan `--find` |
| Menyebut orang, tokoh, perusahaan, produk | Foto atau logo asli. Logo paling rapi di panel `split` dengan `fit: "contain"` | `tools/stock.py commons`, situs resmi |
| Angka, perbandingan, kenaikan/penurunan, ukuran | Diagram SVG buatan sendiri yang digambar bertahap | Komponen `custom` |
| Langkah, daftar, syarat ("ada tiga hal") | Chip bernomor yang muncul satu per satu tepat saat tiap poin disebut | Overlay `chips` |
| Kutipan atau pertanyaan orang lain ("orang sering nanya...") | Gelembung chat | Overlay `bubbles` |
| Benda, tempat, suasana, aktivitas | Foto atau klip footage stok yang benar-benar memperlihatkan hal itu | `tools/stock.py photo` / `video`, lalu `photo`, `clip`, atau `split` |
| Benda spesifik yang tidak ada foto stoknya | Gambar hasil image generation, gaya foto realistis | Image generation, kalau tersedia (6.2) |
| Cara pakai aplikasi atau langkah di layar | Rekaman layar asli sebagai klip | `clip` |
| CTA di akhir | Screenshot profil asli dengan kursor mengklik tombol, lalu kartu penutup berlogo | `screenshot` + `outro` |
| Opini, cerita pribadi, emosi, hook | Tidak ada. Tetap di pembicara, kata kuncinya dibesarkan di subtitle | |

Aturan kepadatan dan waktu:

- Insert layar penuh menutup kira-kira 20 sampai 45% durasi. Di atas 50%, video terasa seperti slideshow. Di bawah 15% untuk video informatif, terasa flat.
- Jangan lebih dari sekitar 8 detik tanpa perubahan visual apa pun (insert, overlay, kata besar, atau punch-in).
- 3 sampai 5 detik pertama: pembicara dan judul. Jangan langsung menutup wajah dengan insert.
- Durasi insert: 1,5 sampai 4 detik. Screenshot dengan teks yang harus dibaca: minimal 2,5 detik.
- Insert mulai 2 sampai 4 frame **sebelum** kata yang digambarkannya (offset `-3`), dan berakhir saat topik kalimatnya selesai.
- Daftar yang disebut berurutan ("ukuran, desain, finishing") memakai insert berantai: akhir insert pertama dan awal insert kedua memakai jangkar yang sama, sehingga bergeser langsung dari satu ke berikutnya.
- Di antara dua insert yang tidak berantai, pembicara terlihat minimal 24 frame. Kurang dari itu terlihat seperti kedipan.
- Variasi jenis: jangan memakai jenis visual yang sama tiga kali berturut-turut.
- Variasi tata letak: dalam satu video pakai minimal dua dari tiga tata letak (pembicara penuh dengan overlay, layar terbagi, layar penuh), dan jangan memakai tata letak yang sama untuk semua scene. Video yang seluruh visualnya kartu layar penuh terasa seperti template.
- Panel `split` dihitung sebagai perubahan visual, tetapi tidak dihitung sebagai insert layar penuh. Durasinya 2 sampai 6 detik.
- Angka di diagram harus berasal dari ucapan pembicara atau sumber yang bisa ditunjuk. Kalau angka hanya ilustrasi, tulis "contoh ilustrasi" di diagramnya.

#### 6.2 Kumpulkan aset

Semua aset disimpan di `video/public/` (subfolder `shots/`, `photos/`, `broll/`, `logos/`, `gen/`, `music/`). Catat URL sumber setiap aset di `work/visual_plan.md`.

**Screenshot halaman asli**

```bash
python3 tools/shot.py "https://situs.com/artikel" video/public/shots/artikel.png --height 1600 --find "potongan judul" --find "kalimat penting"
```

Skrip mencetak ukuran gambar (`img_w`, `img_h`) dan kotak setiap teks yang dicari dalam piksel gambar. Kotak itu langsung dipakai sebagai `highlights` (stabilo) atau `click` (titik tengah tombol: `x + w/2`, `y + h/2`). Pakai potongan teks yang spesifik supaya yang ketemu adalah elemen yang dimaksud.

- Cari sumbernya dulu lewat pencarian web: nama brand atau topik + "berita", halaman resmi, profil publik.
- Hanya halaman publik. Jangan login, jangan menembus halaman privat. Kalau profilnya privat, pakai sumber lain.
- Buka hasilnya. Pastikan bukan halaman error, captcha, atau tertutup pop-up, dan teks pentingnya terbaca.
- Tulis nama situs dan tanggal di `source` supaya tampil sebagai label sumber.

**Tampilan aplikasi dan situs (real-environment UI)**

Kalau pembicara menyebut aplikasi, situs, chat, atau notifikasi, penonton harus melihat tampilan aslinya:

1. Pilihan pertama: screenshot halaman publiknya (`tools/shot.py`), atau rekaman layar dan screenshot dari user.
2. Kalau tampilan aslinya tidak bisa diambil (aplikasi di balik login, layar ponsel): susun dari bahan asli, yaitu logo resmi (`tools/stock.py commons "<nama> logo"`), warna dan tata letak aplikasi yang sebenarnya, dengan melihat screenshot aslinya sebagai acuan. Elemen diletakkan di tempat yang sama seperti di aplikasinya dan muncul pada saat yang sama dengan ucapan.
3. UI karangan yang tidak menyerupai aplikasi atau situs mana pun (kartu bergaya dashboard, ikon generik, latar dekoratif) tidak dipakai. Kalau tidak ada bahan asli, lebih baik tetap di pembicara dengan kata besar.

**Foto dan footage stok, tanpa API key**

```bash
python3 tools/stock.py photo "hands counting cash" -n 6        # Pexels, vertikal. Tambah --landscape untuk panel split
python3 tools/stock.py video "barista pouring coffee" -n 4     # klip Pexels
python3 tools/stock.py open "night market jakarta" -n 6        # Openverse: foto berlisensi CC, cadangan kalau Pexels kosong
```

Skrip membuka halaman pencarian publik lewat browser tanpa login, mengunduh kandidat ke `work/cand/<kata-kunci>/`, mencetak URL sumber dan lisensi tiap file, dan membuat contact sheet `work/cand/<kata-kunci>.jpg`.

- Kata kunci memakai bahasa Inggris dan menyebut bendanya secara konkret ("hands counting cash", bukan "finance").
- **Buka contact sheet-nya dan pilih.** Kriteria: benar-benar memperlihatkan hal yang diucapkan, cocok dipotong vertikal (atau horizontal untuk panel `split`), tidak ada watermark atau teks asing, warna tidak bertabrakan dengan footage.
- Salin yang dipilih ke `video/public/photos/` atau `video/public/broll/`, dan catat URL sumber serta lisensinya di `work/visual_plan.md`.
- Klip B-roll: durasi minimal 1 detik lebih panjang dari waktu tayangnya. Komponen `clip` dan `split` memotongnya sendiri ke bingkai, jadi tidak perlu diubah ukurannya.
- Kalau Pexels menampilkan pemeriksaan bot atau hasilnya kosong: pakai `open` atau `commons`, ganti kata kunci, atau minta user mengunduh sendiri. Jangan mencoba menembus pemeriksaan itu.

**Logo, orang, tempat, benda terkenal (Wikimedia Commons)**

```bash
python3 tools/stock.py commons "TikTok logo" -n 6
```

Logo berformat SVG diunduh sebagai PNG transparan (dan vektornya kalau server mengizinkan). Pakai logo resmi apa adanya: jangan digambar ulang, diwarnai ulang, atau diubah bentuknya. Logo dari user selalu didahulukan. Foto orang nyata hanya dari sumber seperti ini atau dari user, tidak dari image generation.

**Diagram SVG**: digambar sebagai komponen di `Visuals.tsx` (lihat 4.4). Bukan gambar diam, supaya garis dan batangnya bisa tumbuh mengikuti ucapan.

**Image generation (opsional)**: hanya untuk benda spesifik yang tidak ada foto aslinya. Prompt gaya foto realistis, vertikal (1024x1536), tanpa teks di dalam gambar. Jangan dipakai untuk orang nyata, logo, tampilan aplikasi, atau bukti (berita, testimoni). Simpan di `video/public/gen/`.

- Codex: minta gambar langsung di percakapan atau sebut `$imagegen`, lalu simpan hasilnya ke `video/public/gen/<nama>.png`.
- Claude Code dan agent tanpa pembuat gambar: tulis daftar prompt di `work/gen_prompts.md`, minta user membuatnya di aplikasi lain dan menaruh filenya di `video/public/gen/`. Kalau user tidak mau menunggu, ganti dengan foto stok atau diagram.
- Buka setiap gambar hasilnya sebelum dipakai: tidak ada teks rusak, tangan aneh, atau benda yang salah.

**Efek suara**: empat efek di `video/public/sfx/` dibuat `tools/make_sfx.sh` dengan ffmpeg. Tidak perlu mengunduh apa pun. Situs efek suara gratis sering menolak unduhan otomatis (HTTP 403), jadi jangan bergantung padanya.

**Musik (opsional)**: hanya kalau user minta atau memberi filenya. Taruh di `video/public/music/`, isi `music` di `edit.json`, volume 0,05 sampai 0,08 (jauh di bawah suara). Jangan mengunduh lagu berhak cipta.

**Gate:** setiap baris di `visual_plan.md` yang bukan "tetap di pembicara" punya file aset yang sudah dibuka dan dilihat. Setiap visual lolos pertanyaan "kata mana yang digambarkan". Sebagian besar visual berasal dari sumber nyata. Minimal dua tata letak dipakai.

### Tahap 7. Bangun timeline

Isi `events` di `work/edit.json` dari `visual_plan.md` (format di Bagian 4), lalu:

```bash
python3 tools/build_timeline.py
```

Baca laporannya setiap kali:

- Durasi total, persentase yang tertutup insert layar penuh, dan persentase panel `split`. Bandingkan dengan target.
- `exposed jump cuts`: sambungan potongan yang terlihat. Di titik itu zoom otomatis berganti (punch-in). Kalau jumlahnya banyak dan berdekatan, pertimbangkan menutup sebagian dengan insert yang memang relevan, atau kurangi potongan.
- `WARNING` event lebih pendek dari 20 frame, atau pembicara hanya terlihat beberapa frame di antara dua insert: perbaiki jangkarnya.
- Error `full-screen events overlap`: dua insert bertabrakan. Geser salah satunya.
- Error `split ... overlaps`: panel `split` bertabrakan dengan insert atau panel lain. Buat bersentuhan (jangkar yang sama) atau pisahkan.
- `WARNING: overlay ... during split`: overlay dan panel sama-sama memakai bagian atas layar. Pindahkan salah satunya.

**Gate:** tidak ada error dan tidak ada warning yang belum dijelaskan.

### Tahap 8. Loop still

Render frame tunggal jauh lebih cepat daripada render video. Pakai untuk mengecek setiap visual sebelum render penuh.

```bash
cd video && node stills.mjs 40 150 320 480 640 && cd ..     # nomor frame dari laporan build_timeline
python3 tools/sheet.py stills work/qa_stills.jpg
```

Pilih frame: tengah setiap event, 2 sampai 3 frame di sekitar setiap awal dan akhir insert dan panel `split`, frame saat kursor mengklik, frame dengan subtitle terpanjang, dan frame dengan kata besar terpanjang. Buka `work/qa_stills.jpg` dan periksa:

- Subtitle tidak keluar layar, tidak menutupi wajah, tidak bertabrakan dengan overlay.
- Teks di screenshot terbaca. Stabilo tepat di atas kalimat yang dimaksud.
- Kursor mendarat tepat di tombol.
- Foto terpotong dengan benar (atur `pos`), tidak ada wajah atau objek penting yang terpotong.
- Overlay berada di sepertiga atas dan tidak menutupi wajah. Kalau menutupi, kecilkan atau pindahkan lewat `framing` atau posisi overlay.
- Wajah berada di posisi yang sama di semua klip (bandingkan frame dari klip berbeda, betulkan `framing`).
- Panel `split`: kepala pembicara utuh di bawah panel (tidak terpotong tepi panel), dagu di atas subtitle. Kalau tidak pas, atur `shift` (seberapa jauh pembicara turun) dan `h` (tinggi panel) event itu. Logo dan tampilan aplikasi memakai `fit: "contain"` supaya tidak terpotong.
- Insert terang: subtitle berwarna gelap dan terbaca. Insert gelap: subtitle putih.
- Gaya konsisten dan bersih: font, warna, sudut membulat, bayangan. Setiap logo dan tampilan aplikasi atau situs terlihat seperti aslinya.

Perbaiki, build, render still lagi. Ulangi sampai bersih. Jangan lanjut ke render penuh dengan still yang masih bermasalah.

**Gate:** setiap event punya minimal satu still yang sudah dilihat dan lolos.

### Tahap 9. Render dan QA

```bash
nohup bash tools/render.sh v1 > work/render_v1.log 2>&1 &     # background. Cek: tail -c 400 work/render_v1.log
# lebih tajam (1440x2560): bash tools/render.sh v1 1.3334      RAM kecil: CONCURRENCY=2 bash tools/render.sh v1
```

Hasil: `video/out/master_v1.mp4` (kualitas tinggi) dan `out/final_v1.mp4` (untuk dikirim). Lalu jalankan lima pemeriksaan. Semuanya wajib.

**QA 1. Teknis.** Di akhir log: `h264` dan `aac`, 1080x1920 (atau 1440x2560), `30/1`, `yuv420p`, `color_range=tv`, `color_space=bt709`, durasi sesuai, kenyaringan sekitar -14 sampai -16 LUFS, true peak di bawah -1 dB. Kalau `pix_fmt` bukan `yuv420p`, warna bisa berubah setelah diunggah: jangan dikirim.

**QA 2. Keseluruhan.**

```bash
python3 tools/sheet.py video out/final_v1.mp4 work/sheet_v1 1
```

Buka setiap `work/sheet_v1_*.jpg` (satu frame per detik). Tonton sebagai penonton dari awal sampai akhir: ritme visual merata, tidak ada bagian panjang yang kosong, tidak ada frame hitam atau aset yang gagal dimuat, subtitle selalu ada saat orang bicara.

**QA 3. Transisi, frame per frame.**

```bash
python3 tools/sheet.py strips out/final_v1.mp4 work/strips_v1
python3 tools/scene_check.py out/final_v1.mp4
```

`strips` membuat satu baris berisi 12 frame berurutan untuk setiap transisi: awal dan akhir setiap insert dan panel `split`, setiap sambungan potongan, setiap pergantian zoom. Buka semua file `work/strips_v1_*.jpg` dan periksa setiap baris. Yang dicari:

- Pembicara muncul 1 sampai 3 frame di antara dua insert berurutan.
- Zoom pembicara meloncat tepat setelah insert menghilang.
- Warna atau efek kembali sekilas sebelum insert masuk.
- Benda atau posisi tubuh berubah mendadak di tengah kalimat.
- Insert menghilang sebelum fade selesai, atau satu frame kosong.
- Panel `split` dan pembicara tidak bergerak bersamaan, atau ada celah hitam di antara keduanya.
- Subtitle dari kalimat sebelumnya masih tersisa setelah sambungan.

`scene_check.py` mendaftar semua perubahan gambar mendadak dan mencocokkannya dengan yang direncanakan. Setiap baris `UNEXPLAINED` harus dilihat framenya (`cd video && node stills.mjs <frame-1> <frame> <frame+1>`), lalu diperbaiki atau dijelaskan (misalnya gerakan cepat pembicara).

**QA 4. Audio.**

```bash
python3 tools/verify_audio.py out/final_v1.mp4 id > work/verify_v1.log 2>&1
```

Bandingkan `FULL TEXT` dengan `work/script.md`. Untuk setiap baris `cut at`, kata sebelum dan sesudah `||` harus utuh: tidak ada kata yang hilang separuh, tidak ada kata dobel, tidak ada sisa kata dari bagian yang dibuang. Kalau ada, geser `in`/`out` segmen itu 0,03 sampai 0,10 detik berdasarkan envelope dan render ulang.

**QA 5. Subtitle terhadap suara.** Ambil 5 sampai 8 titik acak dari daftar subtitle di `work/timeline_v1.log`, render still pada frame itu, dan pastikan kata yang disorot adalah kata yang sedang diucapkan menurut transkrip ulang.

Setiap perbaikan: ubah `work/edit.json`, build, still di titik yang diperbaiki, lalu render ulang dengan nomor versi baru. Ulangi QA 3 dan QA 4 untuk bagian yang berubah.

**Gate:** kelima QA lolos pada file yang akan dikirim, bukan pada versi sebelumnya.

### Tahap 10. Serah terima dan revisi

Kirim `out/final_vN.mp4` dengan laporan singkat (format di Bagian 9). Laporan harus menyebut dengan jujur apa yang tidak bisa dicek agent, terutama bahwa hasilnya belum didengarkan oleh telinga manusia.

Saat ada revisi:

1. Tulis ulang permintaan user sebagai daftar perubahan konkret. Kalau user mengirim screenshot, cari frame itu di video dan pastikan elemen yang dimaksud.
2. Ubah hanya itu. Jangan ikut "memperbaiki" bagian lain yang sudah disetujui.
3. Kalau perubahan menyentuh elemen yang muncul di beberapa tempat (logo, warna), samakan semuanya dan laporkan.
4. Still di titik yang berubah, render versi baru (`v2`, `v3`), simpan versi lama.
5. Ulangi QA transisi dan audio pada bagian yang berubah, dan QA keseluruhan sekali.
6. Kalau user bertanya "ada yang patah?", jangan menjawab dari ingatan. Jalankan ulang QA 3 dan lihat stripnya.
7. Masukan user pada satu video (misalnya lebih suka kursor yang mengklik daripada garis yang berdenyut) berlaku untuk seluruh sisa project itu. Untuk video berikutnya, ambil prinsipnya sebagai bahan perbaikan, bukan sebagai cetakan yang harus diulang di setiap desain. Catat di `work/brief.md`, dan di file memori atau instruksi agent kalau ada.

---

## Bagian 4. Referensi `work/edit.json`

### 4.1 Contoh lengkap

Contoh untuk video opini/edukasi (file `work/edit.example.json` di kit). Isinya contoh, bentuknya yang dipakai. Salin menjadi `work/edit.json` lalu ganti isinya.

<!-- file: work/edit.example.json -->
```json
{
  "fps": 30,
  "clips": {"A": "take1", "B": "take3"},
  "segments": [
    {"clip": "B", "in": 12.4, "out": 16.85},
    {"clip": "A", "in": 0.62, "out": 21.3},
    {"clip": "A", "in": 27.95, "out": 44.1},
    {"clip": "B", "in": 20.15, "out": 41.7}
  ],
  "framing": {"B": {"scale": 1.05, "y": -40}},
  "timing": {"A": {"3": [0.7, 1.18]}},
  "text": {"A": {"12": "*Rp10 juta", "30": ""}},
  "script": {"B": [{"from": 42, "text": "Gaji naik, tapi *tabungan tetap *nol."}]},
  "keep_case": ["BPS", "Instagram"],
  "sub_max_chars": 24,
  "sub_max_words": 4,
  "outro_frames": 60,
  "music": {"src": "music/bed.mp3", "volume": 0.06},
  "events": [
    {"type": "title", "start": 4, "end": ["B", 54], "line1": "KENAPA GAJI", "line2": "Selalu habis"},
    {"type": "bubbles", "start": ["A", 8, -2], "end": ["A", 24, 4], "items": [
      {"at": ["A", 8, -2], "text": "Gaji segini kok nggak pernah cukup ya?", "img": "photos/wallet.jpg", "side": "l"},
      {"at": ["A", 16, -2], "text": "Nanti aja nabungnya kalau gaji naik", "side": "r", "x_at": ["A", 24]}]},
    {"type": "screenshot", "start": ["A", 30, -3], "end": ["A", 44, -4], "img": "shots/article.png", "img_w": 1080, "img_h": 1600, "source": "NAMA MEDIA · 12 Mei 2025", "highlights": [{"x": 32, "y": 404, "w": 272, "h": 60}, {"x": 233, "y": 719, "w": 410, "h": 30}]},
    {"type": "custom", "name": "bars", "start": ["A", 44, -4], "end": ["A", 52, -3], "label": "PENGELUARAN / BULAN", "sub": "angka dari ucapan pembicara", "values": [{"name": "makan", "n": 3.5, "text": "Rp3,5jt"}, {"name": "cicilan", "n": 2.8, "text": "Rp2,8jt"}, {"name": "nongkrong", "n": 1.9, "text": "Rp1,9jt"}]},
    {"type": "photo", "start": ["A", 52, -3], "end": ["A", 60, -3], "img": "photos/coffee.jpg", "num": "01", "label": "LATTE FACTOR", "sub": "kecil tapi tiap hari", "pos": "50% 40%"},
    {"type": "clip", "start": ["A", 60, -3], "end": ["A", 68, -2], "src": "broll/shopping.mp4", "from": 1.0, "num": "02", "label": "CHECKOUT IMPULSIF"},
    {"type": "split", "start": ["A", 74, -3], "end": ["A", 88], "img": "shots/app.png", "fit": "contain", "caption": "aplikasi pencatat keuangan", "click": {"x": 540, "y": 520}, "click_at": ["A", 82]},
    {"type": "split", "start": ["A", 88], "end": ["A", 96], "src": "broll/saving.mp4", "from": 0.5, "caption": "tabung di awal bulan"},
    {"type": "chips", "start": ["A", 100, -4], "end": ["A", 125, 8], "items": [
      {"at": ["A", 100, -4], "n": "1", "text": "Catat 30 hari"},
      {"at": ["A", 112, -4], "n": "2", "text": "Tabung di awal"}]},
    {"type": "screenshot", "start": ["B", 100, -4], "end": ["B", 118, 2], "img": "shots/profile.png", "img_w": 1080, "img_h": 1600, "click": {"x": 880, "y": 96}, "click_at": ["B", 108]},
    {"type": "outro", "start": ["B", 128, -5], "end": "end", "img": "photos/desk.jpg", "logo": "logo.png", "handle": "@namaakun", "cta": "follow buat tips berikutnya"}
  ]
}
```

### 4.2 Field utama

| Field | Isi |
|---|---|
| `fps` | 30. Skrip QA mengasumsikan 30 |
| `clips` | Huruf pendek untuk tiap klip: `{"A": "<nama file di video/public tanpa .mp4>"}`. Transkripnya dibaca dari `work/tx/<nama>.json` |
| `segments` | Bagian yang dipakai, **dalam urutan tampil**: `clip`, `in`, `out` (detik di klip sumber). Segmen dari klip yang sama tidak boleh saling tumpang tindih |
| `framing` | Per klip: `scale`, `x`, `y` (piksel) supaya wajah berada di posisi yang sama di semua klip |
| `timing` | Koreksi waktu kata: `{"A": {"<indeks>": [mulai, selesai]}}` |
| `text` | Koreksi teks per kata: `"*kata"` = kata besar, `""` = disembunyikan, teks lain = pengganti |
| `script` | Menulis ulang satu rentang sekaligus: `{"from": <indeks kata pertama>, "text": "..."}`. Satu token per kata Whisper. `_` menyembunyikan kata, `~` adalah spasi di dalam satu token (`Rp10~juta`) |
| `keep_case` | Kata yang huruf besarnya dipertahankan di subtitle |
| `sub_max_chars`, `sub_max_words` | Panjang maksimum satu potong subtitle. Default 24 karakter, 4 kata |
| `outro_frames` | Frame tambahan setelah segmen terakhir untuk kartu penutup. 45 sampai 75 |
| `music` | Opsional: `{"src": "music/bed.mp3", "volume": 0.06}` |
| `full_types` | Opsional: daftar jenis event yang menutup seluruh layar. Default `photo, clip, screenshot, custom, outro`. `split` bukan layar penuh |
| `events` | Semua visual. Lihat 4.3 |

### 4.3 Jangkar waktu dan jenis event

Setiap `start`, `end`, `at`, dan field berakhiran `_at` adalah jangkar:

- `["A", 57]`: saat kata indeks 57 di klip A **mulai** diucapkan.
- `["A", 57, -3]`: 3 frame sebelumnya.
- `["A", 57, 4, "e"]`: 4 frame setelah kata itu **selesai**.
- `120`: frame absolut. Hanya untuk awal video (judul).
- `"end"`: frame terakhir video.

Indeks kata dibaca dari `work/tx/<klip>.txt`. Jangkar ke kata yang ikut terbuang otomatis menempel ke awal segmen berikutnya dari klip itu.

Overlay (pembicara tetap terlihat):

| `type` | Field | Dipakai untuk |
|---|---|---|
| `title` | `line1`, `line2` | Judul di 3 sampai 5 detik pertama |
| `bubbles` | `items`: `at`, `text`, `img` (opsional), `side` `"l"`/`"r"`, `x_at` (opsional: tanda silang merah) | Kutipan atau pertanyaan orang lain |
| `chips` | `items`: `at`, `n` (opsional), `text` | Poin bernomor yang muncul saat disebut |

Insert layar penuh:

| `type` | Field | Dipakai untuk |
|---|---|---|
| `photo` | `img`, `label`, `num`, `sub`, `pos`, `dim` (semua opsional kecuali `img`) | Foto asli atau gambar buatan, zoom pelan |
| `clip` | `src`, `from` (detik), `label`, `num`, `sub`, `pos`, `dim` | Footage B-roll atau rekaman layar, tanpa suara |
| `screenshot` | `img`, `img_w`, `img_h`, `source`, `highlights` [`x`,`y`,`w`,`h`], `scroll`, `click` {`x`,`y`}, `click_at` | Halaman asli. Stabilo, scroll, dan kursor yang mengklik |
| `custom` | `name` + field bebas | Diagram SVG sendiri. `bars` sudah tersedia |
| `outro` | `img`, `logo`, `handle`, `cta` | Kartu penutup |

Field `light: true` pada insert layar penuh berarti latarnya terang: subtitle berubah gelap dan gradasi gelap di bawah dimatikan. `custom` otomatis `light` (diagram bawaan berlatar terang). Tulis `"light": false` kalau komponen buatanmu berlatar gelap, dan `"light": true` pada `photo` yang hampir putih.

Layar terbagi (visual di atas, pembicara tetap terlihat di bawah):

| `type` | Field | Dipakai untuk |
|---|---|---|
| `split` | `img` atau `src` (video, dengan `from`), `h` (tinggi panel, default 760), `shift` (pembicara turun berapa piksel, default 300, tidak boleh lebih dari `h`), `fit` (`"cover"` default, `"contain"` untuk logo dan tampilan aplikasi), `bg` (warna panel), `pos`, `caption`, `click` {`x`,`y`} dalam piksel **panel** + `click_at` | Hal yang dilihat sambil tetap melihat pembicara: logo, aplikasi, foto, klip |

Panel masuk dari atas sementara pembicara turun bersamaan, dan kembali dengan cara yang sama. Subtitle ikut turun. Panel boleh bersentuhan dengan panel lain (melebur) atau dengan insert layar penuh (berganti saat tertutup), tetapi tidak boleh tumpang tindih. Jangan menaruh overlay (`title`, `bubbles`, `chips`) pada waktu yang sama dengan panel.

Dua insert berantai: tulis jangkar yang persis sama untuk `end` insert pertama dan `start` insert kedua. Berlaku juga untuk dua panel `split`, dan untuk panel yang disambung insert.

### 4.4 Menambah visual sendiri

Kalau satu kalimat butuh visual yang belum ada (garis waktu, peta, perbandingan dua kolom, diagram ukuran), tulis komponen baru di `Visuals.tsx` dan daftarkan di `CUSTOM`:

```tsx
const Timeline: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();                       // 0 = frame pertama insert ini
  const draw = interpolate(f, [6, 30], [1, 0], {...cl, easing: ease});
  const hi = e.color || '#0A84FF';
  return (
    <AbsoluteFill style={{background: LIGHT}}>
      <Label ink label={e.label} sub={e.sub} />
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path d="M140 900 H940" stroke="#C7C7CC" strokeWidth={8} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={draw} />
        {e.points.map((p: any, i: number) => {
          const g = sp(f, 14 + i * 10);
          const x = 140 + (800 * i) / (e.points.length - 1);
          return (
            <g key={i} opacity={g}>
              <circle cx={x} cy={900} r={18 * g} fill={i === e.points.length - 1 ? hi : INK} />
              <text x={x} y={840} textAnchor="middle" fontFamily={SANS} fontWeight={800} fontSize={44} fill={INK}>{p.year}</text>
              <text x={x} y={970} textAnchor="middle" fontFamily={SANS} fontWeight={600} fontSize={30} fill="#6E6E73">{p.text}</text>
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};
const CUSTOM: Record<string, React.FC<{e: any}>> = {bars: Bars, timeline: Timeline};
```

Aturan untuk komponen baru:

- Jangan menulis transisi masuk atau keluar sendiri. `Insert` sudah mengurusnya.
- Gambar dengan SVG yang tumbuh (`strokeDashoffset`, tinggi batang, `sp()` untuk kemunculan). Elemen muncul berurutan mengikuti ucapan, bukan sekaligus.
- Semua gerak dihitung dari `useCurrentFrame()`. Jangan pakai animasi CSS atau `setTimeout`, karena tidak ikut ter-render.
- Pakai `SANS`, `SERIF`, `LIGHT`, `INK`, `ACCENT` dari `theme.ts`. Latar bawaan diagram adalah `LIGHT` dengan teks `INK` (`<Label ink ... />`) dan satu warna penekanan untuk hal yang paling penting. Boleh diganti mengikuti brand, asal tetap bersih dan terbaca. Isi teks dan angka datang dari `edit.json`, bukan ditulis di komponen.
- Satu diagram satu gagasan. Paling banyak 5 sampai 6 elemen dan banyak ruang kosong.
- Area aman: konten utama di y 150 sampai 1200. Area y 1270 sampai 1530 milik subtitle. Di bawah 1530 tertutup antarmuka aplikasi.
- Setelah menulis: `npx tsc --noEmit -p .` di `video/`, lalu still di tiga titik (awal, tengah, akhir insert).

---

## Bagian 5. Standar desain

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

## Bagian 6. Penyesuaian per jenis roll

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

---

## Bagian 7. Masalah yang sering terjadi

| Gejala | Penyebab | Perbaikan |
|---|---|---|
| Video terasa flat walau banyak animasi | Visualnya hiasan, tidak menggambarkan kalimat | Ulangi tahap 6.1. Setiap visual harus punya kata yang digambarkan dan sebaiknya dari sumber nyata |
| Visual muncul terlambat atau terlalu cepat | Frame diketik tangan, atau jangkar ke kata yang salah | Pakai jangkar kata. Cek indeks di `work/tx/*.txt`. Mulai 3 frame sebelum kata |
| Pembicara berkedip di antara dua insert | Ada celah beberapa frame | Rantaikan (jangkar sama) atau beri jarak minimal 24 frame |
| Zoom meloncat setelah insert hilang | Zoom berganti saat pembicara terlihat | Sudah ditangani `build_timeline.py`. Jangan menambah zoom manual |
| Kata terpotong atau dobel di sambungan | Potongan memakai waktu Whisper | Tahap 4 dengan envelope, lalu QA 4 |
| Bunyi klik di sambungan | Tidak ada fade audio | Fade 2 frame sudah ada di `Main.tsx`. Jangan dihapus |
| Benda tiba-tiba ada di tangan | Potongan di tengah gerakan | Geser potongan ke awal kalimat |
| Subtitle salah eja nama | Whisper salah dengar | `text` atau `script`, kosakata di `transcribe.py`, `keep_case` |
| Subtitle tidak pas dengan suara di awal segmen | Waktu kata pertama meleset | Betulkan di `timing` berdasarkan envelope |
| Wajah bergeser saat ganti klip | Framing antar klip berbeda | `framing` per klip, cek dengan still |
| Still gagal: file tidak ditemukan (404) | Aset belum ada di `video/public`, atau namanya berbeda dari yang ditulis di `edit.json` | Taruh filenya di `video/public`. Cek huruf besar kecil nama file |
| Bundler error `readFile` undefined | TypeScript terlalu baru | `npm i -D typescript@5.5.4` |
| Screenshot tertutup pop-up atau halaman login | Modal situs | `shot.py` sudah menghapus modal umum. Kalau masih, cari sumber publik lain. Jangan login |
| Foto stok tidak nyambung dengan omongan | Kata kunci pencarian terlalu abstrak | Cari bendanya secara konkret, lihat kandidat dengan `sheet.py assets` |
| Terlalu banyak potongan, terasa gelisah | Memotong setiap jeda kecil | Kembalikan jeda wajar. Gabungkan segmen yang hanya menghemat kurang dari 0,5 detik |
| Render sangat lama | Normal: beberapa menit sampai puluhan menit, tergantung CPU (Bagian 0.7) | Cek desain lewat still dulu, render penuh hanya saat still sudah bersih |
| `ModuleNotFoundError: faster_whisper` (atau `PIL`, `playwright`) | venv tidak aktif di shell itu | Awali perintah dengan `source .venv/bin/activate && ` |
| `error: externally-managed-environment` saat `pip install` | Memasang ke Python sistem | Pakai `.venv` (dibuat `tools/setup.sh`) |
| `npx: command not found`, atau Node di bawah 18 | Node belum terpasang atau terlalu lama | Pasang Node 20 (Bagian 0.2) |
| Unduhan gagal, `Could not resolve host`, model Whisper tidak terunduh | Shell agent tidak punya akses jaringan (bawaan Codex) | Nyalakan jaringan (Bagian 0.4), lalu `python3 tools/doctor.py` |
| Remotion: `Failed to launch the browser process`, `error while loading shared libraries` | Pustaka sistem untuk Chrome belum ada (Linux, WSL2) | Perintah pustaka di Bagian 0.2, butuh `sudo` dari user |
| Playwright: `Executable doesn't exist` | Chromium belum diunduh | `python3 -m playwright install chromium` |
| Render mati di tengah, `Killed`, atau komputer macet | RAM habis | `CONCURRENCY=2 bash tools/render.sh v1`, tutup aplikasi lain |
| Transkrip sangat lambat atau kehabisan RAM | Model besar di mesin kecil | `WHISPER_MODEL=medium`. Kalau ada GPU NVIDIA: `WHISPER_DEVICE=cuda WHISPER_COMPUTE=float16` |
| Teks tampil dengan font bawaan | Font Google gagal diunduh saat render | Pastikan ada internet saat render. Offline: ganti font di `theme.ts` dengan font lokal |
| `stock.py`: `nothing found`, atau Pexels menampilkan pemeriksaan bot | Kata kunci terlalu sempit, atau situs menolak browser otomatis | Kata kunci lain, `open` atau `commons`, atau minta user mengunduh. Jangan ditembus |
| Wikimedia `HTTP 429` | Mengunduh file asli atau ukuran thumbnail tidak standar | `stock.py commons` sudah memakai ukuran standar. Tunggu sebentar, kurangi `-n` |
| Situs efek suara atau musik menolak unduhan (`HTTP 403`) | Situs memblokir unduhan otomatis | Pakai `tools/make_sfx.sh`. Musik dari user |
| Video referensi tidak bisa diunduh | Diblokir wilayah, privat, atau butuh login | Minta file mp4 ke user. Jangan diakali |
| Warna pucat atau terlalu gelap setelah diunggah | File bukan `yuv420p` BT.709 | Kirim `out/final_vN.mp4` dari `render.sh`, bukan master. Cek QA 1 |
| Kepala terpotong panel, atau subtitle menutup dagu di layar terbagi | `shift` dan `h` tidak cocok dengan posisi wajah | Atur `shift` dan `h` event `split`, cek dengan still |
| Subtitle tidak terbaca di atas visual terang | Insert terang tanpa `light` | Tambah `"light": true` pada event itu |
| Kit hilang atau rusak sebagian | File terhapus atau terpotong | Salin atau ekstrak ulang kit (Bagian 2.3). `doctor.py` menyebut file yang hilang |

---

## Bagian 8. Batasan yang harus disampaikan dengan jujur

- Agent tidak mendengar. Sambungan audio dicek lewat transkrip ulang dan angka kenyaringan. Intonasi, rasa musik, dan bunyi efek belum dinilai telinga. Minta user menonton sekali dengan suara.
- Agent melihat frame, bukan gerak. Kelancaran gerak dinilai dari strip frame berurutan. Itu menangkap frame yang salah, tetapi rasa tempo tetap perlu mata manusia.
- Ejaan nama yang hanya terdengar di audio bisa salah. Selalu laporkan sebagai asumsi.
- Yang sudah dijalankan pada project nyata: output 9:16 (1080x1920 dan skala lebih besar), Linux. Yang belum: output 16:9, macOS dan Windows/WSL2, GPU. Di sana, jalankan `doctor.py` dan loop still lebih teliti.
- Pencarian stok lewat browser bergantung pada tampilan situs saat ini. Kalau situsnya berubah, pakai sumber cadangan atau aset dari user.
- Selera (warna, font, seberapa ramai) berbeda tiap orang. Versi pertama adalah usulan. Revisi dikerjakan dengan aturan tahap 10.
- Guide ini membuat prosesnya bisa diulang. Kualitas akhir tetap bergantung pada apakah setiap gate benar-benar dikerjakan dan setiap gambar QA benar-benar dibuka.

---

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
