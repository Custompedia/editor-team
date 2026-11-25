# Bagian 4. Referensi `work/edit.json`

### 4.1 Contoh lengkap

Contoh bentuk `edit.json` (file `work/edit.example.json` di kit). Salin menjadi `work/edit.json` lalu ganti isinya.

**Ini contoh format, bukan resep.** Contoh ini memakai hampir semua jenis event supaya setiap field terlihat. Video nyata memakai
jenis yang dibutuhkan kalimatnya saja (`visual-thinking.md`). Blok `theme` di contoh sengaja ditolak build (alasannya diawali
`CONTOH`): tampilan diputuskan per video (4.5).

<!-- file: work/edit.example.json -->
```json
{
  "fps": 30,
  "clips": {"A": "take1", "B": "take3"},
  "theme": {"accent": "#2F6FED", "light": "#F5F5F7", "ink": "#1D1D1F", "font_text": "Plus Jakarta Sans", "font_emph": "Plus Jakarta Sans", "emph_style": "normal",
            "why": "CONTOH, ganti dengan alasanmu: aksen = warna tombol utama di situs brand; font = font situs brand (terpasang sebagai font sistem)"},
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
  "max_quiet_s": 6.0,
  "quiet_ok": [{"from": ["B", 60], "to": ["B", 98, 0, "e"], "why": "cerita pribadi soal gaji pertama: ekspresi pembicara adalah isinya, visual malah mengganggu"}],
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
| `theme` | **Wajib, tanpa bawaan.** Tampilan video ini: `accent` (warna kata besar, stabilo, angka chip, batang penting), `light` (latar panel/diagram terang), `ink` (teks gelap), `font_text` (font subtitle dan UI), `font_emph` (font kata besar, judul baris 2, angka label; boleh sama dengan `font_text`), `emph_style` (`"italic"` atau `"normal"`), `why` (alasan pilihan, sama dengan yang ditulis di `work/brief.md`). Opsional: `on_accent` (warna teks di atas isian aksen; bawaan dihitung otomatis: `ink` atau putih, mana yang lebih kontras), `marker` (warna stabilo screenshot; bawaan `accent`, wajib terang karena dicampur multiply). Lihat 4.5 |
| `segments` | Bagian yang dipakai, **dalam urutan tampil**: `clip`, `in`, `out` (detik di klip sumber). Segmen dari klip yang sama tidak boleh saling tumpang tindih |
| `framing` | Per klip: `scale`, `x`, `y` (piksel) supaya wajah berada di posisi yang sama di semua klip |
| `timing` | Koreksi waktu kata: `{"A": {"<indeks>": [mulai, selesai]}}` |
| `text` | Koreksi teks per kata: `"*kata"` = kata besar, `""` = disembunyikan, teks lain = pengganti |
| `script` | Menulis ulang satu rentang sekaligus: `{"from": <indeks kata pertama>, "text": "..."}`. Satu token per kata Whisper. `_` menyembunyikan kata, `~` adalah spasi di dalam satu token (`Rp10~juta`) |
| `keep_case` | Kata yang huruf besarnya dipertahankan di subtitle |
| `sub_max_chars`, `sub_max_words` | Panjang maksimum satu potong subtitle. Default 24 karakter, 4 kata |
| `outro_frames` | Frame tambahan setelah segmen terakhir untuk kartu penutup. 45 sampai 75 |
| `max_quiet_s` | Opsional, bawaan `6.0`. Rentang terpanjang (detik) tanpa perubahan visual sebelum `build_timeline.py` menolak build. Perubahan visual = event masuk/keluar, item/klik/stabilo muncul di dalam event, atau zoom pembicara berganti. Kata subtitle tidak dihitung. Outro tidak dihitung. Waktu di atas footage bergerak (`clip`, atau `split` dengan `src` video) tidak pernah dihitung sepi. Lihat 4.6 |
| `quiet_ok` | Opsional: `[{"from": <jangkar>, "to": <jangkar>, "why": "<alasan>"}]`. Menyatakan bahwa rentang tanpa perubahan visual di situ memang disengaja. `why` wajib. Lihat 4.6 |
| `cut_ok` | Opsional: `[{"join": <n>, "why": "<alasan>"}]`. `join` n = sambungan antara segmen ke-n dan ke-(n+1) (mulai dari 1). Menyatakan bahwa sambungan itu boleh memperlihatkan pembicara di kedua sisinya. Tanpa entri ini `build_timeline.py` menolak build (CUT CHECK): hapus potongannya, atau tutup dengan insert layar penuh yang sudah penuh ≥7 frame sebelum sambungan dan masih ada ≥6 frame sesudahnya. `why` wajib dan harus alasan gambar (pindah tempat, pergantian bagian yang memang terlihat), bukan "audionya bersih" |
| `music` | `{"src": "music/bed.mp3", "volume": 0.06, "points": [{"at": <jangkar>, "v": 0.4, "ramp": 6}, ...]}`. Dipertimbangkan di setiap video (`workflow.md` 6.2, Musik). `points` opsional: di tiap titik volume lagu bergerak ke `v` kali volume dasar selama `ramp` frame (turun di belokan, kembali, naik sedikit di penutup). Satu lagu saja; laporan build mencetak "music points" |
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
| `chips` | `items`: `at`, `n` (opsional), `text`; opsional `top` (bawaan 140), `step` (bawaan 138), `scale` (bawaan 1) | Poin bernomor yang muncul saat disebut. Kalau tumpukan menyentuh wajah (pembicara mendekat ke kamera), kecilkan dan naikkan dengan `top`/`step`/`scale`, lalu cek still di item terakhir |
| `mood` | `gray` (0..1, bawaan 1), `dim` (0..1, bawaan 0.3) | Lapisan PEMBICARA menjadi abu-abu/lebih gelap selama rentang (belokan nada). Insert, overlay, dan subtitle tetap berwarna. Tanpa sfx. Paling banyak di belokan utama (`visual-thinking.md` 2.0) |

Insert layar penuh:

| `type` | Field | Dipakai untuk |
|---|---|---|
| `photo` | `img`, `label`, `num`, `sub`, `pos`, `dim` (semua opsional kecuali `img`) | Foto asli atau gambar buatan, zoom pelan |
| `clip` | `src`, `from` (detik), `label`, `num`, `sub`, `pos`, `dim` | Footage B-roll atau rekaman layar, tanpa suara |
| `screenshot` | `img`, `img_w`, `img_h`, `source` (opsional: label "SUMBER" + teks), `highlights` [`x`,`y`,`w`,`h`, `at`], `scroll`, `click` {`x`,`y`}, `click_at` | Halaman asli sebagai kartu. Stabilo, scroll, dan kursor yang mengklik. `highlights[].at` = frame sejak awal event (bukan jangkar; bawaan 20, 46, 72...): hitung dari laporan build |
| `custom` | `name` + field bebas | Diagram SVG sendiri. Tersedia: `bars`; `timeline` (`label`, `event`, `months`, `after`, `items`: `at`, `from`, `text`: garis "N bulan sebelum <event>", batang tumbuh mundur dari event saat tiap rentang disebut); `igprofile` (kartu penutup akun Instagram dari screenshot user: `avatar`, `handle`, `verified`, `full_name`, `stats` [[angka, label]], `role`, `bio` [baris; kata `@akun` ditebalkan], `link`, `tiles` [gambar, baris berisi 3], `row2_at`). `page` (halaman ASLI satu layar penuh, bukan kartu: `img`, `img_w`, `img_h`, `light`, `scroll_to` px gambar + `scroll_at` + `scroll_dur`, `mark` {x,y,w,h} + `mark_at` = garis bulat di sekeliling bagian yang disebut, `tap` {x,y} + `tap_at` = titik sentuh gaya HP); `gallery` (beberapa foto ASLI muncul satu per satu di panel terang: `cols`, `top`, `ratio`, `gap`, `zoom`, `items`: `at`, `img`, `pos`); `measure` (foto ASLI dengan garis ukur yang digambar saat ukurannya disebut: `img`, `pos`, `items`: `at`, `x1`,`y1`,`x2`,`y2`); `igpage` (profil Instagram milik pemilik video yang DIBANGUN DENGAN KODE dari screenshot-nya, hanya atas permintaan pemilik, `visual-thinking.md` 3: `c` warna dari pixel screenshot, `avatar`, `handle`, `verified`, `full_name`, `stats`, `role`, `bio` [{`emoji` crop asli, `parts`}], `links`, `follow`, `message`, `highlight`, `tiles` [12 crop asli], `tap_at`, `hl_at` cincin lembut di tombol pesan, `push_at`, `hold_end`; `font` harus font sistem). **`name` dipakai kit untuk memilih komponen**: data isi tidak boleh memakai field bernama `name` (pakai `full_name` dan sejenisnya) |
| `custom` (job04/05) | `name`: `compare`, `range`, `swatches`, `closing` | `compare` (SATU foto asli besar di panel terang + satu lencana vonis di katanya: `img`, `pos`, `label`, `sub`, `color`, `stamp_text`, `stamp_kind` "ok"/"no", `stamp_at`); `range` (rentang angka di penggaris, digambar saat diucapkan: `unit`, `min`, `max`, `ticks`, `from`, `to`, `from_at`, `to_at`, `unit_at`, `from_text`, `to_text`, `band_text`, `note_text`, `note_at`); `swatches` (deret ubin contoh yang muncul saat disebut: `items` [`at`, `img`, `text`, `hi_at` = sorotan pindah ke ubin itu di katanya], `bracket_text`, `bracket_at`, `logo`, `logo_text`, `logo_at`; ubin hasil olahan kode wajib diberi `sub` "ilustrasi …"); `closing` (penutup brand di panel terang: file logo ASLI + `handle`, `line` opsional, pakai dengan `hold_end`). `color` = warna penekanan di panel terang bila aksen theme terlalu pucat di sana |
| `comment` | `text`, `top`, `mark_at`, `mark_color`, `x_at`, `reply` | Kartu komentar BUATAN di atas pembicara, HANYA atas perintah pemilik video (job05). Nama dan avatar buram sejak frame pertama, tidak pernah ada nama rekaan; `text` = kalimat yang dikutip pembicara. `mark_at` = cincin di nama buram ("aku sensor namanya"), `x_at` = stempel X. Komentar asli (screenshot dari user) tetap lebih baik: pakai `screenshot` |
| `outro` | `img`, `logo`, `handle`, `cta` | Kartu penutup |

`photo` atau insert lain yang mulai di frame 0 tampil penuh sejak frame pertama (tanpa fade), supaya video tidak dibuka dengan frame setengah jadi.

Field `"sfx": false` pada event mana pun mematikan bunyi masuknya (pemilik: jangan berlebihan; hanya bunyi yang menandai sesuatu). `tap_at` pada `page`/`igpage` memberi bunyi klik pelan seperti `click_at`.

Caption di atas insert layar penuh yang terang (`light: true`) otomatis diberi latar tenang berwarna panel supaya terbaca di atas halaman yang ramai.

Field `hold_end: true` pada insert layar penuh terakhir (kartu penutup yang berjalan sampai `"end"`) mematikan fade keluar, supaya frame terakhir video bukan frame setengah pudar.

Field `light: true` pada insert layar penuh berarti latarnya terang (pada `photo`, gradasi gelap di atas juga dimatikan): subtitle berubah gelap dan gradasi gelap di bawah dimatikan. `custom` otomatis `light` (diagram bawaan berlatar terang). Tulis `"light": false` kalau komponen buatanmu berlatar gelap, dan `"light": true` pada `photo` yang hampir putih.

Layar terbagi (visual di atas, pembicara tetap terlihat di bawah):

| `type` | Field | Dipakai untuk |
|---|---|---|
| `split` | `img` atau `src` (video, dengan `from`), `h` (tinggi panel, default 760), `shift` (pembicara turun berapa piksel, default 300, tidak boleh lebih dari `h`), `fit` (`"cover"` default, `"contain"` untuk logo dan tampilan aplikasi), `bg` (warna panel), `pos`, `caption`, `click` {`x`,`y`} dalam piksel **panel** + `click_at` | Hal yang dilihat sambil tetap melihat pembicara: logo, aplikasi, foto, klip |

Panel masuk dari atas sementara pembicara turun bersamaan, dan kembali dengan cara yang sama. Subtitle ikut turun. Panel boleh bersentuhan dengan panel lain (melebur) atau dengan insert layar penuh (berganti saat tertutup), tetapi tidak boleh tumpang tindih. Jangan menaruh overlay (`title`, `bubbles`, `chips`) pada waktu yang sama dengan panel.

Dua insert berantai: tulis jangkar yang persis sama untuk `end` insert pertama dan `start` insert kedua. Berlaku juga untuk dua panel `split`, dan untuk panel yang disambung insert.

### 4.4 Menambah visual sendiri

Baca dulu kebijakan kode di `visual-thinking.md` Bagian 5 dan tulis alasan satu kalimat di `work/visual_plan.md`. Kalau satu kalimat butuh visual yang belum ada dan tidak ada aset nyata yang bisa memperlihatkannya (garis waktu, perbandingan dua kolom, diagram ukuran), atau butuh cara menyajikan aset nyata yang belum ada di kit (`visual-craft.md` 9), tulis komponen baru di `Visuals.tsx` dan daftarkan di `CUSTOM`:

```tsx
const Timeline: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();                       // 0 = frame pertama insert ini
  const draw = interpolate(f, [6, 30], [1, 0], {...cl, easing: ease});
  const hi = e.color || ACCENT;
  return (
    <AbsoluteFill style={{background: LIGHT}}>
      <Label ink label={e.label} sub={e.sub} />
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path d="M140 900 H940" stroke={INK} strokeOpacity={0.2} strokeWidth={8} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={draw} />
        {e.points.map((p: any, i: number) => {
          const g = sp(f, 14 + i * 10);
          const x = 140 + (800 * i) / (e.points.length - 1);
          return (
            <g key={i} opacity={g}>
              <circle cx={x} cy={900} r={18 * g} fill={i === e.points.length - 1 ? hi : INK} />
              <text x={x} y={840} textAnchor="middle" fontFamily={SERIF} fontStyle={EMPH_STYLE} fontWeight={800} fontSize={44} fill={INK}>{p.year}</text>
              <text x={x} y={970} textAnchor="middle" fontFamily={SANS} fontWeight={600} fontSize={30} fill={INK} opacity={0.6}>{p.text}</text>
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
- Pakai `SANS`, `SERIF` (font penekanan, belum tentu serif) dengan `fontStyle: EMPH_STYLE`, `LIGHT`, `INK`, `ACCENT`, `ON_ACCENT` dari `theme.ts`. Nilainya datang dari `theme` di `edit.json`; jangan menulis warna atau font sendiri di komponen. Isi teks dan angka datang dari `edit.json`, bukan ditulis di komponen. Warna latar diagram mengikuti look video; satu warna penekanan untuk hal yang paling penting.
- Satu diagram satu gagasan, sedikit elemen, banyak ruang kosong: diagram yang ramai tidak terbaca di HP.
- Area aman: konten utama di y 150 sampai 1200. Area y 1270 sampai 1530 milik subtitle. Di bawah 1530 tertutup antarmuka aplikasi.
- Setelah menulis: `npx tsc --noEmit -p .` di `video/`, lalu still di tiga titik (awal, tengah, akhir insert).

### 4.5 `theme`: tampilan diputuskan per video

Tidak ada tampilan bawaan. `build_timeline.py` berhenti kalau `theme` tidak ada, kalau isinya salah, atau kalau `why` masih teks contoh.
Bentuknya (nilai di bawah hanya tempat isian; build menolaknya sampai diganti):

    "theme": {"accent": "#RRGGBB", "light": "#RRGGBB", "ink": "#RRGGBB",
              "font_text": "<nama family terpasang>", "font_emph": "<nama family terpasang>", "emph_style": "normal",
              "why": "<alasan: dari brand / footage / nada isi, sama dengan di work/brief.md>"}

- Putuskan dengan cara di `visual-thinking.md` Bagian 6. Tulis pilihan dan alasannya di `work/brief.md`, lalu salin alasannya ke `why`.
- Warna ditulis hex `#RRGGBB`. Font ditulis satu nama family persis seperti dicetak `fc-list : family` (tanpa kutip, tanpa `sans-serif`).
- Font harus terpasang sebagai font SISTEM: taruh `.ttf/.otf` statis di `/home/user/editkit/fonts`, jalankan `bash /home/user/editkit/tools/install_fonts.sh` (mencetak nama family yang tersedia). Jangan pernah memuat web font.
- `emph_style: "italic"` hanya kalau `font_emph` punya file italic. Tanpa file italic, build memberi WARNING karena Chrome memiringkan huruf secara palsu; family yang hanya punya file italic juga diberi WARNING bila diminta `"normal"`.
- Aksen gelap: teks di atas aksen otomatis putih. Kalau video memakai stabilo screenshot, isi `marker` dengan versi pucat aksen (build memberi WARNING kalau terlalu gelap).
- Diagram `bars` memakai `accent` untuk batang penting; tulis `color` di event kalau aksen kurang terbaca di atas `light`.
- Mengganti tampilan = mengubah `theme` lalu menjalankan ulang `build_timeline.py`. Jangan menulis warna atau font di `theme.ts` atau komponen.

### 4.6 Rentang sepi: `max_quiet_s` dan `quiet_ok`

Video tidak boleh lama diam secara visual (permintaan pemilik). Setiap kali dijalankan, `build_timeline.py` menghitung semua rentang di antara dua perubahan visual
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
  usulan jangkar dari kata pertama sampai kata terakhir rentang itu. Alasan yang sama ditulis juga di `work/visual_plan.md`.
- `max_quiet_s` hanya dinaikkan kalau brief memang meminta gaya yang lebih tenang. Tulis alasannya di `work/brief.md`.

Sebagai pembanding: dua editor referensi menjaga rentang pembicara-saja terpanjang di sekitar 2,5 sampai 7 detik. job01 v4 yang ditolak punya 16,5 detik.
