# notes_v3 — TikTok 7473068001151978758 (@raymondchins), 90.1 s, 720x1280, 30 fps

Topik: "BDSM PA" segment (Bedah Bisnis Satu Menit…) — dua orang (host pria = penjelas, host wanita = penanya/reaksi) membedah iklan AXE "smells better than Chanel" di Times Square.
Semua path gambar relatif ke `/home/user/jobs/bench01/work/ref/v3/`. Frame = nomor frame 30 fps; waktu = detik video.
Transkrip: `work/ref/v3_transcript.txt`, `v3_words.json` (Whisper mendengar "X" untuk AXE, "Blue de Chanel" untuk Bleu de Chanel, "BDSMPE" untuk BDSM PA, "Bersabisnis" untuk Bedah Bisnis).

## 0. PERINGATAN METODE (penting untuk semua worker)
`tools/sheet.py` (mode `video`/`strips`) menulis setiap frame ke **satu file bersama `/tmp/_frame.jpg`**. Saat 3 worker
menjalankannya bersamaan, frame dari video lain masuk ke sheet. Sheet 1-fps pertama saya (`CONTAMINATED_sheet1fps_*.jpg`)
berisi potongan artikel DBL / "Student Athlete" dari v1/v2 di detik 37, 59, 67, 73 — itu BUKAN isi v3.
Bukti: `chk_59cmp.jpg` (frame 1770 dari pipe = wanita "WOOOOHHHH", bukan artikel). Semua gambar lain di folder ini dibuat
dengan `scripts/grid.py` (ffmpeg pipe → numpy, tanpa file sementara) dan bebas kontaminasi. Sheet v1/v2 worker lain perlu dicek ulang. (Peringatan lead tentang bug ini sudah ditangani: satu-satunya gambar buatan sheet.py adalah `CONTAMINATED_sheet1fps_*`; diganti `sheet1fps_fixed_*` dan TIDAK ada klaim di catatan ini yang bersumber dari sheet yang terkontaminasi — semua dicek ulang terhadap `sheet1fps_fixed_*`, `shots_*` dan strip.)

Bahan: `sheet1fps_fixed_{0,1}.jpg` (1 fps), `shots_{0,1}.jpg` (frame tengah tiap shot, 80 shot), 25 strip padat `strips/s01…s25`,
frame resolusi penuh `full/f*.jpg` + `full_sheetA.jpg`, `full_sheetB.jpg`. Deteksi cut: `cuts.txt`, `hardcuts.txt` (selisih frame rata-rata > 20).
Analisis audio: di bawah kedua insert color-bar ada nada murni **1000 Hz** (peak share 0.32–0.41 vs 0.02 untuk ucapan) = bunyi sensor "tiiit".

## A. NEWS / ARTICLE CUT-OUTS
Video ini **hampir tidak memakai potongan berita**. Hanya ada SATU potongan teks artikel, dan itu bukan berita lokal/headline:

- **Isi**: satu paragraf saja (4 baris, bahasa Inggris) — "According to Axe, a blind scent test has found that 73 percent of guys prefer their favorite Axe Fine Fragrance scent over Bleu de Chanel. Thus triumphant, The Martin Agency has created what it's christened the "first-ever real-life ratio" to celebrate the collection's launch." Tanpa headline, tanpa foto, **tanpa logo/nama media/tanggal**. (`full/f870.jpg`, `full_sheetB.jpg` tile f890)
- **Crop**: sangat ketat — persis kotak paragraf; tepi persegi (tanpa sudut membulat), **tanpa frame device/browser, tanpa bayangan, tanpa rotasi**. Latar kotak putih/abu sangat muda (warna halaman aslinya). Lebar ≈ 91 % frame (margin ≈ 4 % kiri-kanan), tinggi ≈ 10 % frame, posisi y ≈ 27–37 % (sepertiga atas, di "ruang dinding" di atas kepala). Teks kecil (≈ 12 px di frame 720 → tidak dimaksudkan dibaca kata per kata; yang dibaca adalah stabilo).
- **Stabilo**: highlight **biru seperti seleksi teks browser** pada frasa klaim "73 percent of guys prefer their favorite Axe Fine Fragrance scent over Bleu de Chanel." Sudah ada sejak frame pertama — **tidak beranimasi** (strip `strips/s10_article_in.jpg`, `strips/s11_article_highlight.jpg`).
- **Masuk**: fade-in ≈ 7–8 frame (f842 tak terlihat → f849 penuh), muncul bersamaan dengan cut ke wide shot, pada kata "73" (#95, 28.00 s). Tidak ada slide/scale. **Keluar**: hard cut ke close-up wanita di f960 (32.00 s, "Perfume Chanel?").
- **Durasi**: 3.9 s (28.07–32.00), meliputi "73 % cowok" + "mereka lebih suka AXE daripada Bleu de Chanel".
- **Di belakang/di atasnya**: lapisan video **rumus kapur (chalkboard math)** yang bergerak/pan pelan, di-blend (screen) di sepertiga atas; coretan kapur bahkan menimpa kotak artikel (f890: huruf "collect… launch" tertutup kapur). Wide shot di bawahnya tetap jalan dan bahkan berganti angle di f884 tanpa mengganggu kotak (diff top 15 / bottom 30 di `cuts.txt`).
- **Subtitle selama artikel**: berubah jadi huruf kapital tebal ("73% COWOK", "MEREKA LEBIH SUKA AXE / daripada Bleu de Chanel" baris 2 kuning) — subtitle merangkum angka yang sama dengan stabilo.

Pengganti "berita" di video ini adalah **bukti visual asli**: footage billboard 3D AXE di Times Square (3x dipakai), satu ilustrasi Samsung-vs-Apple, satu foto iklan Coca-Cola vs Pepsi, ditambah judul konsep serif. Lihat D.

## B. DI BELAKANG / SEKITAR VISUAL
- **Pembicara tidak pernah disembunyikan oleh gambar.** Tidak ada insert layar penuh berupa foto/screenshot sama sekali. Layar penuh non-pembicara hanya 2× color bar 0.37 s (total 0.73 s = 0.8 %).
- **Pola utama "panel atas di headroom"**: wide two-shot direkam dengan banyak ruang dinding gelap di atas kepala (kepala di ±45–60 % tinggi frame). Gambar ditaruh **full-bleed, rata kiri-kanan, menempel tepi atas, tinggi ±38 % frame**, tepi bawah lurus keras, tanpa border/bayangan/caption. **Pembicara TIDAK digeser turun** — panel menutupi dinding kosong, bukan mendorong pembicara (`full_sheetA.jpg` f230, f1270; `full_sheetB.jpg` f630). Bandingkan kit kita: `split` menurunkan pembicara 300 px dan panel slide dari atas.
- Satu pengecualian: teaser mosaik (3.53–4.80 s) berupa inset sedikit lebih kecil, mulai y≈9 %, margin kiri ≈ 3 % (`full/f125.jpg`).
- **Tanpa blur, tanpa dim, tanpa background desain.** Latar = ruangan asli (dinding abu gelap, lampu kayu hangat, frame foto B&W).
- **B&W (desaturasi penuh) pada pembicara** sebagai beat punchline/ironi: 9.83–10.50 (wanita "ngga…"), 16.73–17.90 (pria "ngga, gw ga pake" → "GW BOONG"), 87.50–90.10 (montase tertawa penutup). (`strips/s04_ngga_bw.jpg`, `strips/s06_bw_bars_17s.jpg`, `strips/s22_bw_ending.jpg`)
- **Color bar SMPTE + beep 1 kHz layar penuh** (2.47–2.83, 17.90–18.27): gag "disensor"/reset — dipakai saat nama segmen yang nyerempet ("BDSM") dan setelah lelucon "gw boong" untuk kembali ke topik. (`strips/s01_open_bdsm_bars.jpg`)
- **Kapan meninggalkan pembicara sepenuhnya**: hanya untuk gag sensor. Semua informasi ditampilkan sambil wajah tetap terlihat.

## C. SUBTITLE / ANIMASI TEKS
Dasar (`full_sheetB.jpg` f160, f890):
- Posisi: tengah horizontal; vertikal **di dada pembicara, tepat di atas tepi tablet**: ±54 % tinggi frame di close-up, ±65–68 % di wide shot. Posisi mengikuti komposisi tiap shot, bukan satu garis tetap.
- Ukuran: tinggi huruf ≈ 3.5–4 % frame (≈ 50–56 px pada 1080 lebar). Font sans grotesk tebal (bold/semibold), tracking rapat, huruf kecil semua kecuali penekanan; putih dengan bayangan tipis lembut, **tanpa box, tanpa stroke tebal**.
- Potongan: 1 klausa pendek per layar (1–5 kata; maksimal 2 baris ±7 kata). Ganti per frasa, **muncul sekaligus dalam 1 frame (hard cut), tanpa pop/scale/fade**, tanpa reveal per kata (dicek di `s07`, `s13`, `s05`, `s16`). Subtitle biasanya berganti tepat di cut kamera.
Penekanan (tiap jenis punya arti):
1. **Baris kedua kuning** = inti kalimat/punchline: "cewe mendekat", "gw pake AXE ini", "daripada Bleu de Chanel", "studi sosial"; kadang baris pertama kuning ("marketingnya"). Kutipan bahasa Inggris dikutip + **miring**: "smells better than Chanel" (`strips/s08_billboard_zoom.jpg`).
2. **Huruf kapital putih** = klaim/angka tegas: "73% COWOK", "MEREKA LEBIH SUKA AXE", "DIA LEBIH BAGUS", "IYA".
3. **Merah** = nama "terlarang"/kejutan: "NGGA" besar (8.63), "Chanel / ga marah?" (36 s), "BDSM PA".
4. **Kuning besar kapital + tanda kutip** = istilah kunci yang dikutip: "BLIND TEST" (66.4–67.07), "GW BOONG" (17.53).
5. **Mengetik huruf per huruf** saat diucapkan dieja: "B → BD → BDS → BDSM → BDSM P → BDSM PA" merah (79.2–80.2; juga di cold open 1.5–2.4) (`strips/s20_bdsm_typing.jpg`, `strips/s25_open_vs_end.jpg`), lalu kata raksasa putih satu per satu "BDSM" / "SAMA" / "PA" (80.27–82.1, ±2.5× ukuran normal).
6. **Subtitle miring (rotasi ±5–7°)** untuk kalimat main-main sang wanita: "emang iya?" (13.2), "jadi kayak penasaran" (−5° lalu +7° setelah punch-in, `strips/s18_tilted_sub.jpg`).
7. **Marquee bergerak** untuk seruan panjang: "WOOOOHHHH" dua baris (kecil + besar ber-motion-blur) meluncur horizontal ±17 px/frame (57.93–59.1, `strips/s15_wooh.jpg`).
8. **Teks menempel ke kepala orang** di wide shot: "eh?" besar di tengah lalu pindah ke atas kepala pria, kemudian "eh?" kedua lebih kecil di sampingnya (86.2–87.4, `strips/s21_eh.jpg`).
9. **Judul konsep serif** (lihat D) menggantikan subtitle (subtitle dihilangkan saat judul tampil).
Perbandingan dengan kit kita (`Main.tsx Subs`): kita = 1 baris putih kecil, reveal per kata (opacity 0.5→1), fade 4 frame, kata besar serif italic kuning. v3 = frasa muncul utuh tanpa animasi, warna dipakai sebagai **makna per baris** (kuning = inti, merah = kaget/tabu, kapital = angka/klaim), dan variasi bentuk (miring, mengetik, marquee, menempel kepala) hanya pada momen emosi. Ini lebih ekspresif tapi tetap satu font sans + satu font serif.

## D. JENIS VISUAL LAIN
| Jenis | Kapan | Asli/gambar? | Presentasi |
|---|---|---|---|
| Footage billboard 3D AXE Times Square (video asli, kaleng berputar) | 3.53 (mosaik), 6.60–8.63, 20.50–24.40, 75.23–77.00 | asli (footage) | panel atas full-bleed ±38 %, hard cut masuk; 22.47 panel saja cut ke close-up tulisan "NEW AXE SMELLS BETTER THAN CHANEL" saat kutipan diucapkan (`s08`) |
| Versi **mosaik/pixelated** billboard (teaser, merek disembunyikan) | 3.53–4.80 "marketingnya gila banget sih" | asli + efek | fade-in ±5 frame (`s24_mosaic_entry.jpg`); dibuka jelas di 6.60 tepat kata "AXE" (`s03_mosaic_to_clear.jpg`) |
| Ilustrasi Samsung vs Apple (planet bertabrakan) | 41.67–43.00 "ini kayak Apple sama Samsung" | gambar meme/ilustrasi yang sudah ada di internet | panel atas; fade + scale turun ±8 frame (`s23_samsung_entry.jpg`) |
| Foto iklan Coca-Cola vs Pepsi | 43.00–44.27 | iklan asli terkenal | hard cut di kata "Coca", geser pelan (`s13_samsung_coke.jpg`) |
| Paragraf artikel + stabilo biru | 28.07–32.00 | screenshot asli | lihat A |
| Video kapur rumus matematika | 26.67–32.0 | stock/meme overlay | screen-blend, fade ±10 frame, pan pelan; pada "bukti data-datanya" (`s09_chalk_math.jpg`) |
| Stiker animasi asap semprot (kartun) | 11.53–12.6 "semprot terus tiba-tiba" | stiker/animasi siap pakai | mengikuti tangan yang memperagakan semprotan (`s05_spray_smoke.jpg`) |
| Judul konsep serif besar putih + sub kapital sans kecil | 20.50 New York/TIME SQUARE; 39.87 Psikologi/PERBANDINGAN; 48.93 Upward/COMPARISON; 60.83 Social/Proof | teks | di headroom wide shot (y ±8–15 %), **muncul per kata tepat saat kata diucapkan** (hard on, tanpa animasi): "New"(f615)→"New York"(f622)→"TIME"(f634)→"TIME SQUARE"(f639) (`s07`, `s12`, `s14`, `s16`) |
| Color bars + beep | 2.47, 17.90 | bawaan | layar penuh 11 frame |
| B&W | 3× | grading | lihat B |
| Punch-in/zoom digital pada shot yang sama | ±10× (9.40, 12.47, 16.07, 36.4, 37.83, 41.03, 71.03, 72.5, 80.27…) | kamera | hard zoom cut di tengah kalimat untuk penekanan |
Tidak ada: logo terpisah, chart/angka gambar, peta, screen recording, bubble chat, kartu penutup/CTA, musik yang terdengar jelas (tidak bisa diverifikasi tanpa mendengar).

## E. RITME
Statistik: **79 hard cut / 90.1 s → rata-rata shot 1.14 s** (`hardcuts.txt`); multicam 3 angle (CU pria, CU wanita, wide two-shot) + punch-in. Cut mengikuti siapa bicara + reaksi pendengar.
Beat visual non-subtitle (event bermakna): ±31 → **1 beat per ±2.9 s**.
Pembagian waktu (perkiraan dari batas frame):
- Pembicara saja (dengan subtitle biasa/penekanan): ≈ 66 s (73 %)
- Pembicara + panel gambar atas: 15.5 s (17 %) [1.27 + 2.03 + 3.90 + 3.93 + 2.60 + 1.77]
- Pembicara + judul serif saja: ≈ 4.2 s (5 %); + overlay kapur/stiker ≈ 2.5 s
- Pembicara tersembunyi: 0.73 s (color bar) (0.8 %)
- B&W: 1.83 + 1.17 (sebagian) + 2.6 ≈ 5 s
Shot terpanjang tanpa cut: 4.1 s (53.80–57.93). Rentang terpanjang tanpa visual desain (hanya cut+subtitle): ≈ 7 s (50.93–57.93, tanya jawab "apa upward comparison?").
Hook 3 s pertama: **cold open** = potongan akhir video ("ini segmen namanya BDSM PA") diputar di depan, nama segmen diketik merah lalu **dipotong color bar + beep** pada 2.47 s → rasa penasaran + humor tabu. Lalu 3.53 s langsung teaser mosaik billboard ("ini brand menurut gw marketingnya gila banget sih").
Ending: pengungkapan nama segmen penuh (BDSM PA → "Bedah Bisnis Satu Jam… eh satu menit") → "eh? eh?" → montase B&W tertawa tanpa subtitle (2.6 s). Tidak ada CTA/logo.

### Tabel kalimat → visual
| waktu | diucapkan (word idx) | tampil | layout | durasi |
|---|---|---|---|---|
| 0.00–2.47 | "Ini segmen namanya BDSM PA" (cold open, footage dari 77.3–80.3) | CU pria/wanita; "BDSM PA" merah diketik | speaker | 2.47 |
| 2.47–2.83 | (beep) | SMPTE color bars | full | 0.37 |
| 2.83–3.53 | "ini brand menurut gw" (#4-7) | CU pria, subtitle biasa | speaker | 0.7 |
| 3.53–4.80 | "marketingnya gila banget sih" (#8-11) | billboard **dipixelate** di atas wide; "marketingnya" kuning | panel atas (inset) | 1.27 |
| 4.80–6.60 | "oh ya kenapa?" / "nih lu tau ga" | CU wanita / CU pria | speaker | 1.8 |
| 6.60–8.63 | "AXE?" "parfum AXE itu tau ga?" (#19-24) | billboard jelas (video), sub "AXE" | panel atas | 2.03 |
| 8.63–9.83 | "Nggak" / "ga tau parfum AXE?" | "NGGA" merah besar; CU pria + punch-in 9.40 | speaker | 1.2 |
| 9.83–10.50 | "nggak…" (#30) | wanita **B&W**, "ngga..." | speaker B&W | 0.67 |
| 10.50–13.20 | "yang ads-adsnya tuh semprot terus tiba-tiba cewek mendekat" | CU pria + **stiker asap** ikut tangan; punch-in 12.47; baris 2 kuning | speaker+stiker | 2.7 |
| 13.20–14.00 | "emang iya?" | CU wanita, subtitle **miring** | speaker | 0.8 |
| 14.00–16.73 | "iya" "lu deket gw karena gw pake AXE ini" "ga ada bau?" | CU cut-cut, "IYA" kapital, baris 2 kuning | speaker | 2.7 |
| 16.73–17.90 | "enggak, lu gak pake bau-bau" → "GW BOONG" | pria **B&W**, sub kuning; "GW BOONG" kuning kapital | speaker B&W | 1.17 |
| 17.90–18.27 | (beep) | color bars | full | 0.37 |
| 18.27–20.50 | "kemarin AXE itu pasang iklan gede-gede di" | CU wanita tertawa / CU pria | speaker | 2.2 |
| 20.50–22.47 | "New York Times Square" (#71-74) | billboard video atas + judul serif "New York / TIME SQUARE" per kata | panel atas + judul | 1.97 |
| 22.47–24.40 | "dia sampe bilang smells better than Chanel" (#75-81) | panel cut ke close-up tulisan billboard; kutipan miring kuning | panel atas | 1.93 |
| 24.40–26.67 | "pede banget" "makanya pede kan?" "iya" "dia bahkan" | CU cut-cut | speaker | 2.3 |
| 26.67–28.07 | "ngasih bukti data-datanya itu" (#90-94) | kapur rumus fade-in di belakang/atas pria | speaker+overlay | 1.4 |
| 28.07–32.00 | "73% cowok mereka lebih suka AXE daripada Bleu de Chanel" (#95-105) | **paragraf artikel + stabilo biru** di atas wide + kapur; sub kapital | panel atas (cut-out) | 3.93 |
| 32.00–35.73 | "Perfume Chanel?" "iya mahal kan?" "hooh" "dia berani bilang DIA LEBIH BAGUS" | CU cut-cut; kapital | speaker | 3.7 |
| 35.73–37.40 | "wow emang Chanel ga marah?" | CU wanita, "Chanel / ga marah?" merah; punch-in | speaker | 1.7 |
| 37.40–39.87 | "nah ini jeniusnya marketing mereka" "jadi ada 2 aspek" | CU pria / wide | speaker | 2.5 |
| 39.87–41.03 | "psikologi perbandingan" (#131-132) | judul serif "Psikologi / PERBANDINGAN" di headroom wide | wide + judul | 1.16 |
| 41.03–41.67 | "ini kayak Apple" | wide (reframe) | speaker | 0.6 |
| 41.67–43.00 | "…Apple sama Samsung" (#135-137) | ilustrasi Samsung vs Apple, fade+scale | panel atas | 1.33 |
| 43.00–44.27 | "Coca-Cola sama Pepsi gitu loh" (#138-143) | foto Coke vs Pepsi, hard cut di "Coca" | panel atas | 1.27 |
| 44.27–48.40 | "pas AXE nyindir Chanel malah sales dua-duanya naik" "wow menarik" | CU pria (gesture) / wide / CU wanita | speaker | 4.1 |
| 48.40–48.93 | "yang kedua" | wide | speaker | 0.5 |
| 48.93–50.93 | "upward comparison, itu nama iklannya" (#157-161) | judul serif "Upward / COMPARISON" per kata | wide + judul | 2.0 |
| 50.93–57.93 | "apa upward comparison?" "kamu tanya aku aku tanya siapa?" "karena AXE bandingin sama Chanel, orang jadi ngira AXE tuh levelnya Chanel" | CU/wide cut-cut, subtitle biasa | speaker | 7.0 |
| 57.93–59.67 | "wow" "iya kan?" "menarik" | **marquee "WOOOOHHHH"**, lalu "menarik" | speaker | 1.7 |
| 59.67–60.83 | "terus yang ke-3 apa?" | CU pria | speaker | 1.2 |
| 60.83–61.87 | "social proof" (#193-194) | judul serif "Social / Proof" (bertingkat) | wide + judul | 1.04 |
| 61.87–66.30 | "jadi dia nunjukin dia lebih enak baunya lewat studi sosial" | CU pria cut-cut, "studi sosial" kuning | speaker | 4.4 |
| 66.30–67.07 | "blind test" (#205-206) | "“BLIND TEST”" kuning kapital besar | speaker | 0.77 |
| 67.07–70.10 | "orang disuruh pilih, makanya kebanyakan orang pilih AXE" "menarik sih" | wide / CU wanita | speaker | 3.0 |
| 70.10–71.90 | "jadi kayak penasaran" | CU wanita, subtitle miring 2 arah + punch-in | speaker | 1.8 |
| 71.90–75.23 | "emang seenak?" "aaa iya kan" "emang seenak itu?" | CU cut-cut | speaker | 3.3 |
| 75.23–77.00 | "itu jeniusnya marketingnya" (#234-236) | billboard "THE NEW G.O.A.T." (callback) | panel atas | 1.77 |
| 77.00–80.27 | "menarik" "ini segmen namanya BDSM…" | CU, "BDSM PA" merah diketik | speaker | 3.3 |
| 80.27–82.13 | "BDSM sama PA" | kata raksasa putih BDSM/SAMA/PA | speaker | 1.9 |
| 82.13–85.47 | "Bedah Bisnis satu jam" "eh satu menit" | CU wanita/pria | speaker | 3.3 |
| 85.47–87.50 | "eh?" "eh?" | "eh?" raksasa; di wide "eh? eh?" menempel ke kepala | speaker | 2.0 |
| 87.50–90.10 | (tertawa) "bersambung" | montase **B&W** tanpa teks, cut 0.2–0.4 s | speaker B&W | 2.6 |

## F. CARA BERPIKIR EDITOR (prinsip yang bisa dipakai model lain)
1. **Wajah adalah kontennya; visual menumpang di ruang kosong.** Format dua orang/obrolan → reaksi adalah hiburannya, jadi gambar tidak pernah menutup wajah. Shot wide sengaja punya headroom gelap; gambar dan judul diletakkan di situ (±38 % atas). Prinsip: *cari ruang kosong di komposisi, taruh visual di sana; jangan pindahkan orang kalau tidak perlu.*
2. **Visual = bukti nyata dari hal yang disebut, persis di kata itu.** Billboard muncul di kata "AXE", Coca-Cola di kata "Coca", artikel di kata "73". Saat kutipan "smells better than Chanel" diucapkan, panel pindah ke close-up tulisan itu di billboard — visual menunjukkan *kalimat yang sama* dengan yang diucapkan.
3. **Teaser lalu reveal.** Merek disamarkan (mosaik) saat "brand ini marketingnya gila", baru dibuka saat namanya disebut → penonton menebak 3 detik.
4. **Kutipan sumber dipotong sesempit mungkin**: hanya paragraf yang memuat angka, stabilo hanya di klaim, tanpa bingkai. Tujuannya "ini ada sumbernya", bukan "baca ini". Subtitle merangkum angkanya dalam bahasa penonton ("73% COWOK").
5. **Konsep abstrak = judul serif, bukan gambar.** "Psikologi perbandingan", "upward comparison", "social proof" tidak punya foto yang jujur → cukup tipografi besar yang berbeda karakter (serif) dari subtitle (sans), muncul per kata mengikuti ucapan. Ini juga menandai struktur "aspek 1/2/3".
6. **Perbandingan = dua merek yang sudah dikenal penonton** (Apple–Samsung, Coke–Pepsi): gambar yang sekali lihat langsung paham, durasi ±1.3 s masing-masing (secepat penyebutan).
7. **Penekanan subtitle = intonasi.** Warna dan bentuk dipilih dari emosi kalimat: kuning = inti, merah = tabu/kaget, kapital = angka/klaim, miring = nada bercanda, mengetik = mengeja, marquee = seruan panjang. Di luar momen itu subtitle polos dan diam.
8. **Komedi dengan "grammar TV"**: color bar + beep = sensor; B&W = momen deadpan/ironi; punch-in = tekanan. Semuanya generik dan murah, tapi tepat di punchline.
9. **Callback/bookend**: cold open memakai potongan akhir; billboard dipakai lagi di "itu jeniusnya marketingnya"; penutup B&W tertawa = akhir yang "selesai" tanpa CTA.
10. **Tempo**: cut tiap ±1.1 s karena dialog dua orang; beat visual tiap ±3 s; tidak ada visual yang lebih lama dari 4 s.

## G. KLASIFIKASI vs KIT (edit-json.md + bench01/video/src/Visuals.tsx, Main.tsx)
| Teknik v3 | Status | Catatan |
|---|---|---|
| Cut-cut multicam, punch-in | **Bisa sekarang** | `segments` + `shots`/framing zoom |
| Panel gambar/video atas (billboard, Samsung, Coke) | **Perlu perubahan parameter kecil** | `split` ada, tapi selalu mendorong pembicara turun (`shift` default 300, boxShadow, spring slide). Perlu `shift: 0` diizinkan + mode masuk `cut`/`fade` (bukan slide) + `shadow: false`. `shift:0` sudah bisa diisi; masuk cut/fade dan tanpa bayangan butuh 2 prop kecil |
| Paragraf artikel cut-out + stabilo, tanpa bingkai, di atas pembicara | **Primitive generik baru: `cutout`** | lihat spesifikasi 1 di bawah. `screenshot` sekarang = kartu layar penuh rounded+shadow+blur bg+label SUMBER, menutup pembicara |
| Judul konsep serif per kata | **Primitive generik baru: `kicker`** (spesifikasi 2). `title` yang ada = 2 baris dengan stabilo kuning, spring, hanya pembuka |
| Subtitle per frasa tanpa animasi, warna per baris (kuning/merah/kapital) | **Perubahan parameter** pada `Subs`: mode `reveal: "phrase"`, warna per kata via `text`/`script` (mis. `^kata` = aksen 2, `!kata` = merah), kapital per chunk. Kata besar sudah ada (`*kata`) tapi serif italic; perlu opsi `big_font: SANS` |
| Subtitle miring (rotasi) | **Parameter kecil**: `tilt` per chunk di `script` |
| Huruf diketik per huruf | **Primitive generik baru: `typeon`** (spesifikasi 3) |
| Marquee teks bergerak | **Primitive generik baru: `marquee`** (spesifikasi 4) |
| Teks menempel ke kepala (eh? eh?) | **Bisa dengan `kicker` + posisi x/y** (spesifikasi 2, field `x`,`y`) |
| B&W pembicara | **Primitive generik baru (kecil): `grade`** (spesifikasi 5) |
| Color bar + beep sensor | **Bisa hampir sekarang**: `photo` dengan gambar color bar asli + sfx 1 kHz (tambah `beep.wav` ke `make_sfx.sh`); `photo` sekarang zoom 1.1→1.22 + gradient + Grain + fade 7 frame → perlu `static: true` (tanpa zoom/fade/grain) |
| Overlay video kapur screen-blend | **Primitive generik baru: `layer`** (spesifikasi 6) — memakai aset video asli |
| Stiker asap animasi | `layer` dengan webm alpha (aset asli) + posisi; tracking tangan manual (x,y keyframe) |
| Mosaik/pixelate untuk teaser | **Parameter kecil** pada panel: `pixelate: n` (render gambar kecil lalu `imageRendering: pixelated`) |
| Montase penutup B&W tanpa subtitle | `grade` + `text` kosong; tidak ada `outro` kartu |

Spesifikasi primitive generik baru (semua menampilkan aset asli atau menganimasikan teks):
1. **`cutout`** — `{type:"cutout", start, end, img, crop:{x,y,w,h} (px gambar), y: 0.27 (posisi atas, fraksi tinggi), width: 0.91, highlights:[{x,y,w,h, color?:"#4A90E2"|"accent", at?: anchor}], enter:"fade"|"cut", shadow:false}`. Gerak: opacity 0→1 dalam 8 frame (atau langsung), tanpa translate/rotasi; highlight statis (bila `at` diberi: lebar 0→1 dalam 10 frame dari kiri ke kanan, sesuai urutan baris). Keluar: cut atau fade 6 frame. Pembicara tidak digeser; subtitle tetap.
2. **`kicker`** — `{type:"kicker", start, end, words:[{text:"Social", at:anchor, style:"serif"}, {text:"Proof", at:anchor, style:"serif", dx: 0.12}, {text:"COMPARISON", at:anchor, style:"caps-small"}], x:0.5, y:0.1, hide_subs:true}`. Tiap kata muncul hard-on (atau opacity 2 frame) tepat pada jangkar katanya; baris kedua boleh di-indent (`dx`) atau label kapital kecil rata kanan di bawah baris 1. Ukuran serif ±150 px/1080, caps ±40 px. Dipakai juga untuk teks yang ditempel ke posisi orang (x,y bebas, ukuran bebas).
3. **`typeon`** — `{type:"typeon", text:"BDSM PA", start, end, at_chars:[anchor…] | cps, color, size, y}`: menampilkan prefix string; satu karakter per jangkar/kecepatan; tanpa kursor; menggantikan subtitle.
4. **`marquee`** — `{type:"marquee", text, start, end, rows:[{size, y, speed_px_per_frame, dir}], blur:true}`: teks berulang meluncur horizontal; motion blur = `filter: blur` sumbu x atau 2–3 salinan semi-transparan.
5. **`grade`** — `{type:"grade", start, end, mode:"bw"|"dim", amount:1}`: filter pada layer pembicara saja (`grayscale(1)` / `brightness`), cut tanpa transisi; overlay & subtitle tidak terpengaruh.
6. **`layer`** — `{type:"layer", start, end, src (video/webm/png), blend:"screen"|"normal", region:{y,h}|full, opacity, fade:10, from, keyframes:[{at, x, y, scale}]}`: menaruh aset video/gambar asli di atas pembicara (di bawah subtitle) dengan blend mode; dipakai untuk tekstur, stiker animasi, efek.

## H. Yang TIDAK bisa saya pastikan
- Audio selain nada 1 kHz: ada/tidaknya musik latar, whoosh/pop di cut, SFX semprot — tidak bisa didengar (hanya beep yang terbukti dari spektrum).
- Nama font persis (sans grotesk tebal mirip Inter/SF Display; serif mirip Times/Didone tipis) — hanya karakter.
- Sumber asli gambar Samsung–Apple, Coke–Pepsi, video kapur, stiker asap, dan halaman artikel (paragraf menyebut The Martin Agency; situs tidak terlihat). Lisensi tidak diketahui.
- Apakah panel atas menimpa wide shot yang sudah di-reframe (kepala diturunkan) atau wide shot memang direkam begitu — dari frame tampak headroom sudah ada di footage (f1200 tanpa panel), tapi reframe kecil tidak bisa dikesampingkan.
- Opacity kotak artikel (terlihat opak; kapur menimpanya) dan apakah kotak sedikit diperbesar saat masuk.
- Hitungan durasi per jenis subtitle bersifat perkiraan dari 1-fps + strip, bukan pengukuran per frame lengkap.
