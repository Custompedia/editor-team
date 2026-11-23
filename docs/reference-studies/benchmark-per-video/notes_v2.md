# notes_v2 — Benchmark v2 (TikTok 7708964677828578568, 90.4 s, 1080x1920, 30 fps) — DBL / komunitas sekolah sebagai aset bisnis

Semua gambar bukti: `work/ref/v2/` (path relatif ke /home/user/jobs/bench01).
- 1-fps overview: `sheet1fps_0.jpg` (0–43 s), `sheet1fps_1.jpg` (44–87 s), `sheet1fps_2.jpg` (88–90 s)
- 20 dense strips: `strip01_…` s/d `strip20_…` (label = nomor frame + detik; urutan frame dari satu decode, akurasi ±1 frame)
- Full-res: `full/fNNNNN.jpg` (23 frame) + grid `fullgrid_types.jpg`, `fullgrid_extra.jpg`
- Script sendiri: `strip.py`, `sheet1fps.py`, `frame.sh`

> PERINGATAN KIT: `tools/sheet.py video` menulis setiap frame ke file bersama `/tmp/_frame.jpg`. Saat tiga worker menjalankannya
> bersamaan, frame dari video lain masuk ke sheet kita (sheet v2 pertama saya berisi frame v1/v3: pria baju garis, wanita, teks
> "semprot…", "BDSM"). Sheet itu sudah saya hapus dan saya buat ulang dengan `sheet1fps.py` (temp dir sendiri). Bukti decode yang
> benar di 6.0 s: `evidence_seek_check_f180.jpg`. Sheet v1/v3 dari worker lain perlu dicek ulang.

---

## A. NEWS / ARTICLE CUT-OUTS (video ini SANGAT bergantung pada artikel: 9 kemunculan dokumen)

Tidak ada device frame, tidak ada browser chrome, tidak ada kartu ber-shadow, tidak ada rotasi, tidak ada "paper cut". Dokumen
tampil **full-bleed sebagai teks di atas latar** (bukan kartu yang melayang). Tiga gaya, dipilih per sumber:

| # | Waktu | Sumber | Gaya | Bukti |
|---|---|---|---|---|
| 1 | 0.0–3.6 | DBL.ID headline + byline + tanggal | **Kartu headline overlay di atas pembicara**: bar hitam atas berisi logo "DBL.ID", kotak putih berisi judul 2 baris (sans bold hitam), byline abu "Kiko Amalia Putri - 22 November 2025". Sudut siku, tanpa shadow, lebar ~79% frame, y≈1195–1425 (62–74% tinggi). Sudah ada sejak frame 0 (tanpa animasi masuk) | `full/f00015.jpg`, `full/f00060.jpg`, `strip01_hook_f0.jpg` |
| 2 | 15.3–20.2 | dbl.id (artikel presale) | **Teks putih di atas latar gelap bertekstur grain/goresan**, logo DBL.ID biru di atas paragraf. Highlight = **kotak putih, teks jadi hitam** (invert), menyapu kiri→kanan per baris | `full/f00520.jpg`, `strip06_article_dblid_f455.jpg` |
| 3 | 22.9–27.1 | headline DBL.ID yang sama dengan hook | Judul putih bold di atas foto stadion yang digelapkan; highlight kotak abu-terang pada "15.729 Penonton"; lalu **lompat zoom ~2.3x** sampai kalimat terpotong di tepi kiri (sengaja) | `full/f00780.jpg`, `strip08_headline_zoom_f680.jpg` |
| 4 | 28.9–32.6 | ANTARA JABAR | Teks putih + logo kecil di atas foto penonton stadion yang digelapkan; highlight kotak putih (invert) | `full/f00940.jpg` (di `fullgrid_types.jpg`), `strip09_antara_f862.jpg` |
| 5 | 36.4–40.3 | artikel "Penggunaan Konsep Student Athlete" | **Halaman terang**: latar abu dengan vignette radial, judul hitam, **stabilo kuning** menyapu per baris mengikuti ucapan (berhenti di tengah kata, "berprest|asi"); paragraf yang tidak di-highlight jadi **pudar + blur** (focus pull) | `full/f01150.jpg`, `strip10_studentathlete_f1088.jpg` |
| 6 | 42.5–45.0 | kutipan dbl.id ("source : dbl.id") | Teks putih kecil di kiri atas, di atas **b-roll tim dance** yang digelapkan; highlight invert per baris | `full/f01320.jpg`, `strip11_article_overbroll_f1270.jpg` |
| 7 | 45.0–46.6 | headline dbl.id "Gak Cuma Tim Basket dan Dance, Suporter Juga Bisa Ikut Berkompetisi!" + "Rena Dwi Astuti - 27 August 2022" + "source : dbl.id" | Headline bold putih di atas foto suporter yang digelapkan; highlight invert menyapu "Suporter Juga Bisa Ikut Berkompetisi" | `full/f01380.jpg`, `strip11_…` |
| 8 | 52.2–54.7 | kutipan dbl.id tentang pendiri & Amerika | Teks putih di atas **foto seorang pria dengan mikrofon yang digelapkan** (kemungkinan tokoh yang dikutip; identitas tidak saya verifikasi) | `full/f01600.jpg` (di `fullgrid_extra.jpg`), `strip16_honest_amerika_f1505.jpg` |
| 9 | 56.3–59.4 | KOMPAS | Halaman terang, font serif asli Kompas, logo KOMPAS; stabilo kuning "Tahun ini, ada 17 sponsor yang akan mendukung DBL" | `full/f01720.jpg`, `strip12_kompas_f1636.jpg` |
| 10 | 63.0–66.4 | HARIAN SURABAYA (.com) | **Screenshot mobile asli** (header situs dengan ikon menu & search terlihat kabur di atas, font Verdana-like). Paragraf fokus tajam + stabilo kuning "DBL Seri Surabaya … disponsori oleh Honda"; paragraf lain pudar abu + vignette | `full/f01950.jpg`, `strip17_sponsor_harian_f1778.jpg` |

Detail umum:
- **Isi**: hanya headline+byline (1,3,7) atau 1–3 paragraf berisi kalimat bukti (lainnya). Tidak pernah ada foto artikel / thumbnail.
  Sumber selalu terbaca: logo media (DBL.ID, ANTARA, KOMPAS, HARIAN SURABAYA) atau "source : dbl.id"; tanggal hanya di headline.
- **Crop**: tidak ada bingkai sama sekali. Teks memenuhi lebar ±75–85% frame (margin ±110–170 px), blok teks berada di y≈350–1150.
  Pada zoom (3, dan akhir #2) teks sengaja terpotong di tepi frame — yang penting hanya baris yang di-highlight.
- **Highlight**: dua gaya, konsisten dengan latar: latar gelap → **kotak putih/abu terang, teks dalam kotak jadi hitam**; latar terang →
  **stabilo kuning-lime** (multiply). Keduanya **menyapu kiri→kanan, baris per baris**, kecepatan mengikuti ucapan (bisa berhenti
  di tengah kata: `full/f01150.jpg`, `full/f01380.jpg`, `full/f01600.jpg`). Satu baris ±10–16 frame.
- **De-emphasis**: teks yang tidak relevan diturunkan opacity-nya dan di-blur (Student Athlete, Harian, Kompas sedikit), sehingga
  mata langsung ke kalimat bukti (`full/f01150.jpg`, `full/f01950.jpg`).
- **Durasi**: 1.6–4.9 s per dokumen (rata-rata ±3.3 s); cukup untuk highlight 1–3 baris.
- **Masuk**: hampir selalu **blur-in** (defocus → tajam) 6–16 frame + sedikit scale turun (`strip06` f459→f475, `strip08` f686→f700,
  `strip11` f1276→f1285, `strip12` f1688→f1694, `strip17` f1890→f1898). Student Athlete: hard cut lalu highlight langsung jalan.
- **Gerak selama tampil**: zoom/pan pelan (drift), atau **zoom kamera ke baris yang sedang dibicarakan** (#2: f535→f555 ±20 frame ke
  "47 jam"; #3: lompatan zoom keras di f740 tepat saat "15" diucapkan).
- **Keluar**: hard cut ke visual berikut, atau **flash/bloom putih + blur** ke pembicara (#2 f603→f611 `strip07_bw_liga_f598.jpg`;
  #3 f810→f814 ke foto arena), atau **fade ke hitam** lalu pembicara fade-up (#5 f1200→f1220 `strip10`).
- **Jangkar kata** (word idx dari v2_words.json): #2 masuk di "Yang pre-sale-nya" (15.3), highlight ke-2 di "tiket normalnya" (18.0),
  zoom ke "47 jam" (19.2); #3 masuk "finalnya DBL Jakarta" (23.3), zoom pada "15" (24.5); #5 masuk tepat "Student" (36.28);
  #9 Kompas di "Dari sejarah" (56.2) sebelum "sponsor" (58.7); #10 Harian tepat di "Honda" (62.98).

## B. DI BELAKANG CUT-OUT

- Tidak ada desain grafis buatan (tidak ada gradient/grid/shape). Latar selalu **foto/footage nyata yang relevan, digelapkan kuat**
  (brightness kira-kira 20–35%) dan sedikit blur, atau **halaman terang dengan vignette abu radial**.
  - Artikel presale (#2): tekstur gelap grain/goresan (`full/f00520.jpg`).
  - Headline 15.729 (#3): foto stadion penuh penonton, digelapkan; sebelum keluar latar dicerahkan lalu flash (`strip08` f810).
  - ANTARA (#4): foto penonton pertandingan internasional (`full/f00940.jpg`).
  - Kutipan dance (#6): b-roll tim dance; headline suporter (#7): foto suporter di tribun (`full/f01320.jpg`, `full/f01380.jpg`) →
    **latar = ilustrasi dari kalimat yang di-highlight**.
  - Kutipan pendiri (#8): foto orang yang dikutip (`full/f01600.jpg`).
  - Kompas/Student Athlete/Harian/sponsor: putih→abu radial vignette (`full/f01150.jpg`, `full/f01720.jpg`).
- **Pembicara tidak pernah terlihat di belakang dokumen** (kecuali hook #1). Dokumen = layar penuh.
- **Hook (0–3.6 s)**: pembicara di-punch-in (wajah ±1.3x lebih besar f15→f60), latar ruangan diganti/ditumpuk foto basket
  (kiri sepia penonton, kanan B&W ring), dan **logo DBL INDONESIA muncul DI BELAKANG kepala pembicara** (pembicara di-matte /
  segmentasi) mulai f30–f36 (fade + sedikit naik). Bukti `strip01_hook_f0.jpg`, `full/f00060.jpg`.
  Teknik "logo di belakang kepala" diulang 3x lagi: 33.6 s "ternyata gini strateginya mereka" (pembicara digeser ke kanan, logo
  kiri — `strip15_arena_logo_f975.jpg` f1006–f1040), 70.5 s "dipelajari dari DBL" (`strip18_crowd_logo_f2030.jpg` f2114–f2142,
  `full/f02130.jpg`), dan 89.5 s "ke DBL?" (`strip20_ending_f2470.jpg` f2686–f2710). Di momen itu latar ruangan jadi gelap.
- **Poster (78–79.7, 82.5–86.3)**: poster asli di tengah (lebar ±60–75%), **latarnya salinan poster yang sama diperbesar + blur +
  vignette** (blur-fill), push-in pelan (`full/f02380.jpg`, `full/f02550.jpg`, `strip19_poster_f2286.jpg`, `strip20_…`).
- **Foto pemain (3.6–5.5)**: foto di "kartu" hampir layar penuh (margin ±45 px), sudut membulat, tepi gelap/vignette lembut di atas
  latar hitam (`full/f00115.jpg`, `strip02_cut_photo_f100.jpg`). Foto resolusinya rendah (lembut) — tetap dipakai karena asli.

## C. SUBTITLE / ANIMASI TEKS — dua mode yang berganti otomatis

**Mode BESAR (saat pembicara di layar, ±85% waktu pembicara)** — `full/f01230.jpg`, `strip10` f1212–f1272, `strip12` f1642–f1686,
`strip18` f2102–f2142, `strip19` f2394–f2463, `strip20` f2590–f2710:
- Posisi: tengah, y≈1150–1420 (60–74% tinggi), di atas dada pembicara, di bawah dagu. Tanpa kotak; shadow lembut saja.
- Hierarki 2–3 level dalam satu chunk:
  1. kata penghubung kecil (sans putih ±40 px) di atas: "dan ini", "terus", "yang", "dipelajari", "jadi “pondasi”", "kalau kalian";
  2. baris utama **sans sangat tebal, putih, ±100–120 px** (lebar s/d ±70% frame): "mereka", "gimana cara", "dapat duit", "punya";
  3. baris kedua **serif italic bold kuning-lime (±#E5EA3C)**, sedikit overlap ke baris 1: "sengaja", "komunitas", "dari mana?", "brand", "bisnis".
  Variasi: kata kunci tunggal ditulis **sans tebal kuning** di baris utama ("sekolah", "contoh", "bisnisnya", "dari DBL", "jual tiket",
  "uniknya") dengan penghubung kecil putih di atasnya. Kata dalam tanda kutip kecil (“satu”, “pondasi”) = penekanan ironi.
- Isi chunk: 2–4 kata, satu frasa makna; teks lowercase (kecuali "DBL"), kadang diparafrase dari ucapan ("gw udah nanya sekitar").
- Kemunculan: **per kata**, opacity naik dari ±35% abu ke 100% dalam ±4–6 frame, disertai sedikit blur→tajam (bukan pop/scale/slide)
  (`strip18` f2102 "menurut gw" kabur-abu → f2108 tajam putih; `strip10` f1224 "mereka" abu → f1228 putih; baris kuning juga mulai
  gelap/olive lalu kuning penuh f1228–f1232). Chunk berganti dengan hard replace.
- B&W: di "tapi gilanya" (11.2 s) dan "“liga pelajar”" (20.8 s) seluruh frame pembicara jadi hitam-putih (`strip14_bw_billboard_f330.jpg`
  f337–352, `strip07_bw_liga_f598.jpg` f624–627).

**Mode KECIL (di atas semua insert, dan di beberapa momen pembicara yang "tenang")** — `full/f00015.jpg`, `full/f00115.jpg`,
`full/f00430.jpg`, `full/f01150.jpg`, `full/f01950.jpg`, `full/f01530.jpg`:
- Sans medium/semibold putih ±44 px, **di dalam chip bersudut bulat**: hitam transparan (±50%) di atas latar gelap, **abu medium
  transparan** di atas halaman terang (tetap teks putih). Posisi tetap y≈1190–1275 (±64% tinggi), selalu di tengah.
- 2–3 kata per chunk, diganti per frasa (tanpa animasi per kata yang terlihat).
- Juga dipakai di pembicara: hook 0–3.6 (karena ada kartu headline), 50.4–52.2 ("dan let's be honest / ini bukan / strategi baru" —
  shot lebih dekat, nada pengakuan), 59.4–60.5, 75.1–76.4, 88.3–89.4 — yaitu kalimat sambungan yang tidak punya kata kunci.

**Banding kit kita (`Main.tsx Subs`)**: kit sudah punya struktur "baris kecil + kata besar serif italic aksen" — mirip mode besar
ini, tetapi terbalik: di referensi **baris utama yang BESAR adalah sans putih**, serif italic kuning adalah baris kedua; kit membuat
baris pertama kecil 50 px. Kemunculan referensi = opacity+blur per kata, kit = spring scale-pop (0.7→1). Referensi punya **mode
chip kecil terpisah untuk insert**; kit memakai gaya yang sama di semua tempat (hanya warna ink saat `light`). Posisi referensi ±80 px
lebih tinggi (y 1150–1420 vs kit 1270–1530).

## D. JENIS VISUAL LAIN

| Jenis | Kapan | Asli/gambar? | Penyajian | Bukti |
|---|---|---|---|---|
| Foto pemain (3 foto, 0.33–0.6 s tiap foto) | "mereka tuh sebenernya simple banget" | foto asli | kartu hampir full, sudut bulat, hard cut cepat, drift pelan | `strip02`, `full/f00115.jpg` |
| **Counter angka** 9→22 "TAHUN" + kicker kuning italic "2004-now" | "Tapi kok bisa tahan sampe 20 tahun lebih?" | teks animasi di atas b-roll dunk digelapkan | angka naik 1/frame (f166 "9" → f177 "20" → f181 "22"), "TAHUN" fade-in f177–180; angka metalik putih-abu | `strip13_counter_f160.jpg`, `strip03_22tahun_f205.jpg` |
| Logo DBL INDONESIA | "pasti tau namanya DBL" | logo asli di atas render/foto lapangan terang yang di-blur | logo naik + blur-in f257–f262 (±5 frame), lalu diam | `strip04_sma_dbl_f252.jpg`, `full/f00280.jpg` |
| Footage pertandingan (watermark "DBL PLAY") | "Ini Liga Basket Pelajar" | footage asli | full-bleed | `full/f00300.jpg` |
| Billboard di gedung (foto B&W, **poster tetap berwarna** — selective colour) | "tiket mereka di 2026" | foto asli, diolah | full-bleed, hard cut tepat di kata "tiket" (11.76) | `strip14_bw_billboard_f330.jpg` f353 |
| Seat plan + harga tiket resmi | "bisa sampe 750 ribu" | grafis resmi asli | **zoom ke baris "1A IDR 750,000"**, harga itu distabilo kuning, harga lain dipudarkan, vignette merah, kamera geser kanan | `strip05_billboard_seat_f385.jpg`, `full/f00430.jpg` |
| Foto udara Indonesia Arena | "di Indonesia Arena" (27.1) dan "di tempat yang sama" (32.6) | foto/footage asli | full-bleed, masuk via flash putih | `strip08` f812, `strip15` f978 |
| Footage penonton/suporter (6 klip) | semua kalimat tentang komunitas sekolah, "akses ke komunitas", "orang dateng buat dukung sekolahnya" | footage asli (logo "Central Java-South", sponsor terlihat) | full-bleed 1.3–2.4 s, hard cut | `full/f01450.jpg`, `strip18`, `strip19` |
| Grafik sponsor resmi (Presented by Honda / Good Day / partners) | "kerjasama mereka sama brand" | grafis resmi asli | full-bleed di latar terang vignette, zoom-out pelan | `full/f01850.jpg`, `strip17` |
| Poster sponsor & poster Final 21 Nov | "brand masuk buat dapetin anak muda", "tanggal 21 November … final" | poster resmi asli | blur-fill (salinan poster blur di belakang), push-in pelan | `full/f02380.jpg`, `full/f02550.jpg` |
| Logo di belakang pembicara | 4x (lihat B) | logo asli + matte pembicara | lihat B | `full/f00060.jpg`, `full/f02130.jpg` |
| B&W pembicara (punchline) | "tapi gilanya", "“liga pelajar”" | efek warna | hard cut ke B&W | `strip07`, `strip14` |

Tidak ada: meme, chart buatan, peta, screen recording, UI drawn in code, chat bubble, end card. Satu-satunya grafis "buatan" adalah
counter angka (teks).

## E. RITME — tabel kalimat → visual

Layout: S = pembicara (sub besar), S* = pembicara + elemen (logo/kartu/B&W), F = layar penuh.

| Waktu (s) | Diucapkan | Ditampilkan | Layout | Durasi |
|---|---|---|---|---|
| 0.0–3.6 | Kalo customer kalian Gen Z, ini gila sih, kalian harus coba pelajarin strateginya DBL. | punch-in + latar foto basket + logo DBL di belakang kepala (1.0 s) + kartu headline "Rekor! 15.729 penonton…" | S* | 3.6 |
| 3.6–5.5 | Ya menurut gua, mereka tuh sebenernya simple banget. | 3 foto pemain DBL (0.33/0.33/1.2 s) | F | 1.9 |
| 5.5–7.0 | Tapi kok bisa tahan sampe 20 tahun lebih? | counter 9→22 TAHUN "2004-now" di atas dunk | F | 1.5 |
| 7.0–8.6 | Gua nanya sekitar yang pernah SMA | pembicara (masuk via flash), sub besar "gw udah / nanya sekitar", "yang pernah / SMA" | S | 1.6 |
| 8.6–9.7 | …pasti tau namanya DBL. | logo DBL INDONESIA di lapangan | F | 1.1 |
| 9.7–11.2 | Ini Liga Basket Pelajar. | footage pertandingan DBL PLAY | F | 1.5 |
| 11.2–11.8 | Tapi gilanya, | pembicara B&W | S* | 0.5 |
| 11.8–13.1 | tiket mereka di 2026 | billboard B&W + poster berwarna | F | 1.3 |
| 13.1–15.3 | itu bisa sampe 750 ribu rupiah. | seat plan, zoom ke 1A IDR 750,000 (stabilo) | F | 2.3 |
| 15.3–20.2 | Yang pre-sale-nya bisa abis dalam 1 jam. Dan tiket normalnya abis dalam 47 jam. | artikel dbl.id gelap, 2 highlight + zoom ke "47 jam" | F | 4.9 |
| 20.2–22.9 | Gua ulangin ya, Liga Pelajar. Kalo mau tau demand-nya mereka, | pembicara (flash in), B&W pada "liga pelajar" 20.8–21.7 | S / S* | 2.7 |
| 22.9–27.1 | finalnya DBL Jakarta itu sampe 15.729 penonton | headline DBL.ID di atas stadion, highlight + lompat zoom "15.729 Penonton" | F | 4.2 |
| 27.1–28.0 | di Indonesia Arena. | foto udara Indonesia Arena | F | 0.9 |
| 28.0–28.9 | Itu lebih rame dari | pembicara "itu lebih rame / dari.." | S | 0.9 |
| 28.9–32.6 | game Piala Dunia Basket 2023 antara Kanada sama Spanyol. | artikel ANTARA di atas penonton, highlight | F | 3.7 |
| 32.6–33.5 | Di tempat yang sama, | foto udara Indonesia Arena (lagi) | F | 0.9 |
| 33.5–36.4 | ternyata gini strateginya mereka. Yang bikin beda, mereka punya konsep yang namanya | pembicara geser kanan + logo DBL kiri belakang; lalu flash → pembicara normal, sub besar | S* / S | 2.9 |
| 36.4–40.3 | Student Athlete. Jadi pemainnya gak boleh cuma jago basket, tapi akademiknya juga harus bagus. | artikel terang, stabilo per baris, blur sisa | F | 3.9 |
| 40.3–42.5 | Dan uniknya, mereka sengaja ngelibatin satu sekolah. | pembicara, sub besar "uniknya", "mereka/sengaja", "ngelibatin “satu”/sekolah" | S | 2.2 |
| 42.5–45.0 | Bahkan tim basketnya daftar, wajib punya tim dance, | kutipan dbl.id di atas b-roll tim dance | F | 2.5 |
| 45.0–46.6 | belum lagi kompetisi supporter. | headline "Suporter Juga Bisa Ikut Berkompetisi!" di atas suporter | F | 1.6 |
| 46.6–50.4 | Jadi yang punya alasan buat dateng bukan cuma fansnya basket, tapi satu komunitas sekolah itu. | 2 klip penonton (lampu HP, tribun penuh) | F | 3.8 |
| 50.4–52.2 | Dan let's be honest, ini bukan strategi baru. | pembicara shot lebih dekat, sub KECIL | S | 1.8 |
| 52.2–54.7 | Konsep Liga Pelajarnya itu terinspirasi dari Amerika. | kutipan dbl.id di atas foto tokoh digelapkan | F | 2.5 |
| 54.7–56.3 | Terus, bisnisnya dapet duit dari mana? | pembicara, "terus/bisnisnya", "dapat duit/dari mana?" | S | 1.6 |
| 56.3–59.4 | Dari sejarah, mayoritas duitnya DBL itu dateng dari sponsor. | Kompas, stabilo "17 sponsor" | F | 3.2 |
| 59.4–60.5 | Dan menariknya, | pembicara, sub kecil | S | 1.1 |
| 60.5–63.0 | kerjasama mereka sama brand bisa panjang banget. | grafik sponsor resmi | F | 2.4 |
| 63.0–66.4 | Honda udah 18 tahun jadi sponsor mereka tanpa berhenti. | Harian Surabaya, stabilo kalimat Honda | F | 3.4 |
| 66.4–67.9 | Bukan cuma dapet duit dari jual tiket, | pembicara "bukan cuma/dapat duit", "dari/jual tiket" | S | 1.6 |
| 67.9–70.1 | tapi brand-brandnya jadi punya akses ke komunitas sekolah. | footage tribun putih | F | 2.1 |
| 70.1–71.5 | Menurut gue yang bisa dipelajari dari DBL | pembicara, logo DBL muncul di belakang pada "dipelajari" | S* | 1.4 |
| 71.5–75.1 | itu gimana mereka bikin komunitas sekolah jadi pasar yang menghasilin uang | 2 klip suporter (merah, kuning) | F | 3.7 |
| 75.1–76.4 | dari banyak arah. | pembicara, sub kecil | S | 1.3 |
| 76.4–78.0 | Orang dateng buat dukung sekolahnya, | footage banner suporter | F | 1.6 |
| 78.0–79.7 | brand masuk buat dapetin anak muda. | poster sponsor, blur-fill | F | 1.7 |
| 79.7–82.5 | Dan ini contoh gimana cara komunitas jadi fondasi sebuah bisnis. | pembicara, 3 chunk sub besar | S | 2.8 |
| 82.5–86.3 | Terus, tanggal 21 November juga bakal ada final DBL Jakarta di Indonesia Arena lagi. | poster Final resmi, blur-fill | F | 3.8 |
| 86.3–90.4 | Kalau kalian punya brand, targetnya? Anak muda. Kalian sendiri tertarik nggak buat dateng ke DBL? | pembicara, sub besar; logo DBL di belakang pada "ke DBL?" (89.5) | S → S* | 4.1 |

Hitungan (dari cut yang terdeteksi `ffmpeg scene>0.12` + inspeksi strip):
- **Beat visual**: 28 visual layar penuh berbeda + 7 beat di atas pembicara (kartu headline, 4x logo-di-belakang, 2x B&W) = **±35 beat
  dalam 90 s → satu beat tiap ±2.6 s** (jauh lebih padat dari baseline STYLE_NOTES ±5 s).
- **Waktu**: layar penuh ±60.4 s (**67%**), pembicara ±30.0 s (33%), di dalamnya pembicara + elemen ±8 s.
- **Run pembicara terpanjang 4.1 s** (penutup), lainnya 0.5–3.6 s. Blok insert terpanjang tanpa kembali ke pembicara 8.4 s
  (11.8–20.2: billboard → seat plan → artikel), tetapi di dalamnya visual berganti tiap 1.3–4.9 s dan ada gerak (highlight/zoom).
  Tidak ada 1 gambar diam > 5 s.
- **Hook 3 detik pertama**: visual = bukti (headline "Rekor! 15.729 penonton") sudah di layar dari frame 0 + punch-in + logo brand
  di belakang kepala pada detik 1; verbal = panggilan audiens ("customer kalian Gen Z") + "ini gila sih". Hard cut pertama di 3.6 s.
- **Penutup/CTA**: tidak ada end card. Pertanyaan ke penonton dengan sub besar + logo DBL muncul di belakang kepala 1 detik terakhir.
  (Catatan: STYLE_NOTES menyebut "full-screen real ending" — video ini tidak; penutupnya pembicara + logo.)
- Transisi: mayoritas hard cut tepat di awal kata. Flash/bloom putih 4–5x (7.0, 20.2, 27.1, 34.7 s), fade-ke-hitam 1x (40.3 s),
  blur-in di hampir semua dokumen.

## F. CARA BERPIKIR EDITOR (prinsip yang bisa dipakai model mana pun)

1. **Klaim faktual → dokumen bukti asli, kalimatnya disorot.** Setiap angka/fakta (750 ribu, 1 jam, 47 jam, 15.729, Piala Dunia,
   Student Athlete, 17 sponsor, Honda 18 tahun) muncul sebagai sumber nyata dengan kalimat yang persis diucapkan di-highlight,
   saat itu diucapkan. Penonton tidak perlu percaya pada pembicara — mereka membaca buktinya. Layar penuh, karena teks harus terbaca.
2. **Highlight bergerak mengikuti mulut.** Stabilo/kotak menyapu dengan kecepatan bicara, kadang berhenti di tengah kata; zoom kamera
   pindah ke baris berikutnya ketika pembicara pindah ke angka berikutnya ("1 jam" → "47 jam"). Dokumen = panggung untuk satu kalimat.
3. **Yang tidak relevan dibuang secara visual**, bukan dipotong: paragraf lain dipudarkan/blur, harga lain di seat plan dipudarkan,
   gedung jadi B&W sementara poster tetap berwarna. Satu titik fokus per layar.
4. **Abstrak/emosional → footage nyata orangnya.** "Komunitas sekolah", "alasan buat dateng", "akses ke anak muda" selalu dijawab
   dengan tribun penuh suporter (1.5–2.4 s, cukup untuk "merasakan", tidak untuk dibaca).
5. **Latar dokumen = ilustrasi isi dokumen** (artikel dance di atas tim dance, headline suporter di atas suporter, kutipan pendiri di
   atas foto tokoh, artikel Piala Dunia di atas penonton) — digelapkan supaya teks tetap terbaca.
6. **Pembicara kembali hanya untuk opini, pertanyaan, dan sambungan retoris** ("gua ulangin ya", "let's be honest", "dapat duit dari
   mana?", "ini contoh…"). Di situ sub besar membawa kata kunci; sambungan tanpa kata kunci pakai sub kecil.
7. **Brand milik cerita, bukan stiker**: logo DBL ditaruh di belakang kepala (pembicara tetap di depan) setiap kali kalimat menyebut
   "strategi mereka/DBL" sebagai subjek — 4x, konsisten, jadi motif visual video.
8. **Angka yang bisa dihitung dibuat hidup**: "20 tahun lebih" → counter yang berhenti di angka yang lebih tepat (22, "2004-now").
9. **Kontras ritme**: dokumen terang ↔ gelap bergantian, foto cepat 0.3 s di awal (energi), dokumen 3–5 s di tengah (bukti),
   footage 1.5–2 s (rasa). B&W hanya 2x untuk kata yang ingin "dihentikan" ("gilanya", "liga pelajar").
10. **Ukuran**: dokumen/poster layar penuh (harus dibaca); kartu headline di hook ukuran sedang di bawah wajah (wajah = hook, kartu =
    bukti); logo selebar ±75% frame di belakang kepala (dramatis tapi tidak menutup wajah).

## Klasifikasi teknik vs kit kita (`skill/reference/edit-json.md`, `video/src/Visuals.tsx`, `Main.tsx`)

| Teknik | Status | Catatan |
|---|---|---|
| Footage b-roll full-bleed (pertandingan, tribun) | **Bisa sekarang** | `clip` (tanpa `label`) |
| Foto udara arena full-bleed | **Bisa sekarang** | `photo` |
| Hard cut antar insert (bukan slide) | **Parameter kecil** | `Insert` selalu fade-in 7f / push-slide saat berantai → tambah `transition: "cut"` |
| B&W pembicara (punchline) | **Parameter kecil** | belum ada di kit; tambah event `look` {start,end, `grayscale`, `dim`} yang memberi filter ke `<Speaker>` |
| Flash/bloom putih + blur sebagai transisi | **Parameter kecil** | opsi `transition: "flash"` di Insert: 3–5 frame brightness 1→2.5 + blur 0→12px lalu kembali |
| Blur-in masuk (defocus→tajam 8–14 f) | **Parameter kecil** | opsi `enter: "blur"` di Insert (filter blur 16→0 + scale 1.04→1) |
| Poster/grafik resmi di atas salinannya yang di-blur | **Parameter kecil** | `screenshot` sudah punya `BlurBg`, tapi kartunya punya radius 28, shadow, rotasi masuk, label "SUMBER" → opsi `chrome:false`, `card_w`, tanpa rotasi |
| Grafik sponsor di latar terang vignette | **Parameter kecil** | `photo` + `fit:"contain"` + `bg` vignette (sekarang `cover` saja) |
| Kartu foto inset (margin ±45px, sudut bulat, tepi gelap) + montase cepat 0.3–0.6 s | **Parameter kecil** | `photo` + `inset`, `radius`; berantai dengan `transition:"cut"` |
| Logo di atas latar foto blur (logo naik + blur-in 5 f) | **Parameter kecil** | `photo` + field `logo` (tengah, w%) dengan animasi naik |
| Pembicara bergeser kiri/kanan untuk memberi ruang | **Parameter kecil** | `framing` sekarang per klip, bukan per waktu → tambah `x` di `shots`/event `reframe` |
| Subtitle 2 mode (besar sans putih + serif italic aksen; chip kecil di atas insert) | **Perubahan sedang di `Subs` (generik)** | lihat C: tukar hierarki (baris utama besar sans), reveal per kata opacity 0.35→1 + blur 6→0 px dalam 5 f (ganti spring scale), mode `chip` otomatis saat full insert aktif (chip rgba(0,0,0,.5) / abu di `light`, 44 px, frasa 2–3 kata), posisi y≈1150–1420 |
| **Dokumen full-bleed dengan kamera + highlight tersinkron** (artikel gelap/terang, seat plan, headline zoom) | **Perlu PRIMITIF BARU generik: `doc`** | Input: `img` (screenshot asli) ATAU `text` {logo, paragraphs[], headline, byline, source} untuk re-typeset; `bg` (img/clip + `dim` 0.2–0.35, atau `paper` = abu terang + vignette radial); `style` `dark`/`light`; `highlights` [{rect atau rentang kata/baris, `at` jangkar, `until` jangkar}] → wipe kiri→kanan per baris, durasi per baris = waktu ucapan rentang itu (bukan 14 f tetap); gaya highlight `invert` (kotak putih, teks hitam) di dark / `marker` kuning multiply di light; `defocus_others` (opacity 0.35 + blur 2–3 px untuk teks di luar highlight aktif); `camera` keyframes [{at, rect fokus, `ease` atau `jump`}] → scale/translate supaya rect fokus memenuhi ±85% lebar (boleh memotong tepi); masuk blur-in 8–14 f; keluar cut/flash/fade-black. Menyajikan aset NYATA — bukan gambar konten |
| **Kartu headline overlay di atas pembicara** (hook) | **Perlu PRIMITIF BARU generik: `headline`** (overlay) | Input: `source_logo` (img) atau `source` teks, `headline`, `byline`, `y` (default 1190), `w` (default 860); gaya: bar hitam + kotak putih, sudut siku, tanpa shadow; muncul 0–4 f (atau sudah ada di frame 0); bisa pakai crop gambar asli headline (`img`) sebagai pengganti teks |
| **Counter angka** (9→22 + unit + kicker) | **Perlu PRIMITIF BARU generik: `counter`** (animasi teks) | Input: `from`, `to`, `at` (jangkar kata angka), `unit`, `kicker`, `bg` (img/clip + dim). Gerak: integer naik 1 per frame (atau easeOut bila selisih besar) selesai ±2 f sebelum angka diucapkan; unit fade-in 3 f saat ±90%; angka besar ±300 px |
| **Logo di belakang kepala pembicara** (+ ganti latar ruangan) | **Perlu PRIMITIF BARU + tool pra-proses** | Butuh matte pembicara per frame (mis. background-matting/segmentasi video di CPU — berat, belum ada di kit). Primitif `behind`: {start,end, `img` logo, `y`, `w`, `bg` opsional, enter fade+naik 6 f}; Speaker dirender 2 lapis (latar, logo, lalu pembicara ber-alpha). Tanpa matte: hanya bisa logo di atas kepala (tidak overlap) — bukan efek yang sama |
| Selective colour (foto B&W, satu objek tetap berwarna) | **Persiapan aset** (bukan motion) | dibuat di aset dengan mask (PIL/ffmpeg) lalu `photo`; perlu mask manual/segmentasi |

## Yang TIDAK bisa saya tentukan

- Audio: tidak bisa mendengar — SFX (whoosh di flash?), musik latar, level suara tidak diketahui.
- Nama font pasti (sans tampak seperti grotesk tebal ala Helvetica/Inter Black; serif italic kontras tinggi; artikel gelap tampak
  Montserrat-like). Hanya karakter yang saya catat.
- Apakah artikel dbl.id / ANTARA (gaya gelap) adalah **teks yang di-retype** oleh editor atau screenshot mode gelap — tipografinya
  seragam (font yang sama di dbl.id dan ANTARA) sehingga kemungkinan besar diketik ulang, tetapi tidak terbukti. Harian Surabaya
  jelas screenshot asli (header situs terlihat); Kompas kemungkinan screenshot asli (font serif Kompas).
- Apakah latar render lapangan di 8.6 s dan foto udara Indonesia Arena adalah foto asli atau render/AI — tampak seperti render 3D/foto
  udara bersih; tidak saya verifikasi.
- Identitas pria di latar kutipan 52–54.7 s (kemungkinan pendiri yang dikutip) tidak diverifikasi.
- Cara matte pembicara di hook (rotoscope manual vs AI) — hanya hasilnya yang terlihat.
- Perbedaan shot 50.4–52.2 s (lebih dekat, sedikit lebih gelap) bisa punch-in digital atau kamera kedua — tidak bisa dipastikan.
- Ketelitian frame: strip berasal dari satu decode berurutan setelah seek; label bisa meleset ±1 frame (bandingkan
  `evidence_seek_check_f180.jpg`).
