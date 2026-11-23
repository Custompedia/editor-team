> **Arsip bukti, bukan bacaan worker.** Salinan dari `/home/user/jobs/bench01/work/BENCHMARK_NOTES.md` (2026-11-23). Isinya sudah
> diserap ke `.claude/skills/edit-aroll/reference/visual-thinking.md` dan `visual-craft.md`; tes untuk lead ada di `docs/review-tests.md`.
> Path gambar di bawah relatif ke `/home/user/jobs/bench01/work/` (tidak ada di repo). Rujukan ke `style-notes.md`, `STYLE_NOTES` dan
> `CLAUDE.md` lama di dalam teks adalah sejarah: file style-notes sudah dihapus dari skill (lihat `parcelin-study.md`).

# BENCHMARK_NOTES — sintesis 3 video benchmark (@raymondchins) + cek silang dengan studi Parcelin

Ditulis 2026-11-23 dari `notes_v1.md`, `notes_v2.md`, `notes_v3.md`, `STUDY_BRIEF.md`, `skillwork/ACCEPTANCE.md`,
`edit-aroll/reference/style-notes.md` (Parcelin + job01 v4) dan `edit-aroll/reference/edit-json.md`.
Semua path gambar relatif ke `/home/user/jobs/bench01/work/`. Klaim yang dinaikkan jadi prinsip sudah dicek ke gambarnya
(daftar gambar yang saya buka sendiri ada di bagian 8).

Singkatan: **v1** = solo, AI di kantor (58,6 s) · **v2** = solo, DBL (90,4 s) · **v3** = dua orang, AXE vs Chanel (90,1 s) ·
**PH** = Parcelin Hardbox ref (128 s) · **PL/PM** = Parcelin Lebaran / MOQ · **job01 v4** = edit kita yang ditolak.

Ini **keputusan**, bukan tampilan. Warna, font, bentuk chip, gaya highlight = pilihan per video (lihat bagian 2).

---

## 1. Keputusan yang sama di ketiga video benchmark

| # | Aturan keputusan | Kenapa berhasil untuk penonton | Bukti (video · detik · gambar) |
|---|---|---|---|
| D1 | **Visual muncul tepat di kata yang ia gambarkan** (kata benda, nama, angka), bukan di awal kalimat dan bukan "sekitar" | Mata dan telinga menerima hal yang sama di saat yang sama → tidak ada beban mencocokkan | v1 33,1/33,9/34,3/35,1 logo Sheets/Drive/Meta tepat saat disebut (`ref/strips/v1_29_card_icons.jpg`); v2 Harian Surabaya tepat di "Honda" 62,98 (`ref/v2/strip17_sponsor_harian_f1778.jpg`); v3 billboard tepat di "AXE" 6,60, Coca-Cola tepat di "Coca" 43,0, artikel di "73" 28,0 (`ref/v3/strips/s03_mosaic_to_clear.jpg`, `s13_samsung_coke.jpg`, `s10_article_in.jpg`) |
| D2 | **Klaim/angka/fakta → bukti nyata** (halaman berita, grafik resmi, foto/footage asli) dengan **kalimat yang diucapkan** dibuat menonjol | Penonton tidak perlu percaya pembicara; mereka melihat sumbernya | v1 headline Bloomberg Technoz 0–4,8 (`ref/frames/v1_t005_headline.jpg`); v2 9 dokumen, mis. Student Athlete 36,4 stabilo (`ref/v2/full/f01150.jpg`); v3 paragraf "73 percent…" stabilo biru (`ref/v3/full/f870.jpg`) |
| D3 | **Satu fokus per layar**: yang tidak dibicarakan diredam (pudar, blur, B&W, keluar frame), bukan dibiarkan bersaing | HP kecil; mata harus tahu ke mana dalam <1 s | v1 bagian prompt aktif tajam, sisanya pudar+blur (`ref/frames/v1_t165_chatui.jpg`); v2 paragraf lain blur di Student Athlete/Harian, harga lain pudar di seat plan (`ref/v2/full/f01150.jpg`, `f01950.jpg`, `f00430.jpg`); v3 hanya satu paragraf, satu frasa distabilo (`ref/v3/full/f870.jpg`) |
| D4 | **Wajah tidak pernah ditutup** oleh overlay; overlay ditaruh di ruang kosong komposisi (dada, headroom, samping kepala) | Wajah = kontak dan emosi; kalau tertutup, layar terasa "slide" | v1/v2 kartu headline di bawah dagu (`ref/frames/v1_t005_headline.jpg`, `ref/v2/full/f00060.jpg`); v3 panel di headroom wide shot (`ref/v3/full/f630.jpg`) |
| D5 | **Tidak ada jeda sepi panjang**: gambar berubah paling lambat tiap ±4 s (v1 ≤2,5 s, v2 run pembicara terpanjang 4,1 s, v3 shot terpanjang 4,1 s) | Ritme vertikal: penonton swipe saat layar diam | tabel bagian 3; v3 `ref/v3/hardcuts.txt` (79 cut / 90 s) |
| D6 | **Kalau tidak ada benda untuk ditunjukkan, perubahan datang dari kamera/teks, bukan grafik palsu**: punch-in, ganti angle, teks kinetik besar, close-up blur | Ritme tetap hidup tanpa memaksakan visual yang tidak jujur | v1 teks besar + close-up blur 11,2 / 19,4 (`ref/v1/v1_11_bigsub_ui1.jpg`); v2 punch-in hook + shot dekat 50,4 (`ref/v2/strip01_hook_f0.jpg`, `ref/v2/full/f01530.jpg`); v3 ±10 punch-in, 3 angle (`ref/v3/strips/s18_tilted_sub.jpg`) |
| D7 | **Pembicara kembali untuk opini, pertanyaan, sambungan, emosi, punchline** — informasi ditunjukkan, pendapat diucapkan ke kamera | Wajah memberi bobot pada pendapat; bukti memberi bobot pada fakta | v1 "padahal yang seharusnya", "menyeramkan banget" (`ref/strips/v1_54_ending.jpg`); v2 "gua ulangin ya", "let's be honest", "dapat duit dari mana?" (notes_v2 E); v3 Q&A 50,9–57,9 |
| D8 | **Penanda nada (tonal turn) = perubahan "dunia" gambar yang murah dan singkat**: B&W, flash, warna merah pada kata, color bar | Penonton merasakan belokan tanpa membaca | v2 B&W "tapi gilanya" 11,2, "liga pelajar" 20,8 (`ref/v2/strip14_bw_billboard_f330.jpg`, `strip07_bw_liga_f598.jpg`); v3 B&W "GW BOONG" + color bar (`ref/v3/strips/s06_bw_bars_17s.jpg`); v1 kata merah "menyeramkan" 56,2 (`ref/strips/v1_54_ending.jpg`) |
| D9 | **Teks/caption berganti mode menurut apa yang ada di belakangnya** (lihat 4c) | Keterbacaan + hierarki: di atas bukti, caption mengecil supaya bukti jadi fokus | v1 caption kotak kecil di insert vs teks besar di wajah (`ref/sheets/v1_sheet_0.jpg`); v2 chip kecil vs teks besar (`ref/v2/fullgrid_types.jpg`); v3 caption hilang saat judul serif tampil, judul pindah ke zona caption saat panel atas aktif (`ref/v3/strips/s07_newyork_title.jpg`) |
| D10 | **Konsep abstrak tanpa wujud asli → tipografi atau diagram monokrom minimal, bukan UI/ilustrasi buatan** | Jujur dan cepat dibaca; tidak ada yang terlihat palsu | v1 diagram 10→100 hitam-putih (`ref/strips/v1_51_diagram.jpg`); v3 judul serif "Upward / COMPARISON", "Social / Proof" (`ref/v3/full/f1500.jpg`); v2 hanya counter angka (`ref/v2/strip13_counter_f160.jpg`) |
| D11 | **Hook: frame 0 sudah berisi sesuatu yang menyebut topik/bukti** (headline asli, atau cold open) — tidak ada layar kosong, tidak ada judul buatan sendiri di v1/v2 | Detik pertama menjawab "kenapa saya harus nonton" | v1 headline di frame 0 (`ref/strips/v1_00_open.jpg`); v2 headline + logo di frame 0 (`ref/v2/strip01_hook_f0.jpg`); v3 cold open "BDSM PA" + color bar (`ref/v3/strips/s01_open_bdsm_bars.jpg`) |
| D12 | **Durasi = waktu yang dibutuhkan penonton**: dokumen dibaca 2,5–5 s, b-roll rasa 1–2,5 s, logo/perbandingan ±1–1,3 s, tidak ada gambar diam >5 s tanpa gerak internal | Cukup untuk menangkap, tidak cukup untuk bosan | v1 UI 5,5 s berisi pan+penanda; v2 dokumen rata-rata 3,3 s, footage 1,3–2,4 s; v3 Apple/Samsung 1,33 s, Coke/Pepsi 1,27 s |

---

## 2. Yang berbeda antar video (= pilihan per video, bukan aturan)

| Dimensi | v1 | v2 | v3 | Pendorong perbedaan |
|---|---|---|---|---|
| Pembicara disembunyikan | ±52% | ±67% | ±1% (hanya color bar) | **Jumlah orang + jenis konten.** Solo + topik demonstrasi/bukti → layar penuh. Dua orang → reaksi adalah hiburannya, jadi wajah tak pernah ditutup |
| Bentuk "bukti" | 1 headline + UI asli | 9–10 dokumen berita | 1 paragraf kecil + footage iklan asli | Topik: v2 klaim bisnis berbasis data publik; v1 tutorial alat; v3 bedah iklan (bukti = iklannya sendiri) |
| Penempatan visual saat wajah tampil | lower-third, logo di samping kepala | lower-third, logo **di belakang** kepala | **panel atas di headroom** | **Framing/headroom**: v3 wide shot direkam dengan dinding kosong ±38% atas; v1/v2 medium shot dengan dada sebagai ruang bebas |
| Latar dokumen layar penuh | panggung putih-vinyet netral untuk semua insert | footage/foto terkait yang digelapkan, atau kertas abu vinyet | tidak ada (tidak ada dokumen layar penuh) | Banyaknya dokumen: v2 butuh variasi, v1 butuh satu "papan tulis" |
| Caption di wajah | teks kinetik besar 2–3 tingkat, blur-in per kata, serif diketik | teks besar sans + serif italic aksen, opacity+blur per kata | 1 baris polos per frasa, hard swap; ekspresi hanya di momen emosi (miring, marquee, ketik) | Solo → teks harus "jadi visual"; dua orang → wajah dan cut sudah memberi gerak |
| Caption di atas insert | kotak hitam pekat persegi | chip bulat transparan | (tidak relevan) caps saat artikel | gaya |
| Transisi | flash putih, light-leak, blur→fokus | hard cut, flash/bloom, fade hitam, blur-in | hard cut + color bar gag | nada: v3 komedi TV, v1/v2 opini-edukasi |
| Penanda nada | kata merah, close-up blur | B&W ×2 | B&W ×3, color bar ×2, beep | komedi = lebih sering |
| Penutup | wajah + kata merah, tanpa CTA | wajah + pertanyaan ke penonton + logo DBL, tanpa CTA | montase B&W tertawa, tanpa CTA | Tujuan: kreator opini (bukan jualan). **Parcelin = showcase brand layar penuh + CTA** karena tujuannya jualan |
| Kepadatan cut kamera | 1 kamera + punch-in/close-up | 1 kamera + punch-in | 3 angle, cut tiap ±1,1 s | jumlah kamera di footage |

Pelajaran: proporsi layar penuh, posisi overlay, gaya caption, transisi dan penutup **diturunkan dari footage dan tujuan video**,
bukan disalin. Worker menulis alasannya di `work/brief.md`.

---

## 3. Cek silang lintas editor (benchmark vs Parcelin)

### 3a. Prinsip

| Prinsip | Benchmark (v1/v2/v3) | Parcelin (PH/PL/PM) | Verdict |
|---|---|---|---|
| Visual di kata yang digambarkan | 3/3 | ya (P16 "tepat di kata", offset −2…−4 f) | **CONFIRMED BY BOTH** |
| Klaim → bukti pihak ketiga, kalimatnya disorot | v1 headline (tanpa stabilo), v2 ×9 sapuan, v3 stabilo statis | JPNN + stabilo (P10), detik + callout | **CONFIRMED BY BOTH** |
| Wajah tidak ditutup overlay | 3/3 | ya (P2 bubble sepertiga atas, P4) | **CONFIRMED BY BOTH** |
| Rentang tanpa perubahan dibatasi | ≤2,5 / 4,1 / ±7 s (tanpa grafik, tapi cut tiap 1,1 s) | wajah saja ≤6–7 s; v4 ditolak dengan 16 s | **CONFIRMED BY BOTH** (+ owner, ACCEPTANCE 6) |
| Tidak ada visual untuk opini/sambungan/ajakan; wajah kembali di sana | 3/3 | P12 | **CONFIRMED BY BOTH** |
| Penanda punchline/nada (B&W/dim/zoom) 1–3× | v2, v3 ya; v1 pakai merah + close-up blur | P3 B&W 1–2× | **CONFIRMED BY BOTH** sebagai alat; jumlah 1–3 (komedi lebih) |
| Platform/aplikasi: tunjukkan ISI yang dibicarakan, besar, bukan bingkainya | v1 ChatGPT di-zoom ke kalimat | P9 grid pin besar, bukan header | **CONFIRMED BY BOTH** |
| Daftar → kanvas yang terisi bertahap / rantai, item muncul saat disebut | v1 prompt 1–4, logo satu per satu; v3 aspek 1/2/3 judul | P5 rantai, chips, panel bertambah | **CONFIRMED BY BOTH** |
| Konsep tanpa sumber nyata → diagram/teks minimal | v1 monokrom, v3 judul serif, v2 counter | P1 box3d, kurva, formulir (berwarna, lebih "dirancang") | **CONFIRMED** (ada), **DIFFERS** dalam kadar: benchmark jauh lebih minimal |
| Hook: topik/bukti di layar ≤0,5 s, perubahan kedua ≤3,5 s | frame 0 headline / cold open | judul 0,3 s, bubble 3 s | **CONFIRMED BY BOTH**; bentuk DIFFERS |
| Callback/bookend | v1 UI yang sama kembali 3×; v3 billboard callback + cold open | formulir kosong→terisi, bubble + silang | **CONFIRMED BY BOTH** |
| Napas wajah di antara visual kuat | v2 kembali 0,5–2,9 s antar dokumen | P12 1–3 s | **CONFIRMED BY BOTH** |
| Caption: satu sistem per video, warna aksen bermakna tetap | 3/3 (kuning=inti, merah=kaget/tabu) | P17 satu sistem, kata kunci diwarnai | **CONFIRMED BY BOTH**; bentuk DIFFERS |
| Caption menyesuaikan latar (keterbacaan) | mode kecil berkotak di insert, besar di wajah | warna caption dibalik di insert terang | **CONFIRMED** (keterbacaan); **ganti mode = DIFFERS** (gaya) |
| Punch-in/ganti angle sebagai beat tanpa grafik | 3/3 | hanya disebut sebagai opsi punchline (P3) | **ONLY ONE** editor, tapi 3/3 video → kuat; jadikan alat standar |
| Sisa dokumen diredam (blur/pudar) | v1, v2 | tidak | **ONLY ONE** (2 video) → dianjurkan |
| Kartu dokumen dengan bingkai/label "SUMBER"/mockup laptop | tidak pernah | ya (kartu kit, laptop PL) | **DIFFERS** → owner memilih **tanpa bingkai** (ACCEPTANCE/brief) |
| Latar di belakang dokumen | footage terkait digelapkan / kertas vinyet / blur-fill | kartu di latar blur | **DIFFERS** |
| Layar penuh maksimal 50% (P12 Parcelin) | v2 = 67% | 30–40% | **DIFFERS** → batas 50% BUKAN aturan; alasan konten yang menentukan |
| Chat bubble untuk kutipan orang lain | tidak ada (tidak ada kutipan pihak ketiga di ketiga video) | P2 | **ONLY ONE** editor, tetapi **dianjurkan owner** (ACC 10) → pakai setiap kali ada ucapan orang lain |
| Gerak masuk | blur-in, hard cut, flash | pop skala overshoot, geser, pegas | **DIFFERS** |
| Penutup layar penuh nyata + CTA | tidak pernah | ya (P14) | **DIFFERS** (tujuan jualan vs opini) |

### 3b. Angka kepadatan berdampingan

| Video | Durasi | Beat visual | s / beat | Pembicara tersembunyi | Pembicara + overlay | Pembicara saja (+caption) | Rentang terpanjang tanpa perubahan gambar | Rentang terpanjang tanpa elemen desain |
|---|---|---|---|---|---|---|---|---|
| v1 | 58,6 | ±30 | ±2,0 | ±52% | ±11% grafik + ±37% teks kinetik besar | ±0% | ≤2,5 s | ≤2,5 s (teks besar berganti tiap ±1 s) |
| v2 | 90,4 | ±35 | ±2,6 | ±67% | ±9% | ±24% (teks besar) | 4,1 s (penutup) | 4,1 s |
| v3 | 90,1 | ±31 (+79 cut kamera) | ±2,9 (cut tiap 1,14) | ±1% | ±25% (panel 17, judul 5, layer 3) | ±73% | 4,1 s (shot) | ±7 s (50,9–57,9) |
| PH | 128,4 | ±25 | ±5,1 | ±35% | tidak diukur | tidak diukur | — | 6–7 s |
| PL / PM | 53 / 94 | — | — | 30–40% + panel | — | — | — | — |
| job01 v4 | 112,3 | 13 | 8,6 | 15% (+8% split) | — | — | — | **16 s** |

Yang **dibuktikan** angka ini: semua edit yang owner pakai sebagai acuan menjaga "tanpa elemen desain" ≤7 s dan perubahan gambar
apa pun (cut, punch-in, visual) ≤±4 s; edit yang ditolak punya 16 s. Benchmark baru (2–3 s/beat) lebih padat dari Parcelin (5 s).
Yang **tidak** dibuktikan: (1) persentase layar penuh bukan target — 1% sampai 67% sama-sama diterima; (2) angka beat tidak sebanding
langsung: v1 menghitung penanda/pan/transisi, v3 tidak menghitung cut kamera, Parcelin menghitung insert/panel/overlay/efek →
ketidakpastian ±30%; (3) sampel kecil (2 editor, 6 video) dan korelasi, bukan sebab. Kit harus mengukur semua video kita dengan satu
definisi (lihat T1/T2) supaya angka kita sebanding antar job.

---

## 4. Topik fokus owner — sebagai penalaran yang bisa diterapkan

### 4a. Potongan berita/artikel

Tiga perlakuan, dipilih dari tiga pertanyaan: **apa yang harus DIBACA penonton? apakah WAJAH penting saat itu? di mana RUANG KOSONG?**

| Perlakuan | Kapan cocok | Bentuk | Bukti |
|---|---|---|---|
| **Strip headline di bawah dagu** (lower-third) | Hook/klaim pembuka; yang dibaca hanya judul ≤2 baris + nama media; kontak mata penting | Bar tipis berisi logo/nama media asli + kotak berisi judul + (byline/tanggal atau poin video 1 baris). Lebar ±80–88%, y ±62–75%, datar, sudut siku, tanpa bayangan. Ada sejak frame 0 atau masuk ≤0,4 s (blur→tajam). Caption kecil di bawahnya | v1 0–4,8 `ref/frames/v1_t005_headline.jpg`; v2 0–3,6 `ref/v2/full/f00060.jpg` |
| **Dokumen layar penuh + sapuan highlight + sisa diredam** | Penonton harus membaca **kalimat persis** (angka, kutipan); wajah tidak dibutuhkan 2,5–5 s; banyak klaim berurutan | 1–3 paragraf atau headline+byline; logo media/“source : …” terlihat; highlight menyapu kiri→kanan per baris **dengan kecepatan bicara** (boleh berhenti di tengah kata); kamera zoom/pan ke baris aktif sampai ±85% lebar (tepi boleh terpotong); paragraf lain opacity rendah + blur; masuk blur-in 6–16 f; keluar cut/flash/fade hitam | v2 #2–#10 (`ref/v2/full/f00520.jpg`, `f00780.jpg`, `f01150.jpg`, `f01720.jpg`, `f01950.jpg`, `ref/v2/strip08_headline_zoom_f680.jpg`); pola sama untuk UI di v1 (`ref/frames/v1_t165_chatui.jpg`) |
| **Crop paragraf kecil di headroom** | Wajah/reaksi adalah tontonannya; sumber cukup **terlihat ada**; angka dibawa caption | Hanya kotak paragraf (4 baris), lebar ±91%, y ±27–37%, tanpa logo, stabilo statis (biru seleksi browser), fade-in 7–8 f, keluar hard cut; caption merangkum ("73% COWOK") | v3 28,1–32,0 `ref/v3/full/f870.jpg` |

**"Hanya crop yang pas" dalam praktik**
- **Disimpan:** identitas sumber (logo/nama media; tanggal bila headline), baris yang memuat klaim yang diucapkan, dan sedikit
  konteks halaman (font asli situs) supaya terlihat nyata.
- **Dibuang:** perangkat, bar browser, tab, iklan, navigasi, foto artikel, komentar, label "SUMBER" buatan, bayangan, sudut bulat,
  rotasi. Paragraf lain boleh tetap ada **asal diredam** (v2) — itu memberi rasa "halaman asli" tanpa mencuri fokus.
- **Mata dituntun** oleh tiga hal berurutan: (1) highlight bergerak mengikuti mulut; (2) kamera pindah ke baris berikutnya saat
  pembicara pindah angka (v2 "1 jam" → zoom "47 jam" 19,2 s; lompatan zoom pada "15" 24,5 s); (3) semua yang lain lebih gelap/kabur.
- **Gaya highlight mengikuti latar:** latar gelap → kotak terang dengan teks dibalik gelap; latar terang → marker warna (multiply);
  di crop kecil → warna seleksi. Satu gaya per latar, bukan per selera.
- **Kejujuran:** dokumen gelap v1/v2 tampaknya diketik ulang (font seragam lintas media; tidak terbukti). Untuk kita: pakai crop
  screenshot asli; kalau harus diketik ulang demi keterbacaan, teksnya **verbatim** + logo media asli + URL dicatat. Jangan mengubah kata.
- **Kapan TIDAK pakai berita:** kalau bukti terbaik adalah bendanya sendiri (v3: footage billboard AXE lebih kuat dari artikel).

### 4b. Apa yang ada di belakang/sekitar potongan
- **Lower-third:** pembicara utuh, tidak di-dim/blur; boleh ditemani logo asli brand yang disebut di ruang kosong samping/ belakang
  kepala (v1 `ref/strips/v1_03_logos.jpg`; v2 `ref/v2/full/f00060.jpg`).
- **Layar penuh:** salah satu dari tiga, dipilih dengan alasan:
  1. **Footage/foto nyata yang menggambarkan kalimat**, digelapkan ±20–35% + sedikit blur → latar menguatkan isi (artikel dance di atas
     tim dance, kutipan pendiri di atas foto tokoh) — v2 `ref/v2/full/f01320.jpg`, `f01380.jpg`, `f00940.jpg`.
  2. **Kertas netral** (putih/abu dengan vinyet radial) → satu "panggung" untuk semua insert penjelasan supaya UI asli, ikon dan
     diagram terlihat satu sistem — v1 `ref/frames/v1_t345_aiicons.jpg`; v2 `ref/v2/full/f01150.jpg`.
  3. **Salinan aset yang sama diperbesar + blur** (blur-fill) untuk poster/grafik yang rasionya tidak 9:16 — v2 `ref/v2/full/f02380.jpg`.
- **Crop di headroom:** ruangan asli tetap; boleh satu lapisan tekstur yang **menggambarkan kalimat** ("bukti data" → kapur rumus,
  screen-blend) — v3 `ref/v3/strips/s09_chalk_math.jpg`.
- Tidak ada: gradient dekoratif, grid, bentuk bergerak, partikel. Gerak datang dari konten (highlight, zoom, pan), bukan dari latar.

### 4c. Caption/teks — yang konstan vs yang dipilih

**Konstan (aturan):**
- Selalu tampil dan sinkron dengan ucapan (frasa 1–5 kata; ganti tepat di frasa/cut), kecuali saat elemen lain **membawa kata yang sama**
  (judul serif v3, teks dalam diagram v1 51,8–54,1) — maka caption disembunyikan, tidak dobel.
- Posisi: tengah, di bawah dagu/di dada, **y ±54–80%** tergantung framing (v1 caption 73–80%, teks besar 55–75%; v2 60–74%; v3 54% CU,
  65–68% wide). Tidak pernah di mata/mulut; tidak di bawah ±80% (UI platform).
- Terbaca di semua latar: kotak/chip di atas insert/latar ramai; bayangan lembut di atas pembicara.
- Huruf kecil gaya ucapan; kata yang dipakai ulang boleh diparafrase singkat, angka ditulis angka ("0,1%", "73%").
- Warna = makna tetap dalam satu video: aksen = konsep inti; merah = kaget/tabu/emosi negatif; kapital = angka/klaim tegas.

**Dipilih per video:** hierarki ukuran (2–3 tingkat v1/v2 vs satu baris v3); reveal (blur+opacity per kata 4–6 f v1/v2; hard swap per frasa
v3; ketik per huruf untuk serif/angka v1, untuk ejaan v3); bentuk kotak (persegi pekat v1, chip bulat transparan v2); warna aksen; bentuk
ekspresif sesekali (miring, marquee, teks menempel kepala — v3 saja).

**Pola "mode caption ikut tata letak"** (inti D9):
| Tata letak | Mode caption | Bukti |
|---|---|---|
| Pembicara saja (tanpa visual lain) | **besar/ekspresif**: kata kunci besar, hierarki — caption menjadi visualnya (solo); atau polos bila cut/reaksi sudah ramai (dua orang) | v1 `ref/frames/v1_t065_bigsub.jpg`; v2 `ref/v2/full/f01230.jpg`; v3 `ref/v3/full/f630.jpg` (polos) |
| Pembicara + overlay (headline, kartu) | **kecil** dalam kotak/chip di bawah overlay | v1 `ref/strips/v1_00_open.jpg`; v2 `ref/v2/full/f00060.jpg` |
| Insert layar penuh / dokumen | **kecil** dalam kotak/chip, y tetap; abu di atas halaman terang | v1 `ref/sheets/v1_sheet_0.jpg` 9–36 s; v2 `ref/v2/fullgrid_types.jpg` (Kompas, sponsor) |
| Pembicara saja tapi kalimat sambungan tanpa kata kunci | kecil (v2 "let's be honest" 50,4) | `ref/v2/full/f01530.jpg` |
| Judul/konsep tampil | caption **hilang**; judul menempati ruang kosong: headroom bila kosong (v3 `ref/v3/full/f1500.jpg`), zona caption bila headroom dipakai panel (v3 `ref/v3/strips/s07_newyork_title.jpg`) | |

### 4d. KAPAN MEMOTONG (ganti gambar)

**Pemicu perubahan gambar yang terlihat di benchmark**
| Pemicu dalam ucapan | Perubahan | Bukti |
|---|---|---|
| Nama benda/brand/tempat disebut | cut ke aset asli tepat di kata itu (logo, footage, foto) | v2 "DBL" 8,6 logo, "Indonesia Arena" 27,1; v3 "AXE" 6,6, "Coca" 43,0 |
| Angka/fakta | cut ke dokumen/grafik resmi; highlight/zoom pindah di angka berikutnya | v2 "750 ribu" 13,1, "47 jam" 19,2, "15.729" 24,5; v3 "73" 28,0 |
| Item daftar ("kedua", "nah yang ke-3") | penanda/item baru di kanvas yang sama, atau kembali sebentar ke wajah dengan teks besar sebagai "tanda bab" | v1 13,6/15,6/19,2/24,7/26,3 (`ref/v1/v1_21_ui3_ui4.jpg`); v3 judul aspek 39,9 / 48,9 / 60,8 |
| Tonal turn ("tapi gilanya", "gw boong") | hard cut ke B&W / merah / color bar, ±0,5–1,2 s | v2 11,2; v3 16,7 |
| Kalimat opini/pertanyaan setelah blok bukti | cut kembali ke wajah (sering via flash/blur→fokus) | v2 7,0, 20,2, 54,7; v1 4,8 |
| Penekanan di tengah kalimat tanpa benda | punch-in/ganti angle di kata tekanan (boleh di tengah kalimat — **gambar**, bukan **audio**) | v3 9,40, 12,47, 36,4, 80,27 (`ref/v3/hardcuts.txt`) |
| Lelucon/reaksi (dua orang) | cut ke pendengar | v3 cut tiap ±1,1 s |

**Berapa lama ditahan:** dokumen 2,5–5 s (selama kalimatnya dibaca); UI yang sedang "diisi" sampai 5,5 s asal ada gerak internal; footage rasa
1,3–2,4 s; montase foto pembuka 0,33 s per foto (energi); logo/perbandingan ±1–1,3 s; wajah 0,5–4,1 s (benchmark), maksimal ±7 s di
dua orang dengan cut. **Tidak ada gambar diam >5 s** — gambar yang lebih lama wajib bergerak di dalam (highlight, pan, zoom, penanda).

**Rantai:** saat beberapa fakta berurutan tidak butuh opini di antaranya, visual dirantai tanpa kembali ke wajah (v2 11,8–20,2:
billboard → seat plan → artikel, 8,4 s, ganti tiap 1,3–4,9 s). Kembali ke wajah saat kalimat berganti fungsi (fakta → opini).

**Sengaja menahan (tanpa grafik):** pertanyaan/opini ke kamera, pengakuan ("let's be honest"), tanya-jawab dua orang (v3 50,9–57,9 = 7 s
hanya cut antar orang), kalimat penutup emosional. Gantinya: punch-in, angle lain, teks besar — bukan gambar tambahan.

**Audio:** semua cut ucapan di benchmark jatuh di awal kata/antar frasa (notes_v2 E "mayoritas hard cut tepat di awal kata"). Cut gambar
(punch-in, insert) boleh di tengah kalimat; **cut audio tidak pernah**.

### 4e. POSISI dan kerapian
- **Cari ruang kosong dulu, pindahkan orang hanya bila perlu.** v3 panel mengisi dinding di atas kepala tanpa menggeser pembicara
  (`ref/v3/full/f630.jpg`); kit kita `split` justru mendorong pembicara turun 300 px. v2 menggeser pembicara ke kanan hanya untuk memberi
  tempat logo di kiri (33,6 s, `ref/v2/strip15_arena_logo_f975.jpg`).
- **Zona tetap per video:** overlay di dada/bawah dagu (y ±60–75%) ATAU di headroom (y ±0–38%); caption di zona yang sama di semua shot
  sejenis; tidak ada apa pun yang penting di bawah ±80% atau di kolom kanan bawah (tombol platform).
- **Margin konsisten:** blok teks dokumen 75–91% lebar (margin 4–12%), rata tengah; kartu headline lebar sama di v1/v2 (±80–88%).
- **Satu fokus:** paling banyak satu blok baca + caption; elemen kedua (logo, stiker) hanya bila ia hiasan kecil di tepi (v1 starburst
  hanya di hook).
- **Rapi walau padat:** satu panggung latar untuk insert penjelasan (v1), satu gaya highlight per latar (v2), satu sistem caption,
  durasi seragam per jenis visual, semua elemen datar (tanpa bayangan/rotasi). Padat datang dari **frekuensi perubahan**, bukan dari
  banyaknya elemen sekaligus.

### 4f. Layar penuh vs panel vs overlay vs pembicara saja

| Pilihan | Alasan di benchmark | Bukti |
|---|---|---|
| **Layar penuh** | Penonton harus **membaca** (dokumen, UI, harga) atau **merasakan skala** (tribun penuh, arena) dan wajah tidak menambah apa-apa saat itu; pembicara solo | v1 UI, diagram; v2 dokumen/footage 67% |
| **Panel di ruang kosong (atas)** | Wajah/reaksi tetap penting (dua orang) dan footage punya headroom; aset bisa dikenali sekilas (billboard, Apple–Samsung) | v3 17% (`ref/v3/full/f630.jpg`) |
| **Overlay kecil di atas wajah** | Hook/klaim yang harus disertai kontak mata; logo brand yang disebut; rekap kecil (v1 kartu prompt 29,8) | v1 0–4,8, 29,8–31,6; v2 0–3,6 |
| **Pembicara saja** (+ teks besar/punch-in) | Opini, pertanyaan, emosi, sambungan, punchline; reaksi lawan bicara | v1 37%, v2 24%, v3 73% |
Aturan bantu: kalau jawabannya "harus dibaca" → layar penuh; "harus dikenali" → panel/overlay; "harus dirasakan dari wajah" → pembicara
saja + perangkat kamera/teks.

### 4g. Aset nyata vs gambar buatan
| Video | Nyata | Buatan |
|---|---|---|
| v1 | headline + logo media, UI ChatGPT, logo Sheets/Drive/Meta/Gemini, b-roll CGI stok | ikon AI stok + diagram timeline dan 10→100 (±4 s ≈ 7%), 2 starburst |
| v2 | semua dokumen, foto, footage, poster, grafik sponsor resmi, logo | hanya counter angka (±1,5 s ≈ 2%) |
| v3 | footage billboard, meme Apple–Samsung, iklan Coke–Pepsi, artikel, video kapur, stiker asap | 0 (hanya tipografi) |
Grafik buatan dijaga minimal dengan: monokrom (hitam di putih), piktogram generik, satu gagasan per layar, digerakkan oleh kamera
(pan/motion blur) bukan hiasan, teks serif yang sama dengan sistem caption. **Tidak pernah UI palsu, kartu formulir buatan, mockup
perangkat.** Parcelin lebih banyak gambar buatan (box3d, kurva, formulir, cap) — itu batas atas yang masih diterima, bukan arah utama.
Rincian per visual ada di 4j.

### 4h. TIMING — kapan visual muncul dan berapa lama (ACCEPTANCE 9)

Cara ukur: onset visual (dari strip/tabel catatan) dikurangi awal kata di `ref/v{N}_words.json` (Whisper, ketelitian ±2 f). Positif =
setelah kata mulai. 30 fps.

**Onset terhadap kata**
| Jenis visual | Onset yang teramati | Contoh (visual · kata · selisih) |
|---|---|---|
| Hard cut ke aset (foto, footage, dokumen, panel) | **0 sampai +5 f** setelah kata yang menamai benda | v2 billboard · "tiket" 11,76 · 0 f; v2 Student Athlete · "Student" 36,28 · 0 f; v2 Harian · "Honda" 62,98 · 0 f; v2 arena · "Indonesia" 27,10 · 0 f; v3 Coke · "Coca" 42,84 · +5 f; v3 close-up tulisan · "smells" 22,36 · +3 f |
| Aset yang menjadi **subjek seluruh klausa** | di awal klausa, **−7 sampai −20 f** sebelum kata benda | v2 seat plan di "itu bisa sampe" 13,1 · "750" 13,66 · −17 f; v2 headline suporter di "belum lagi" 45,0 · "supporter" 45,68 · −20 f; v2 artikel presale di "Yang" 15,3 · "pre" 15,52 · −7 f; v3 Samsung di antara "Apple" (41,32) dan "Samsung" (42,26) |
| Overlay yang masuk dengan fade (logo, ikon, crop artikel, tekstur) | fade **mulai −12…−2 f**, penuh di kata (±3 f) | v1 Sheets mulai 33,10 · "Sheets" 33,50 · −12 f (`ref/strips/v1_29_card_icons.jpg`); v1 Drive 33,90 · 33,96 · −2 f; Meta 34,30 · 34,40 · −3 f; accounting 35,10 · 35,10 · 0 f; v3 kapur 26,67 · "bukti" 26,86 · −6 f; v3 artikel fade 28,07–28,30 · "73" 28,00 · +2 f (penuh +9 f) |
| Judul/kata besar per kata | **−1 sampai +3 f** (hard on) | v3 "New" f615 · 20,50 · 0 f; "TIME" 21,13 · "Times" 21,08 · +2 f; "SQUARE" 21,30 · 21,32 · −1 f; "Psikologi" 39,87 · 39,90 · −1 f; "Upward" 48,93 · 48,82 · +3 f; "Social" 60,83 · 60,78 · +1 f (`ref/v3/strips/s07_newyork_title.jpg`) |
| Caption kinetik per kata (blur-in) | mulai di kata, tajam **+4…+6 f** | v1 "kasih tau" 12,33→12,47; "menyeramkan" mulai 56,47, tajam 56,63 (`ref/strips/v1_54_ending.jpg`) |
| Perubahan di dalam visual (highlight, penanda, zoom, pan) | **0 f** di kata yang dipindahi; gerak kamera boleh tiba **sebelum** angka diucapkan | v1 penanda "2" · "Kedua" 15,64 · 0 f, pan +11 f; v1 pan timeline ke 12:00 · "jam" 42,08 · 0 f; v2 zoom f531→f551 (17,70–18,37) mulai di "tiket normalnya" 17,78, tiba ±0,8 s sebelum "47" 19,16 (`ref/v2/strip06_article_dblid_f455.jpg`); v2 lompatan zoom f740 · "15" 24,50 · +5 f |
| Penanda nada (B&W) | di kata pembalik, **−1…0 f** | v2 B&W 20,8 · "Liga" 20,84; v2 "tapi gilanya" 11,2 di awal "tapi" |
| Counter angka | hitung 15 f, **selesai sebelum** angka/ satuannya diucapkan | v2 f166→f181 (5,53–6,03) di "tahan sampe 20 tahun" (`ref/v2/strip13_counter_f160.jpg`) |
| Kartu headline hook | frame 0 (sudah ada) | v1, v2 |

**Durasi tahan (min / tipikal / maks) dan apa yang mengakhirinya**
| Jenis | Min | Tipikal | Maks | Berakhir saat | Alasan panjangnya |
|---|---|---|---|---|---|
| Strip headline (hook) | 3,6 | 4–5 | 4,8 s | kalimat klaim selesai (+2 f), keluar flash/cut | membaca judul ±9–12 kata sambil melihat wajah |
| Dokumen layar penuh | 1,6 | 3,3 | 4,9 s (v3 crop 3,9) | kalimat bukti selesai, atau klaim berikutnya punya visual sendiri | membaca baris yang disorot (bukan seluruh halaman) |
| UI asli yang diisi | 2,9 | 3–4,5 | 5,5 s | "nah yang ke-N" → kembali ke wajah | membaca satu bagian; >5 s hanya dengan pan/penanda di dalamnya |
| Foto/footage layar penuh | 0,33 (montase) | 1,3–2,4 | 3,8 s (2 klip) | benda/kalimat berikutnya | dikenali/dirasakan, tidak dibaca |
| Panel atas (dua orang) | 1,27 | 1,3–2,0 | 3,9 s | kata bendanya selesai, cut ke reaksi | dikenali sekilas; wajah tetap utama |
| Logo | 0,9 | 1–1,4 | 2,8 s (menemani headline) | kalimat berikutnya | bentuk yang dikenal: <0,5 s untuk mengenali |
| Angka/counter | 1,5 | ±2 | 2,1 s | satuan/kalimat selesai | angka + satuan dibaca dalam 1 pandang |
| Judul konsep / teks besar | 0,77 | 1,0–1,6 | 2,0 s | frasa berikutnya | 1–3 kata dibaca <0,6 s; tetap selama istilah diucapkan |
| Penanda nada (B&W, color bar) | 0,37 | 0,5–1,2 | 2,6 s (montase penutup) | punchline mendarat, cut berikutnya | beat rasa, bukan informasi; panjang = waktu lelucon |
| Grafik buatan (diagram) | 1,9 | ±2,2 | 4,5 s (hub logo) | gagasan selesai diucapkan | satu gagasan, digambar sambil diucapkan |

**Cara menurunkan durasi untuk kasus baru (resep)**
1. **Mulai:** jangkar ke kata pertama yang menamai benda. Hard cut → 0…+3 f; fade/blur-in → mulai −6…−10 f supaya penuh dan tajam saat kata
   terdengar. Bila benda itu subjek seluruh klausa ("itu bisa sampe 750 ribu"), mulai di awal klausa.
2. **Selesai:** di akhir kata terakhir yang digambarkan visual (+0…6 f) atau tepat di jangkar visual berikutnya (rantai). Hilang saat
   topik selesai — jangan menyeberang ke kalimat yang tidak berhubungan.
3. **Cek minimum:** `durasi ≥ max(panjang frasa yang diucapkan, waktu baca)`, dengan waktu baca ≈ **0,5 s + N/3,5 s** untuk N kata yang
   **harus dibaca** (hanya yang disorot, bukan seluruh halaman). Contoh: highlight 7 kata → ≥2,5 s; headline 10 kata → ≥3,4 s.
   Dicek ke benchmark: v2 #2 dua baris ±14 kata → 4,5 s (nyata 4,9 s); v2 #7 yang disorot "Suporter Juga Bisa Ikut Berkompetisi" 5 kata
   → 1,9 s (nyata 1,6 s, ditopang ucapan yang sama); v1 headline ±9 kata → 3,1 s (nyata 4,8 s). Hanya dikenali (logo, merek terkenal,
   tempat) → ≥0,8–1,0 s; footage rasa → 1,3–2,5 s per klip; beat (B&W/flash) → 0,4–1,2 s.
4. **Cek maksimum:** >5 s → wajib gerak internal (highlight ke baris berikutnya, zoom, item baru) atau dipecah; tidak ada satu gambar
   diam >5 s di benchmark.

**Sengaja sangat pendek (≤1,5 s) dan kenapa tetap berhasil:** montase foto pemain 0,33 s (pesannya "ini orang-orang nyata, banyak",
bukan wajah tertentu); logo DBL 1,1 s, arena 0,9 s (bentuk/ tempat dikenal sekejap); Apple–Samsung 1,33 s, Coke–Pepsi 1,27 s (pasangan yang
sudah ada di kepala penonton); B&W 0,5 s, color bar 0,37 s (beat, bukan informasi); judul konsep 1,0 s (2 kata). Berhasil karena
(a) **dikenali, bukan dibaca**, (b) ucapan mengatakan hal yang sama pada saat yang sama, (c) gambar familiar. Jangan pendekkan sesuatu
yang harus **dibaca** di bawah resep langkah 3.

### 4i. GERAK — apa yang membuat animasi halus dan pas (ACCEPTANCE 8)

| Gerak | Panjang | Dipakai di | Artinya |
|---|---|---|---|
| Hard cut | 0 f | v3 semua panel kecuali Samsung, v2 sebagian besar footage + Student Athlete, punch-in v3 | energi, "ini dia", timing lelucon; paling sering |
| Blur-in (defocus→tajam, sering + skala turun sedikit) | dokumen 6–16 f (v2 f459→f475 16 f, f686→f700 14 f, f1276→f1285 9 f, f1688→f1694 6 f, f1890→f1898 8 f); headline v1 12 f; kembali ke wajah 6–8 f | dokumen, kembali ke pembicara (v1, v2) | "lapisan baru, fokus ke sini"; lembut, editorial |
| Fade (+ naik/skala kecil) | 5–12 f (v3 artikel 7–8 f, mosaik 5 f, kapur 10 f, Samsung fade+skala 8 f; v1 logo fade+naik 12 f, ikon AI 12 f) | overlay di atas pembicara tanpa ganti adegan | "ditambahkan", bukan "pindah" |
| Flash/bloom putih | 2–8 f (v1 4,80–4,87; v2 f603→f611, f810→f814) | keluar dari blok bukti ke opini, tutup hook | **ganti bagian** |
| Light-leak sapuan | 8–10 f | v1 29,5 dan 54,0 | tutup satu blok (daftar prompt, diagram) |
| Fade ke hitam | 20 f, sekali | v2 40,3 (Student Athlete → "uniknya") | jeda bab yang lebih berat |
| Dissolve | pendek (tak terukur) | v1 antar klip CGI 47–50 | rangkaian suasana |
| Type-on per huruf | sesuai tempo bicara (v1 "mereka apa" 12 f; "0,1%" 18 f; v3 "BDSM PA" 30 f) | baris serif, angka, ejaan | "sedang diucapkan/dieja sekarang" |
| Sapuan highlight | 10–16 f per baris, kecepatan = ucapan, boleh berhenti di tengah kata (v2); statis (v3) | dokumen | **"baca ini sekarang"** |
| Gerak kamera ke area | ease 20–24 f (v1 pan 16,0–16,8; v2 zoom f531→f551); lompatan keras 0 f (v2 "15"); whip pan dengan motion blur ±6 f (v1 timeline) | dokumen, UI, diagram | ease = "ikuti saya ke baris berikut"; lompatan = tekanan pada angka |
| Drift/push pelan | sepanjang tampil | poster, dokumen (v2) | gambar tetap hidup tanpa menarik perhatian |
| Count-up | 1 angka/frame, 15 f | v2 counter | angka "terjadi" |
| Keluar | hampir selalu **tanpa animasi keluar** — diganti cut berikutnya (caption juga hard replace) | semua | tidak ada sisa yang berlama-lama |

**Konstan dalam satu video:** satu kosakata gerak kecil (v1: blur-in + flash + light-leak; v2: blur-in + flash + cut; v3: hard cut + fade);
jenis elemen yang sama selalu masuk dengan cara yang sama; arti tiap transisi tetap (flash = ganti bagian).
**Dihindari di ketiga video:** pegas/overshoot "pop", slide/push dokumen dari samping (Parcelin dan kit kita memakainya; benchmark tidak),
rotasi, berdenyut terus, beberapa gerak bersamaan pada elemen berbeda, animasi keluar yang lambat.

**Cek "halus" di strip frame berurutan** (setiap transisi, setiap frame atau tiap 2 frame):
1. Posisi/skala berubah monoton, tanpa lompatan antar frame (kecuali hard cut/lompatan zoom yang disengaja).
2. Ease: selisih per frame kecil di awal dan akhir gerak, besar di tengah.
3. Elemen **sudah terbaca penuh (opacity 1, blur 0) paling lambat saat katanya mulai**, atau ≤2 f sesudahnya untuk hard cut.
4. Tidak ada frame sisa: tidak ada 1–2 frame visual lama/kosong/hitam di titik cut, tidak ada bayangan transparan setelah keluar.
5. Blur benar-benar kembali ke 0; teks tidak bergetar saat diam.
6. Dua elemen tidak tumpang tindih tak terbaca di tengah transisi; caption tidak meloncat posisi antar potongan dalam tata letak yang sama.
Bukti contoh yang lulus: `ref/v2/strip06_article_dblid_f455.jpg` (blur-in 16 f, zoom ease 20 f, highlight berurutan, keluar bloom 4 f).

### 4j. ASET NYATA — klasifikasi tiap visual (ACCEPTANCE 7)

Nyata = aset dunia nyata yang tidak digambar editor (termasuk stok/CGI dan meme yang sudah ada); **+tambahan** = aset nyata + highlight,
penanda, redaman, efek; **buatan** = digambar editor. Teks/caption dan grade pembicara tidak dihitung.

| Video | Nyata | Nyata + tambahan | Buatan | Catatan |
|---|---|---|---|---|
| v1 | 6: logo ChatGPT/Gemini; UI ChatGPT prompt pendek; kartu composer rekap; logo Sheets/Drive/Meta; b-roll CGI server; 3 klip CGI robot/neural/humanoid (1 set) | 2: headline Bloomberg Technoz (+baris poin video, starburst); UI ChatGPT prompt panjang (+penanda 1–4, redaman, zoom) | 3: starburst dekoratif; diagram timeline (dengan 1 logo Google Ads asli); diagram 10→100. Campuran: hub ikon AI (ikon stok + logo asli) | buatan ±7% waktu |
| v2 | 16: 3 foto pemain, logo DBL di lapangan, footage DBL PLAY, 2 foto arena, 6 klip penonton, grafik sponsor resmi, 2 poster; + 4 logo-di-belakang-kepala (logo asli) | 12: kartu headline hook, billboard B&W + poster berwarna, seat plan (+stabilo, redaman), 9 dokumen (+highlight/redaman; sebagian mungkin diketik ulang) | 1: counter angka di atas footage dunk asli | buatan ±2% |
| v3 | 6: footage billboard (3 pemakaian), close-up tulisan billboard, ilustrasi Apple–Samsung (sudah ada di internet), iklan Coke–Pepsi; + overlay temuan: video kapur, stiker asap, color bar (×2) | 2: billboard dipixelate (teaser), paragraf artikel + stabilo | 0 (hanya tipografi) | buatan 0% |

**Cara editor mendapat "nyata" untuk kasus sulit**
| Yang diucapkan | Tidak ada foto persisnya → yang ditunjukkan |
|---|---|
| "AI bukan menggantikan, tapi mengkalikan" (v1) | CGI robot/neural sebagai metafora suasana, lalu diagram monokrom 10→100 untuk angkanya |
| "dibikin timernya, cron/heartbeat" (v1) | CGI ruang server (suasana) + teks besar; "jam 9 / jam 12" → timeline minimal |
| Struktur prompt (v1) | alat aslinya (ChatGPT) diisi teks prompt dari ucapan — demonstrasi alat nyata, bukan bukti palsu |
| "komunitas sekolah", "akses ke anak muda" (v2) | footage penonton/suporter asli dari acaranya |
| "20 tahun lebih" (v2) | counter di atas footage asli, dengan fakta tepat "2004-now / 22 tahun" |
| "tiket mereka di 2026" (v2) | foto billboard asli, gedung B&W supaya posternya jadi fokus |
| "terinspirasi dari Amerika" (v2) | kutipan dokumen di atas foto orang yang dikutip |
| Teaser "brand ini marketingnya gila" (v3) | billboard asli yang dipixelate, dibuka di nama merek — bukan kotak misteri buatan |
| "bukti data-datanya" (v3) | paragraf sumber asli + video kapur stok sebagai tekstur |
| "kayak Apple sama Samsung / Coca-Cola sama Pepsi" (v3) | gambar perbandingan yang sudah beredar + iklan asli terkenal |
| "semprot… cewek mendekat" (iklan lama, v3) | stiker asap mengikuti gerakan tangan pembicara — tidak membuat iklan palsu |
| Konsep psikologi (v3) | judul tipografi, bukan ilustrasi |
Pola: (1) cari benda/peristiwa aslinya; (2) bila tidak ada, cari **dokumen** tentang benda itu; (3) bila tidak ada, **metafora nyata**
(stok/footage suasana) atau gambar yang sudah dikenal publik; (4) baru tipografi; (5) diagram buatan hanya untuk angka/hubungan,
monokrom, satu gagasan. Resolusi rendah tetap dipakai bila asli (v2 foto pemain). Setiap visual buatan butuh alasan tertulis (ACC 7).

### 4k. Tidak terlalu jarang, tidak terlalu ramai (ACCEPTANCE 10–11, ringkas)
- **Batas atas dari benchmark:** tidak pernah >1 blok baca + caption sekaligus; tidak ada perubahan bermakna lebih cepat dari ±1 per 2 s
  secara berkelanjutan (kecuali montase ≤1 s sebagai satu beat); pembicara diberi ruang untuk kalimat penting (v2 penutup 4,1 s; v3 tanya-jawab 7 s).
- **Tes "kalau dibuang, apa yang hilang?"**: tiap elemen benchmark menjawab satu kata yang diucapkan; hiasan murni hanya di hook (v1 starburst).
- **Mencari peluang** (ACC 10): kutipan orang lain → bubble chat kiri/kanan di atas pembicara (Parcelin P2; owner menganjurkan); benda
  disebut → bendanya; angka → sumber atau tipografi; belokan → ganti "dunia" gambar; daftar → kanvas bertambah; perbandingan → dua gambar
  yang dikenal. Batas: bubble = ilustrasi ucapan (boleh); layar aplikasi/profil/artikel palsu sebagai bukti = tidak.

---

## 5. Contoh penalaran (untuk ditempel ke guide)

**K1 — Klaim berita di hook** (v1 0–4,8; v2 0–3,6)
Situasi: kalimat pertama = statistik mengejutkan. → Penonton butuh: percaya klaimnya **dan** kenal siapa yang bicara. → Opsi: artikel layar
penuh / judul buatan / headline asli sebagai lower-third. → Dipilih: headline asli + logo media di bawah dagu, sejak frame 0, caption kecil di
bawahnya. → Kenapa: wajah = hook, kartu = bukti; dua-duanya terbaca dalam satu pandangan. → Pelajaran: di hook, bukti menumpang di wajah;
layar penuh baru setelah penonton "kenal" pembicara. (`ref/frames/v1_t005_headline.jpg`, `ref/v2/full/f00060.jpg`)
*Timing/gerak/aset:* frame 0 → akhir kalimat klaim +2 f (4,8 s / 3,6 s); masuk blur→tajam 12 f, keluar flash 2 f; judul + logo media asli.

**K2 — Fakta beruntun di tengah video** (v2 15,3–20,2 "pre-sale abis 1 jam… normal 47 jam")
→ Butuh: membaca dua angka dan percaya sumbernya. → Opsi: teks besar di wajah / artikel layar penuh. → Dipilih: artikel dbl.id layar penuh,
latar gelap, highlight kotak terbalik pada baris 1, lalu kamera zoom ke "47 jam" saat diucapkan. → Kenapa: dua angka = dua fokus berurutan;
kamera memindahkan mata. → Pelajaran: satu dokumen bisa memuat beberapa klaim asal fokusnya berpindah mengikuti mulut.
(`ref/v2/full/f00520.jpg`, `ref/v2/strip06_article_dblid_f455.jpg`)
*Timing/gerak/aset:* masuk −7 f di awal klausa "Yang pre-sale-nya", blur-in 16 f; zoom ease 20 f mulai di "tiket normalnya" dan tiba ±0,8 s sebelum "47"; tahan 4,9 s (≈ waktu baca 2 baris); keluar bloom 4 f ke wajah; halaman asli + highlight.

**K3 — Angka: dua keputusan berbeda** (v2 13,1 "750 ribu" vs v1 44,6 "0,1%")
"750 ribu" punya sumber resmi → seat plan asli, zoom ke baris "1A IDR 750,000", stabilo, harga lain dipudarkan (`ref/v2/full/f00430.jpg`).
"0,1%" adalah kesimpulan pembicara tanpa sumber → angka raksasa diketik per karakter di atas wajah (`ref/sheets/v1_sheet_1.jpg` 45–46 s).
→ Pelajaran: angka **bersumber** = tunjukkan sumbernya; angka **opini/punchline** = tipografi di wajah. Jangan membuat grafik untuk angka
yang tidak ada datanya.
*Timing/gerak/aset:* seat plan masuk di awal klausa (−17 f sebelum "750"), tahan 2,3 s; "0,1%" diketik per karakter 18 f mengikuti ucapan, tahan ±2 s. Grafik resmi asli vs tipografi.

**K4 — Aksi aplikasi/layar** (v1 13,6–29,6 "lu adalah expert… kedua… ketiga… keempat")
→ Butuh: melihat isi prompt bagian demi bagian. → Opsi: screenshot di kartu / screen recording penuh / satu kanvas UI yang di-zoom.
→ Dipilih: UI ChatGPT asli tanpa bingkai di panggung vinyet, bagian aktif tajam + penanda merah bernomor, sisanya pudar; kembali ke wajah
dengan teks besar di setiap "nah yang ke-N". → Kenapa: ritme wajah–UI menjaga 16 s daftar tetap hidup; penanda memberi rasa kemajuan.
→ Pelajaran: zoom ke kalimatnya, bukan ke halamannya; kanvas yang sama kembali dengan status bertambah. (`ref/frames/v1_t165_chatui.jpg`,
`ref/v1/v1_21_ui3_ui4.jpg`)
*Timing/gerak/aset:* penanda di kata nomor (0 f), pan ease 24 f; tiap tampil 2,9–5,5 s, wajah di antaranya 0,9–1,6 s; masuk blur→tajam 6–8 f; UI asli.

**K5 — Daftar nama** (v1 31,6–35,9 "Google Sheets, Google Drive, Meta Ads, accounting software")
→ Dipilih: ikon AI di tengah, tiap logo asli muncul tepat di namanya dan mengelilingi pusat. → Kenapa: gagasan "AI diberi akses ke semua ini"
menjadi satu gambar. → Pelajaran: daftar = elemen bertambah di satu kanvas, satu per kata. (`ref/strips/v1_29_card_icons.jpg`)
*Timing/gerak/aset:* tiap logo fade+skala mulai −12…0 f sebelum namanya, penuh di kata; kanvas 4,5 s; logo asli, ikon pusat stok.
Varian dua orang: aspek 1/2/3 sebagai judul serif per kata di headroom (v3 `ref/v3/full/f1500.jpg`).

**K6 — Tonal turn** (v2 11,2 "Tapi gilanya,"; v3 16,7 "…gw boong")
→ Butuh: merasakan belokan sebelum faktanya. → Dipilih: hard cut ke B&W pembicara 0,5–1,2 s, lalu langsung bukti (v2 billboard di
"tiket") atau color bar + beep (v3 komedi). → Pelajaran: penanda nada murah, singkat, di kata pembaliknya; 1–3× per video.
*Timing/gerak/aset:* hard cut 0 f di "tapi"/kata pembalik, tahan 0,5–1,2 s (= waktu lelucon), langsung cut ke visual berikutnya; tanpa aset.
(`ref/v2/strip14_bw_billboard_f330.jpg`, `ref/v3/strips/s06_bw_bars_17s.jpg`)

**K7 — Tanpa grafik** (v3 50,9–57,9 tanya-jawab "apa upward comparison?"; v2 50,4 "let's be honest, ini bukan strategi baru")
→ Butuh: dinamika percakapan/pengakuan. → Opsi: menambah ilustrasi / menahan di wajah. → Dipilih: wajah saja; v3 cut antar orang dan
angle, v2 shot lebih dekat + caption kecil. → Kenapa: tidak ada benda yang jujur untuk ditunjukkan; grafik akan mengganggu momen.
→ Pelajaran: "tanpa grafik" tetap butuh perubahan gambar (cut/punch-in) dan alasan tertulis; maksimal ±7 s. (`ref/v2/full/f01530.jpg`)
*Timing/gerak:* v3 cut antar orang tiap ±1 s (hard cut), v2 1,8 s lalu dokumen berikutnya.

**K8 — Benda yang tidak bisa difoto persis (aset nyata untuk kasus sulit)** (v3 3,5–6,6 teaser; v2 5,5 "20 tahun lebih")
→ Butuh: rasa penasaran / angka yang "terjadi". → Opsi: kotak misteri atau grafik buatan. → Dipilih: billboard asli dipixelate lalu dibuka
tepat di "AXE" (−5 f); counter 9→22 di atas footage dunk asli, selesai sebelum "tahun". → Pelajaran: ubah aset nyata (pixelate, gelapkan,
tumpuk angka) sebelum menggambar sesuatu yang baru. (`ref/v3/strips/s03_mosaic_to_clear.jpg`, `ref/v2/strip13_counter_f160.jpg`)

---

## 6. Benchmark minimum (untuk reviewer: contact sheet + build report edit kita)

T1–T15 urut menurut pentingnya; T16–T20 ditambahkan untuk ACCEPTANCE 7–11 (T16/T17 setara pentingnya dengan T3/T4). **M** = bisa dicek mesin (build report), **J** = penilaian di still. Angka ACCEPTANCE di kolom terakhir.

| # | Tes (pertanyaan) | Lulus bila | Jenis | ACC |
|---|---|---|---|---|
| T1 | Berapa rentang terpanjang tanpa **perubahan gambar** (cut kamera, punch-in, visual masuk/keluar, ganti grade; ganti caption tidak dihitung)? | ≤4 s; 4–7 s hanya dengan alasan tertulis; >7 s gagal | M | 6 |
| T2 | Berapa rentang terpanjang tanpa **elemen visual apa pun** selain caption (insert, panel, overlay, judul, teks besar)? | ≤7 s, dan setiap rentang >4 s punya alasan tertulis (opini/tanya-jawab/emosi) | M | 6, 1 |
| T3 | Tes tutup-caption: untuk tiap visual, apakah gambarnya saja menunjukkan hal yang sedang diucapkan? | 100% visual lulus; b-roll "suasana" hanya untuk konsep tanpa wujud, ≤1 per ±30 s | J | 5 |
| T4 | Apakah setiap visual mulai di kata yang ia gambarkan? | awal visual dalam −4…+2 frame dari jangkar kata | M | 5, 2 |
| T5 | Apakah setiap kalimat punya keputusan tertulis (visual apa / kenapa tanpa visual)? | 100% kalimat di `visual_plan`; setiap klaim, angka, nama punya visual atau alasan | J | 1 |
| T6 | Apakah wajah (mata–mulut) pernah tertutup overlay atau caption? | 0 still dengan wajah tertutup | J | 3 |
| T7 | Apakah caption dan elemen ada di zona aman, dengan margin dan perataan konsisten? | caption y ±54–80% sesuai framing, tidak ada elemen penting di bawah ±80% atau kolom kanan bawah; margin kiri-kanan ≥4% dan sama untuk elemen sejenis | M/J | 3 |
| T8 | Satu fokus per frame? | tiap still: paling banyak 1 blok baca + caption; dokumen = 1 kalimat disorot, sisanya diredam | J | 3 |
| T9 | Potongan berita: sumber asli terlihat, kalimat yang diucapkan disorot saat diucapkan, crop hanya baris perlu, tanpa bingkai perangkat/kartu, terbaca di HP? | semua 5 ya; teks yang harus dibaca ≥ ±28 px tinggi-x pada 1080 lebar | J | 5, 3 |
| T10 | Setiap pilihan layar penuh / panel / overlay / pembicara saja punya alasan dari tabel 4f? | 100% beat punya alasan "dibaca / dikenali / dirasakan dari wajah" | J | 4 |
| T11 | Apakah ada cut audio di tengah kalimat? | 0 (cek titik cut vs batas kata/kalimat di build report) | M | 2 |
| T12 | Apakah ada gambar diam >5 s tanpa gerak internal, atau visual yang lebih pendek dari waktu bacanya? | 0; dokumen yang harus dibaca ≥2,5 s | M | 2, 6 |
| T13 | Caption: sinkron, terbaca di semua latar, mode berganti sesuai tata letak, warna punya satu arti tetap? | sinkron ±2 frame; kontras cukup di setiap still; tidak dobel dengan judul | J | 3 |
| T14 | Penanda nada (B&W/dim/punch-in/merah) dipakai di kalimat pembalik, 1–3×? | ada di kalimat pembalik utama; tidak >3× (kecuali video komedi) | J | 2 |
| T15 | Hook: sesuatu yang menyebut topik/bukti ada di ≤0,5 s, perubahan kedua ≤3,5 s? | keduanya ya | M | 6 |
| T16 | Onset: hard cut 0…+5 f dari kata; fade/blur sudah penuh saat kata mulai; visual subjek-klausa boleh mulai di awal klausa (≤−20 f) | 100% visual dalam rentang; pengecualian tertulis | M | 9 |
| T17 | Durasi: tiap visual ≥ max(frasa yang diucapkan, 0,5 s + N/3,5 s untuk N kata yang harus dibaca), ≥0,8 s untuk yang dikenali, dan berakhir saat topiknya selesai | 100%; daftar durasi per visual ada di build report | M | 9 |
| T18 | Gerak halus di strip frame berurutan (6 cek di 4i) dan satu kosakata gerak per video dengan arti tetap | semua transisi lulus 6 cek; tidak ada pop/pegas/slide dokumen tanpa alasan | J (strip) | 8 |
| T19 | Aset nyata dulu: setiap visual buatan punya alasan tertulis "tidak ada aset nyata yang bisa menunjukkan ini"; sumber + lisensi tiap aset tercatat | 100% | J | 7 |
| T20 | Tidak terlalu ramai: tiap elemen lulus "kalau dibuang, apa yang hilang?"; ≤1 blok baca + caption per frame; kepadatan tidak jauh di atas ±1 perubahan / 2 s tanpa alasan | lulus; reviewer mempertanyakan bila jauh di luar rentang benchmark konten sejenis | J + M | 11 |

Tidak ada tes warna, font, atau bentuk. Angka kepadatan (s/beat, % layar penuh) dilaporkan untuk dibandingkan, **bukan** syarat lulus.

---

## 7. Kit gap — digabung dan diprioritaskan (primitif generik saja)

| Prio | Primitif | Yang dimungkinkan | Kasus benchmark | Ukuran |
|---|---|---|---|---|
| **1** | **`doc` — sajikan crop halaman asli** dengan tata letak `full` / `lower` (strip headline) / `region` (x,y,w di ruang kosong); `highlights` per baris berjangkar kata dengan sapuan selebar ucapan (gaya `marker`/`invert`/`select`); `defocus_others` (opacity+blur di luar highlight aktif); `camera` keyframe (ease/jump ke rect); `bg`: speaker / foto-klip ter-dim / kertas vinyet / blur-fill; masuk `blur`/`fade`/`cut`, keluar `cut`/`flash`/`black`; **tanpa bingkai, bayangan, label, rotasi** | semua potongan berita (4a), UI asli (v1 ChatGPT), seat plan, poster | v1 A1/A2, v2 #1–#10 + seat plan, v3 artikel; juga Parcelin P10 | besar (menggantikan `screenshot` yang berkartu) |
| **2** | **Mode caption menurut tata letak** di `Subs`: `big` (hierarki 2–3 tingkat, reveal blur+opacity per kata) di pembicara saja; `small` (kotak/chip, per frasa) otomatis saat insert/overlay aktif; `hidden` saat judul membawa kata yang sama; peran warna via markup (aksen / alert / caps); posisi per framing | 4c | v1, v2, v3 | sedang |
| **3** | **`grade` + `zoom` pada pembicara**: B&W/dim/blur per rentang (hard cut), punch-in/reframe di kata (scale, x, y), close-up blur untuk teks besar | tonal turn, beat tanpa grafik, ruang untuk logo | v1 close-up blur, v2 B&W ×2 + geser kanan, v3 B&W ×3 + ±10 punch-in; Parcelin P3 | kecil (parameter + filter Speaker) |
| **4** | **Transisi + panel tanpa dorong**: `enter`/`exit` = `cut`/`blur`/`fade`/`flash`/`black` di semua insert; `split` dengan `shift:0`, region bebas (headroom), tanpa bayangan/pegas | hard cut v3, flash v1/v2, blur-in dokumen, panel headroom | v1, v2, v3 | parameter |
| **5** | **Teks judul/kinetik**: `kicker` (kata muncul di jangkarnya, serif/sans, posisi bebas, sembunyikan caption) + `typeon` (per karakter, untuk angka/ejaan) | konsep abstrak, angka opini, daftar aspek | v1 "0,1%", serif diketik; v3 judul konsep, "BDSM PA" | kecil |
| 6 | **Logo/ikon di kata** (overlay kecil di ruang kosong, fade+naik, beberapa berurutan mengelilingi pusat) | nama brand/alat disebut | v1 logo di kepala dan di sekitar ikon AI | kecil |
| 7 | `photo` `fit:contain` + `bg: blur-fill`/kertas, tanpa zoom bila `static` | poster/grafik resmi, color bar | v2 poster/sponsor, v3 color bar | parameter |
| 8 | `layer` blend (screen/normal) untuk aset video/gambar asli di atas pembicara | tekstur kapur, stiker | v3 saja | kecil, prioritas rendah (ONLY ONE) |
| 9 | `counter` angka | "20 tahun → 22" | v2 saja | kecil, rendah |
| **(laporan)** | **Build report per visual**: jenis, kata jangkar, onset relatif kata (frame), durasi, waktu baca minimum (dari N kata highlight), rentang sepi, % tersembunyi, perubahan/detik; + **strip otomatis** frame-berurutan untuk tiap transisi (temp dir per job — bug `/tmp/_frame.jpg`) | memungkinkan T1, T2, T4, T12, T16–T18 dicek mesin | semua | kecil–sedang, **prioritas tinggi** (ACC 6, 8, 9) |
| 10 | `bubbles` kiri/kanan di atas pembicara (sudah ada) — sesuaikan gerak ke kosakata video (fade/blur, bukan selalu pop) | kutipan pihak lain (ACC 10) | Parcelin | parameter |

**Jangan dibangun:** gambar konten spesifik (box3d, formulir, kurva khusus), UI aplikasi palsu, mockup laptop/HP (bertentangan dengan
"tanpa bingkai perangkat"; daftar Parcelin no. 10 `dmchat` dan 12 `laptop` dicoret), kartu "SUMBER", marquee/teks miring sebagai fitur umum
(cukup `kicker` dengan rotasi opsional), selective colour (butuh mask manual per foto).

**Tidak praktis di sini:** **logo di belakang kepala** (v2 ×4) butuh matting pembicara per frame — di CPU 4 vCPU untuk video 1080p
berjam-jam dan rawan tepi rambut. Alternatif: logo di ruang kosong samping kepala (v1), atau geser pembicara (`zoom` x) lalu logo di sisi
kosong (v2 33,6 tanpa overlap), atau cut singkat ke logo layar penuh (v2 8,6). Audio/SFX referensi tidak bisa diverifikasi; jangan
membangun sound design berdasarkan tebakan selain beep 1 kHz (terukur di v3).

---

## 8. Hal terbuka dan kontradiksi

**Kontradiksi antar catatan, diselesaikan dengan gambar**
- **Posisi judul serif v3:** notes_v3 D menulis "y ±8–15%". Gambar menunjukkan "New York / TIME SQUARE" di **zona caption (±66%)** karena
  headroom sedang dipakai panel (`ref/v3/strips/s07_newyork_title.jpg`), sedangkan "Upward / COMPARISON" di headroom ±27–33% saat panel
  tidak ada (`ref/v3/full/f1500.jpg`). Kesimpulan: judul ditaruh di ruang yang kosong saat itu, bukan di posisi tetap.
- **Batas layar penuh 50% (Parcelin P12)** vs v2 67%: bukan kontradiksi data, tapi aturan lama terlalu sempit → diganti alasan per beat (4f).
- **"Penutup layar penuh nyata" (CLAUDE.md lama/Parcelin)** vs ketiga benchmark tanpa CTA/kartu: penutup = pilihan menurut tujuan video.
- **Baseline kepadatan "1 beat / 5 s" (STYLE_NOTES lama)** vs benchmark 2–3 s: angka lama hanya batas bawah; benchmark owner lebih padat.
- **Kategori "pembicara saja"** diukur berbeda (v1 menganggap teks kinetik besar sebagai overlay → "±0%"; v2/v3 menghitungnya sebagai
  pembicara). Tabel 3b memisahkannya; angka beat antar catatan tidak sebanding persis.

**Belum bisa ditentukan**
- Audio/SFX/musik di semua video (hanya beep 1 kHz v3 terukur). Apakah flash/light-leak disertai whoosh tidak diketahui.
- Apakah headline/dokumen gelap v1/v2 diketik ulang atau screenshot (tipografi seragam lintas media → kemungkinan diketik ulang).
- Apakah close-up v1 dan shot dekat v2 50,4 adalah kamera kedua atau punch-in digital.
- Cara matte logo-di-belakang-kepala v2 (rotoscope atau AI).
- Sumber/lisensi b-roll CGI v1, meme v3, video kapur, stiker asap.
- Kurva easing persis (hanya jarak frame: blur-in 4–16 f, pan 24 f, light-leak 8–10 f).
- Onset di 4h dihitung dari kata Whisper (±2 f) dan label strip (±1 f); angka onset adalah rentang, bukan ukuran presisi.
- notes_v2 menulis zoom ke "47 jam" di f535→f555 dan juga "zoom ke 47 jam (19.2)"; strip menunjukkan zoom f531→f551 (17,7–18,4 s) dimulai
  di "tiket normalnya" dan selesai sebelum "47" (19,16) diucapkan — dipakai versi strip.
- Apakah owner menerima kadar gambar buatan Parcelin (formulir, box3d) di video gaya benchmark — tanyakan bila relevan.

**Bug `sheet.py` dan notes_v1:** saya membuka `ref/sheets/v1_sheet_0.jpg`, `v1_sheet_1.jpg` dan 7 strip v1 di `ref/strips/`
(`v1_00_open`, `v1_03_logos`, `v1_08_chat_ui`, `v1_29_card_icons`, `v1_38_timer`, `v1_51_diagram`, `v1_54_ending`): **semua frame milik v1**
(pria berkacamata, kaos hitam, ruang gelap, atau insert v1). Cap waktu file menunjukkan sheet/strip di `ref/sheets` dan `ref/strips` dibuat
berurutan oleh satu proses (03:18–03:22, v1 → v2 → v3), bukan bersamaan; gambar `ref/v1/*` dibuat 03:26 oleh worker v1. **Tidak ada klaim
notes_v1 yang bergantung pada frame tercemar.** (Catatan: v1 dan v2 tampaknya pembicara yang sama di ruangan berbeda — itu bukan kontaminasi.)

Gambar yang saya buka sendiri untuk sintesis ini: `ref/sheets/v1_sheet_0.jpg`, `v1_sheet_1.jpg`; 7 strip v1 di atas;
`ref/v2/fullgrid_types.jpg`; `ref/v2/full/f00060.jpg`, `f01150.jpg`, `f01950.jpg`, `f00430.jpg`; `ref/v3/full/f870.jpg`, `f630.jpg`,
`f230.jpg`, `f1500.jpg`; `ref/v3/strips/s07_newyork_title.jpg`; `ref/v2/strip06_article_dblid_f455.jpg` (timing/gerak).
