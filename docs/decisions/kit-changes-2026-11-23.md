# kit-look: tampilan video = data yang wajib diputuskan (blok `theme` di work/edit.json)

Salinan kerja: `/home/user/jobs/skillwork/kit-look/editkit/` (file lengkap, siap ditimpa ke `editkit/` di repo).
Tidak ada yang diubah di /home/user/editor-team atau /home/user/editkit.

## 1. Perubahan per file

| File | Perubahan | Alasan |
|---|---|---|
| `tools/build_timeline.py` | Langkah 0 baru `check_theme()`: `theme` WAJIB. Validasi: `accent/light/ink` hex `#RGB`/`#RRGGBB`; `font_text/font_emph` satu nama family (tanpa kutip/koma); `emph_style` `italic`/`normal`; `why` wajib (≥ 8 karakter) dan tidak boleh teks contoh (diawali `CONTOH`). Font dicek terpasang lewat `fc-list : family` (semua alias family, tanpa beda huruf besar/kecil). Field opsional `on_accent`, `marker`. Hasil dimasukkan ke `data.json` sebagai `"theme"`. Mencetak satu baris `theme: ...` di laporan. | Default kuning tidak bisa lagi menang diam-diam; tidak ada fallback. |
| | `on_accent` (warna teks DI ATAS isian aksen: highlight judul, angka chip, tag SUMBER, tombol CTA) dihitung otomatis: `ink` atau `#FFFFFF`, mana yang kontrasnya (WCAG) lebih tinggi terhadap aksen. Bisa ditimpa. | Dulu `#111` tetap; dengan aksen gelap (biru) teksnya tidak terbaca. |
| | `marker` (stabilo screenshot, `mix-blend-mode: multiply`), default = `accent`. WARNING kalau gelap (luminance < 0,35) DAN ada screenshot dengan `highlights`. | Stabilo multiply warna gelap menutupi teks halaman. |
| | WARNING: `emph_style: "italic"` tapi `font_emph` tidak punya face italic terpasang (Chrome memiringkan palsu). WARNING: kontras `ink` di atas `light` < 4,5:1. | Peringatan, bukan gagal. |
| `video/src/theme.ts` | Tidak ada lagi warna/font di kode. Membaca `data.json.theme`; kalau tidak ada → `throw` dengan pesan jelas. Ekspor: `SANS` (= font_text), `SERIF` (= font_emph; nama dipertahankan agar komponen custom lama tetap jalan, tidak harus serif), `EMPH_STYLE`, `ACCENT`, `ON_ACCENT`, `MARKER`, `LIGHT`, `INK`, `FPS`, `cl`, `ease`, `sp`. | Satu sumber: edit.json. |
| `video/src/Main.tsx` | Kata besar subtitle: `fontStyle: 'italic'` → `EMPH_STYLE`. | Italic tidak lagi dipaksa. |
| `video/src/Visuals.tsx` | `Label` angka `num` dan `title` line2: `fontStyle` → `EMPH_STYLE`. Teks `#111` di atas `ACCENT` → `ON_ACCENT` (tag SUMBER, CTA outro, angka chip, teks judul line2 saat highlight). Stabilo screenshot `ACCENT` → `MARKER`. Batang penting `bars`: `e.color \|\| '#0A84FF'` → `e.color \|\| ACCENT`. | Warna yang sebenarnya "aksen" ikut tema. Tidak ada restyle lain, tidak ada visual baru. |
| `work/edit.example.json` | Blok `theme` netral (biru `#2F6FED`, Plus Jakarta Sans, normal) dengan `why` diawali `CONTOH, ...` — sengaja DITOLAK build kalau disalin mentah. Sisanya tidak berubah. | Contoh bentuk tanpa jadi default terselubung. |
| `tools/install_fonts.sh` | Baris terakhir sekarang mencetak SEMUA family di `~/.local/share/fonts/editkit` (dulu hanya grep jakarta/playfair). | Nama yang dicetak = nama persis untuk `font_text`/`font_emph`. |

Semua gerak tetap dari `useCurrentFrame`; tidak ada animasi CSS; tidak ada web font.

## 2. Teks referensi untuk `reference/edit-json.md`

Tambahkan baris ini di tabel 4.2 (setelah `clips`):

```
| `theme` | **Wajib, tanpa bawaan.** Tampilan video ini: `accent` (warna kata besar, stabilo, angka chip, batang penting), `light` (latar panel/diagram terang), `ink` (teks gelap), `font_text` (font subtitle dan UI), `font_emph` (font kata besar, judul baris 2, angka label; boleh sama dengan `font_text`), `emph_style` (`"italic"` atau `"normal"`), `why` (alasan pilihan, sama dengan yang ditulis di `work/brief.md`). Opsional: `on_accent` (warna teks di atas isian aksen; bawaan dihitung otomatis: `ink` atau putih, mana yang lebih kontras), `marker` (warna stabilo screenshot; bawaan `accent`, wajib terang karena dicampur multiply). Lihat 4.5 |
```

Dan bagian baru:

```
### 4.5 `theme`: tampilan diputuskan per video

Tidak ada tampilan bawaan. `build_timeline.py` berhenti kalau `theme` tidak ada, kalau isinya salah, atau kalau `why` masih teks contoh.

    "theme": {"accent": "#DE6B17", "light": "#F7F3EC", "ink": "#2B2522",
              "font_text": "Poppins", "font_emph": "Poppins", "emph_style": "normal",
              "why": "oranye = warna tombol di situs brand; Poppins = font situs brand"}

- Putuskan dari brand (warna tombol/logo, font situs), footage (warna baju, ruangan), dan brief. Tulis pilihan dan alasannya di `work/brief.md`, lalu salin alasannya ke `why`.
- Warna ditulis hex `#RRGGBB`. Font ditulis satu nama family persis seperti dicetak `fc-list : family` (tanpa kutip, tanpa `sans-serif`).
- Font harus terpasang sebagai font SISTEM: taruh `.ttf/.otf` statis di `/home/user/editkit/fonts`, jalankan `bash /home/user/editkit/tools/install_fonts.sh` (mencetak nama family yang tersedia). Jangan pernah memuat web font.
- `emph_style: "italic"` hanya kalau `font_emph` punya file italic (Playfair Display di kit hanya italic). Tanpa file italic, build memberi WARNING karena Chrome memiringkan huruf secara palsu.
- Aksen gelap: teks di atas aksen otomatis putih. Kalau video memakai stabilo screenshot, isi `marker` dengan versi pucat aksen (build memberi WARNING kalau terlalu gelap).
- Diagram `bars` memakai `accent` untuk batang penting; tulis `color` di event kalau aksen kurang terbaca di atas `light`.
- Mengganti tampilan = mengubah `theme` lalu menjalankan ulang `build_timeline.py`. Jangan menulis warna atau font di `theme.ts` atau komponen.
```

Di 4.4, ganti kalimat `Pakai SANS, SERIF, LIGHT, INK, ACCENT dari theme.ts ...` menjadi:
"Pakai `SANS`, `SERIF` (font penekanan, belum tentu serif) dengan `fontStyle: EMPH_STYLE`, `LIGHT`, `INK`, `ACCENT`, `ON_ACCENT` dari `theme.ts`. Nilainya datang dari `theme` di `edit.json`; jangan menulis warna atau font sendiri di komponen."

Dokumen lain yang masih menyuruh mengedit `theme.ts` (perlu diselaraskan lead):
- `CLAUDE.md` (root dan repo): "Set them in video/src/theme.ts (ACCENT, LIGHT, INK, SANS, SERIF)" → "Set them in work/edit.json → "theme" (build_timeline refuses a job without it)".
- `.claude/skills/edit-aroll/SKILL.md` baris 37–38, `reference/design.md` baris 4, 24, 28 (`default kuning #FFD60A` sudah tidak ada), `reference/kit.md` baris 80 (`theme.ts` → "membaca `theme` dari data.json; tampilan diatur di `work/edit.json`"), `reference/troubleshooting.md` baris 49 (ganti font di `edit.json` → `theme`).
- Tambahan troubleshooting A yang disarankan: `| build_timeline: ERROR ... "theme" | Tampilan belum diputuskan | Isi blok theme (edit-json.md 4.5) |` dan `| Still/render: data.json has no "theme" | data.json lama | Jalankan build_timeline.py |`.

## 3. Pesan gagal (persis)

Tanpa `theme`:
```
ERROR: work/edit.json has no "theme" block.
Decide the look of THIS video (accent colour, panel/text colours, fonts) from the brand, the footage and the brief,
write the choice + the reason in work/brief.md, then add to work/edit.json:
  "theme": {"accent": "#RRGGBB", "light": "#RRGGBB", "ink": "#RRGGBB",
            "font_text": "<installed font family>", "font_emph": "<installed font family>",
            "emph_style": "italic" | "normal", "why": "<the reason, same as in work/brief.md>"}
There is no default look (see edit-json.md, field "theme").
```
Isi salah (semua kesalahan sekaligus, lalu teks bantuan di atas), contoh:
```
ERROR: invalid "theme" in work/edit.json:
  - theme.accent must be a hex colour like "#DE6B17" (got 'orange')
  - theme.font_text must be ONE font family name without quotes or commas, e.g. "Poppins" (got "'Poppins', sans-serif")
  - theme.emph_style must be "italic" or "normal" (got 'bold')
  - theme.why is required: the reason for this look (brand colour/font, footage, brief), same as in work/brief.md
```
`why` disalin dari contoh: `- theme.why is still the text from edit.example.json: decide the look for THIS video and write your own reason`
Font tidak terpasang:
```
ERROR: theme font(s) not installed as system fonts: Montserrat
  Put the static .ttf/.otf files in /home/user/editkit/fonts, run: bash /home/user/editkit/tools/install_fonts.sh
  then check: fc-list : family | grep -i '<name>'   and use the family name exactly as fc-list prints it.
  Never load web fonts (@remotion/google-fonts, @remotion/fonts, FontFace): they hang the renderer here.
```
data.json lama tanpa theme (dari theme.ts, saat still/render):
`data.json has no "theme": add a "theme" block to work/edit.json and run tools/build_timeline.py (see edit-json.md)`

Semua keluar dengan exit 1 (SystemExit) → `render.sh` (set -e) ikut berhenti.

## 4. Warna hard-coded yang sengaja dibiarkan

- `Main.tsx`: latar `#000`; teks subtitle kecil `#fff` di atas footage; bayangan teks; vignette dan gradasi atas/bawah hitam.
- `Visuals.tsx`:
  - `Label` pill `sub`: `#111` di atas putih 92% (dan `#fff` di atas INK); bayangan.
  - `Grain` `#fff/#000`; `BlurBg` `#0c0c0e`; latar `#000` photo/clip/outro; gradasi atas hitam.
  - Screenshot: kartu `#fff`, teks sumber `#fff`, bayangan klik `#000`, kursor `#111` + `#fff`.
  - `bars`: garis dasar `#D2D2D7`, batang lain `#C7C7CC`, nama batang `#6E6E73` (abu netral).
  - Outro: lingkaran logo `#fff`, handle `#fff`, overlay `rgba(10,8,6,…)`.
  - Split: `bg` panel `#000` (cover), caption `INK` di atas putih 94%.
  - Title line1 `#fff`; line2 `#fff` sebelum highlight.
  - Chips: kapsul `rgba(14,14,18,0.86)`, teks `#fff`, border putih 14%.
  - Bubbles: latar `#fff`, teks `#15151a`, tanda silang merah `#FF3B30` + border `#fff` (makna "salah", bukan aksen).

## 5. Hasil tes (job `/home/user/jobs/_looktest`, klip smoke-test, edit.full.json + satu insert `custom bars` untuk melihat LIGHT/INK/aksen)

| # | Tes | Hasil |
|---|---|---|
| 1 | Tanpa `theme` | GAGAL dengan pesan di atas, exit 1 ✔ |
| 1b | `theme` disalin dari edit.example.json | GAGAL (`why` masih teks contoh) ✔ |
| 1c | Nilai salah (`orange`, font berkutip, `bold`, `why` kosong) | GAGAL, 4 kesalahan terdaftar ✔ |
| 2A | Oranye `#DE6B17`, light `#F7F3EC`, ink `#2B2522`, Poppins/Poppins normal | Still 100/170/470/515: judul highlight oranye + teks ink, kata besar "uang" oranye tegak Poppins, angka chip oranye dengan teks gelap (on_accent = ink, dihitung), diagram latar krem + batang oranye ✔ |
| 2B | Biru `#1E5EFF`, light `#EEF3FF`, ink `#0E1B3D`, Plus Jakarta Sans + Playfair Display italic | Judul "Tiap bulan" Playfair italic putih di atas biru (on_accent = #FFFFFF otomatis), "uang" Playfair italic biru, chip angka putih di lingkaran biru, diagram latar biru pucat + batang biru, teks Jakarta ✔ |
| 2f | Font benar-benar yang disebut, bukan fallback | Crop teks chip dibandingkan dengan teks yang digambar langsung dari file .ttf: A = Poppins ExtraBold, B = Plus Jakarta Sans ExtraBold, emphasis B = Playfair Display ExtraBold Italic ✔ |
| 3 | `font_text: "Montserrat"` (tidak terpasang) | GAGAL dengan pesan font ✔ |
| 3b | `marker` | Aksen oranye + screenshot dengan highlights → WARNING; dengan `marker: #F9D9BF` → tidak ada WARNING; tanpa screenshot → tidak ada WARNING ✔ |
| 4 | `npx tsc --noEmit -p .` | Lulus (theme A dan B) ✔ |
| 5 | Render penuh theme A `CONCURRENCY=2 flock … render.sh v1` | Selesai, 2m19s (termasuk antre lock). h264 1080x1920 30/1 yuv420p tv bt709 + aac, 19,46 s, -15,1 LUFS, true peak -4,5 dBTP ✔. Frame tiap 3 dtk dari final_v1.mp4: tema A konsisten ✔ |
| 6 | data.json tanpa theme → still | Bundle gagal dengan pesan theme.ts yang jelas ✔ (data.json lalu dipulihkan) |

Gambar yang dibuka (Read):
- `/home/user/jobs/_looktest/work/look_A.jpg`
- `/home/user/jobs/_looktest/work/look_B.jpg`
- `/home/user/jobs/_looktest/work/look_fontcheck.jpg`
- `/home/user/jobs/_looktest/work/final_A_0.jpg`
Render: `/home/user/jobs/_looktest/out/final_v1.mp4`, log `/home/user/jobs/_looktest/work/render_v1.log`.
File uji: `/home/user/jobs/_looktest/work/edit.{notheme,copied,bad,nofont,A,B}.json`.

## 6. Belum diverifikasi / catatan

- Insert `screenshot`, `photo`, `clip`, `split`, `outro`, `bubbles` tidak dirender di tes (tidak ada aset); perubahan di sana hanya ganti konstanta (`MARKER`, `ON_ACCENT`), lolos tsc. Tag SUMBER, CTA outro, stabilo belum dilihat dengan mata.
- Font dengan satu ketebalan saja: Chrome menebalkan palsu untuk weight 700/800; build tidak memeriksa ketebalan.
- `emph_style: "normal"` dengan `font_emph: "Playfair Display"`: kit hanya punya file italic Playfair, jadi tetap tampil italic (fontconfig memilih yang ada). Tidak ada WARNING untuk kasus ini.
- Job lama (job01, bench01, _smoketest) punya salinan tools/src sendiri → tidak terpengaruh. Kalau tools baru disalin ke job lama, job itu harus menambah `theme` dulu.
- Setelah menimpa kit: `edit.example.json` di repo dan di `/home/user/editkit/work/` ikut diganti; dokumen di bagian 2 perlu diselaraskan lead.

---

# Tambahan: race file /tmp bersama saat beberapa job jalan paralel

Masalah: `sheet.py` (`grab`) menulis `/tmp/_frame.jpg`, `scene_check.py` menulis `/tmp/_scene.txt`, `verify_audio.py` menulis
`/tmp/_final.wav`. Job paralel saling menimpa (contact sheet berisi frame video lain). `grep -rn "/tmp" tools/` hanya menemukan tiga ini
(`new_job.sh`, `stills.mjs`, `render.sh` tidak memakai /tmp).

| File | Perubahan |
|---|---|
| `tools/sheet.py` | `grab()` memakai `tempfile.TemporaryDirectory(prefix="sheet_")` per panggilan; frame dibaca penuh (`im.copy()`) sebelum folder dihapus. Ukuran, kualitas, dan isi sheet tidak berubah. |
| `tools/scene_check.py` | File metadata ffmpeg di `TemporaryDirectory(prefix="scene_")`, dibaca di dalam blok `with`. Kalau ffmpeg tidak membuat file sama sekali, dibaca sebagai kosong (dulu: bisa membaca file basi dari job lain, atau FileNotFoundError). Output sama. |
| `tools/verify_audio.py` | WAV di `TemporaryDirectory(prefix="verify_")`; transkripsi dan konsumsi generator Whisper (`ws = [...]`) dilakukan di dalam blok `with`, sehingga file masih ada selama dibaca. Output sama. |

Setelah perubahan: `grep -rn "/tmp" tools/` kosong. Folder sementara terhapus otomatis (dicek: tidak ada `sheet_*`/`scene_*`/`verify_*` tersisa di /tmp).
Catatan: `/tmp/_frame.jpg` (03:35) masih ada dari job lain yang memakai `sheet.py` lama; job yang sudah dibuat tetap memakai salinan tools lamanya sampai tools-nya diganti.

Tes:
- Dua `sheet.py video` berjalan BERSAMAAN pada video berbeda (`/home/user/jobs/bench01/work/ref/v1.mp4` 58,6 dtk dan `v2.mp4` 90,4 dtk, tiap 4 dtk):
  `/home/user/jobs/_looktest/work/par_v1_0.jpg` dan `/home/user/jobs/_looktest/work/par_v2_0.jpg` dibuka: v1 hanya berisi frame v1 (topik AI, latar polos),
  v2 hanya frame v2 (topik DBL, dinding kayu). Tidak ada frame tertukar ✔
- `scene_check.py out/final_v1.mp4` (render tema A): 4 hard changes, 0 unexplained, exit 0 ✔
- `flock … verify_audio.py out/final_v1.mp4`: teks penuh benar, baris "cut at 7.10s" tampil, exit 0 ✔
- Mode `sheet.py strips` memakai `grab()` yang sama, tidak diuji terpisah.

---

# Tambahan 2: gerbang "quiet stretch" (ACCEPTANCE.md poin 6)

## Perubahan

| File | Perubahan |
|---|---|
| `tools/build_timeline.py` | Langkah 8 baru (setelah efek suara, SEBELUM `data.json` ditulis). **Perubahan visual** = event masuk atau keluar (semua jenis: overlay, split, layar penuh), item muncul di dalam event (`items[].at`, `x_at`, `click_at`, `tap_at`, field `*_at` lain, dan stabilo `highlights` screenshot pada waktunya sendiri), serta pergantian zoom pembicara (`shots`). Kata subtitle TIDAK dihitung. Semua rentang di antara dua perubahan dihitung, dari frame 0 sampai awal `outro` (atau `total` kalau tidak ada outro). Laporan yang dicetak: jumlah perubahan visual, rata-rata panjang rentang, rentang terpanjang, porsi waktu layar (full-screen / split / pembicara+overlay / pembicara saja, outro tidak dihitung), dan setiap rentang > `max_quiet_s` beserta waktunya dan teks yang diucapkan di dalamnya. |
| | Gerbang: setiap rentang yang terlalu panjang harus ditutup entri `quiet_ok`. Kalau ada yang tidak tertutup, keluar dengan exit 1 dan `data.json` TIDAK ditulis. Daftar rentang, teksnya, dan usulan entri `quiet_ok` dengan jangkar kata ikut tercetak di pesan error, karena `render.sh` mengirim stdout ke log dan hanya stderr yang terlihat. `quiet_ok` tanpa `why` = error. `quiet_ok` yang tidak menutup rentang panjang mana pun = WARNING (basi). Toleransi: entri boleh mulai atau berakhir sampai 1 detik di dalam rentang (jangkar kata jarang tepat di titik perubahan). |
| | Setiap entri `words` sekarang menyimpan indeks kata (`i`) untuk usulan jangkar. Tidak ada yang ditambahkan ke `data.json`; kode Remotion tidak bergantung pada gerbang ini. |
| `work/edit.example.json` | Ditambah `"max_quiet_s": 6.0` dan satu contoh `quiet_ok` dengan alasan. |

## Teks referensi untuk `reference/edit-json.md`

Baris tabel 4.2 (setelah `outro_frames`):

```
| `max_quiet_s` | Opsional, bawaan `6.0`. Rentang terpanjang (detik) tanpa perubahan visual sebelum `build_timeline.py` menolak build. Perubahan visual = event masuk/keluar, item/klik/stabilo muncul di dalam event, atau zoom pembicara berganti. Kata subtitle tidak dihitung. Outro tidak dihitung. Waktu di atas footage bergerak (`clip`, atau `split` dengan `src` video) tidak pernah dihitung sepi. Lihat 4.6 |
| `quiet_ok` | Opsional: `[{"from": <jangkar>, "to": <jangkar>, "why": "<alasan>"}]`. Menyatakan bahwa rentang tanpa perubahan visual di situ memang disengaja. `why` wajib. Lihat 4.6 |
```

Bagian baru:

```
### 4.6 Rentang sepi: `max_quiet_s` dan `quiet_ok`

Video tidak boleh lama diam secara visual. Setiap kali dijalankan, `build_timeline.py` menghitung semua rentang di antara dua perubahan visual
(event masuk/keluar, item `chips`/`bubbles` muncul, `click_at`/`x_at`, stabilo screenshot, zoom pembicara). Kata subtitle tidak dihitung.
Waktu di atas footage BERGERAK (insert `clip`, atau `split` dengan `src` video) tidak pernah dihitung sepi, karena gambarnya bergerak dan
memperlihatkan sesuatu. Hitungan mulai lagi dari nol saat footage itu selesai. Insert DIAM (`photo`, `screenshot`, `custom`) yang ditahan lebih lama
dari batas tanpa item/stabilo/klik baru tetap dihitung sepi.
Laporan `QUIET CHECK` dibaca setiap kali: jumlah perubahan, rata-rata panjang rentang, rentang terpanjang, porsi layar penuh / split /
pembicara+overlay / pembicara saja, dan setiap rentang yang lebih panjang dari `max_quiet_s` (bawaan 6 detik) beserta kalimat yang diucapkan di situ.

Rentang yang terlalu panjang membuat build GAGAL sampai diputuskan. Ini KEPUTUSAN, bukan kuota:
- Kalimatnya punya sesuatu yang bisa diperlihatkan → tambah visual yang menggambarkan kalimat itu (insert, `split`, item `chips`, klik, stabilo).
  Bukan hiasan untuk memenuhi angka.
- Pembicara saja memang paling tepat (cerita pribadi, momen emosional, wajah dan ekspresi adalah isinya) → tulis entri `quiet_ok`:

    "quiet_ok": [{"from": ["A", 66], "to": ["A", 116, 0, "e"], "why": "cerita pribadi: ekspresi pembicara adalah isinya"}]

  Jangkarnya sama dengan jangkar event. Entri harus menutup rentang itu (toleransi 1 detik di kedua ujung). Pesan error sudah mencetak
  usulan jangkar dari kata pertama sampai kata terakhir rentang itu. Alasan yang sama ditulis juga di `work/visual_plan.md` atau `work/brief.md`.
- `max_quiet_s` hanya dinaikkan kalau brief memang meminta gaya yang lebih tenang. Tulis alasannya di `work/brief.md`.

Sebagai pembanding: dua editor referensi menjaga rentang pembicara-saja terpanjang di sekitar 2,5 sampai 7 detik. job01 v4 yang ditolak punya 16,5 detik.
```

## Pesan gagal (persis)

```
ERROR: 1 stretch(es) longer than 6s with no visual change. data.json NOT written.
  0:00.00-0:07.07 (7.1s, frames 0-212): "Halo semuanya, hari ini aku mau bahas 3 cara sederhana untuk menghemat uang setiap bulan."
      quiet_ok entry would be: {"from": ["A", 0], "to": ["A", 14, 0, "e"], "why": "..."}
  This is a DECISION, not a quota. For each stretch, either:
  - add a visual that SHOWS what is being said there (event, split, chips item, click, ...), or
  - if the bare speaker is right (e.g. a personal story where the face IS the content), add to work/edit.json
    "quiet_ok": [{"from": <anchor>, "to": <anchor>, "why": "<the reason>"}] covering the stretch (edit-json.md, quiet_ok).
```
`quiet_ok` tanpa alasan: `ERROR: quiet_ok entry {...} has no "why": write the reason the bare speaker is right there`
Basi: `WARNING: quiet_ok 0:10.50-0:13.83 covers no long quiet stretch (stale? remove it or fix its anchors)`

## Tes (`/home/user/jobs/_looktest`, file `work/edit.Q*.json`)

| Config | Hasil |
|---|---|
| `Qpass`: tema A, judul keluar di kata "3" (`["A",7,-3]`) | exit 0, data.json ditulis. Terpanjang 3,8 dtk; 9 perubahan; full 9% / split 0% / pembicara+overlay 70% / pembicara saja 20% ✔ |
| `Qfail`: judul dihapus → 0:00–0:07,07 pembicara saja (7,1 dtk) | exit 1, data.json tidak ada, pesan di atas dengan kalimatnya dan usulan jangkar ✔ |
| `Qok`: `Qfail` + `quiet_ok` A0..A14e dengan alasan | exit 0, rentang ditandai `quiet_ok ... <- why: ...` ✔ |
| `Qnowhy`: `why` kosong | exit 1 dengan pesan ✔ |
| `Qstale`: `quiet_ok` di rentang yang tidak sepi + `max_quiet_s: 8` | exit 0, WARNING basi, batas 8 terpakai ✔ |
| `render.sh vQ` dengan `Qfail` | Berhenti di build_timeline (exit 1), pesan terlihat di terminal, tidak ada render ✔ |
| Kalibrasi: salinan `job01/work/edit.json` + `tx` (di scratchpad, job01 tidak disentuh) | Gagal dengan 5 rentang: **16,5 dtk di 0:27,7–0:44,2** (sama dengan temuan v4 yang ditolak), 10,4 / 8,6 / 6,2 / 6,1 dtk. Full 15% / split 8% / overlay 21% / pembicara saja 55% ✔ |

Catatan:
- `edit.full.json` asli smoke-test (judul tampil 6,8 dtk, 4–209) sekarang GAGAL di gerbang ini (judul yang diam 6,8 dtk dihitung sepi). Kalau
  smoke-test dipakai lagi dengan kit baru: tambah `theme`, dan percepat akhir judul atau tambah `quiet_ok`. `video/src/data.json` di `_looktest` sekarang dari `Qpass`.
- Insert layar penuh yang statis dan lama (foto 8 dtk tanpa item) dihitung sepi. Footage bergerak (`clip`, `split` dengan video) TIDAK dihitung sepi
  (keputusan lead, diterapkan di Tambahan 3).
- Seluruh frame [0, awal outro) dicek, termasuk rentang di bawah insert layar penuh.

---

# Tambahan 3: keputusan lead + tes semua jenis event

## Keputusan yang diterapkan

- `on_accent` otomatis, `marker` opsional, WARNING kontras/italic: tetap seperti sebelumnya.
- **Gerbang sepi, footage bergerak**: `build_timeline.py` sekarang melewati setiap rentang yang berada di atas `clip` atau `split` dengan `src`.
  Awal dan akhir event itu sudah titik perubahan, jadi setiap rentang seluruhnya bergerak atau seluruhnya tidak, dan hitungan mulai lagi saat footage selesai.
  Laporan `QUIET CHECK` sekarang punya baris legenda:
  `(visual change = an event in/out, an item/click/highlight appearing, a speaker zoom change; subtitle words do not count; time on moving footage - clip, split with a video src - is never quiet; a static insert held long still is)`
  dan `screen time (moving footage N% of the talk): ...`. Teks field di Tambahan 2 sudah diperbarui.
- **WARNING bentuk huruf** (per face, dari `fc-list :family=<nama> style`):
  - `font_text` selalu tegak; `font_emph` tegak kalau `emph_style: "normal"`. Kalau family itu HANYA punya face italic:
    `WARNING: theme.font_emph 'Playfair Display' has ONLY italic faces installed: it will render italic although "normal" is asked. Install the upright files or choose another font.`
  - Kebalikannya (italic diminta, tidak ada face italic): `WARNING: theme.font_emph 'Poppins' has no italic face installed: Chrome will slant it artificially. ...`
  - Tes: Playfair normal → WARNING; Playfair sebagai `font_text` → WARNING; Poppins italic → WARNING; Playfair italic → tanpa WARNING ✔

Tes gerbang footage bergerak (`/home/user/jobs/_looktest/work/edit.move_{clip,split,photo}.json`, satu event 9,6 dtk di 0:07,1–0:16,7):
`clip` → exit 0 (terpanjang 2,5 dtk, moving 58%); `split` dengan video → exit 0; `photo` diam → exit 1, TOO QUIET 9,6 dtk dengan kalimatnya ✔

## Tes semua jenis event dengan aset asli

Aset disalin (job01 tidak diubah) ke `/home/user/jobs/_looktest/video/public/`: `shots/parcelin_site.png`, `photos/card_desain.jpg`, `card_finishing.jpg`,
`split_rekomendasi.jpg`, `logos/parcelin-icon.png`; `broll/crowd.mp4` = 7 dtk dipotong dari `bench01/work/ref/v2.mp4` @69 dtk (video jadi dengan subtitle
tertanam, jadi di panel terlihat wajah dan teks dari video itu; cukup untuk tes).
Config: `work/edit.allA.json` / `work/edit.allB.json` (tema B dengan `marker: #BFD3FF`). Urutan: bubbles → split contain (logo, caption, klik) → split video →
screenshot (SUMBER, 2 stabilo, scroll 300, klik) → chips → photo (num/label/sub) → clip (num/label/sub) → custom bars → split cover (caption) → outro (logo, handle, CTA).
Gerbang sepi lolos: terpanjang 2,8 dtk, 20 perubahan.
Still di entry+8 dan tengah setiap event (+klik, +akhir outro), lewat heavy lock.

Gambar yang dibuka:
- Tema A: `/home/user/jobs/_looktest/work/all_A.jpg` (23 still), zoom `/home/user/jobs/_looktest/work/all_A_zoom.jpg`, stabilo `/home/user/jobs/_looktest/work/all_A_hl.jpg`
- Tema B: `/home/user/jobs/_looktest/work/all_B.jpg` (15 still), zoom `/home/user/jobs/_looktest/work/all_B_zoom.jpg`
- Strips: `/home/user/jobs/_looktest/work/strips_v1_0.jpg` (`sheet.py strips out/final_v1.mp4`, data.json dibangun ulang dari config render v1 + `quiet_ok`)

| Event | Tema A (oranye, Poppins tegak) | Tema B (biru, Jakarta + Playfair italic) |
|---|---|---|
| `bubbles` | Bubble putih, teks gelap, thumbnail foto; tidak memakai token tema. Rapi | Sama, bubble kedua kanan rapi |
| `split` contain + klik | Panel `LIGHT` krem, logo utuh dengan ruang, caption terbaca, kursor di logo | Panel `LIGHT` biru pucat, sama baiknya |
| `split` video | Panel atas memutar footage, caption pill terbaca | Sama |
| `screenshot` | Tag SUMBER oranye + teks ink (on_accent) terbaca. Stabilo oranye gelap (tanpa `marker`, build memberi WARNING): teks halaman yang hitam masih terbaca karena hitam, tapi berat. WARNING-nya pantas. Klik di "Lihat Produk" OK, scroll OK | Tag SUMBER biru + teks putih terbaca. `marker #BFD3FF` di atas halaman oranye → abu-lila tipis, teks jelas |
| `chips` | Lingkaran oranye, angka gelap | Lingkaran biru, angka putih |
| `photo` | Num "01" oranye Poppins, label putih, sub pill putih | Num "01" Playfair italic biru, label putih |
| `clip` | Num "02" oranye + label putih di footage gelap: terbaca | Num "02" biru di footage gelap: kontras lebih rendah tapi terbaca (ada bayangan) |
| `custom bars` | Latar krem, batang penting oranye, teks ink | Latar biru pucat, batang biru, teks navy |
| `split` cover | Foto + caption terbaca | Sama |
| `outro` | Logo di lingkaran putih, handle putih, CTA oranye + teks gelap terbaca | CTA biru + teks putih terbaca |
| `title` (tes sebelumnya) | Highlight oranye + teks ink | Highlight biru + teks putih, Playfair italic |

Tidak ada kuning kit di mana pun. Kuning yang terlihat adalah isi klip tes (bar kuning/biru) dan rumah L'Oréal kuning di screenshot asli.
Tata letak tidak rusak di kedua tema. Tidak ada perbaikan kode yang dibutuhkan dari tes ini.

Temuan lama (bukan dari tema; tidak diubah, sebaiknya jadi catatan di guide):
- `photo` sangat terang (card_desain abu-putih): label putih "KURANGI JAJAN" kontrasnya lemah walau ada bayangan. Pilih foto/`pos` dengan atas yang lebih gelap, atau `dim`.
- Aksen gelap (biru) sebagai `num` di atas footage gelap kontrasnya lebih rendah daripada aksen terang. Masih terbaca; tidak ada WARNING.

## Masih belum diverifikasi

- Render penuh dengan semua jenis event (hanya still; render penuh hanya config smoke-test tema A).
- `x_at` (silang merah di bubble) tidak tertangkap di still (muncul di antara frame yang dirender); tidak memakai token tema.
- Tema dengan `light` gelap (panel gelap) tidak dites.
