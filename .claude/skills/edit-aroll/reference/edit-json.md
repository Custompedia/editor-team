# Bagian 4. Referensi `work/edit.json`

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
