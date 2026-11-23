# Benchmark v1 — @raymondchins 7628165590825422098 ("90% pengguna AI masih pakai AI sebagai tool", 58,6 s)

File: `work/ref/v1.mp4` (720x1280, 30 fps, 58,58 s). Transkrip: `work/ref/v1_transcript.txt`, `work/ref/v1_words.json` (large-v3).
Bukti gambar (semua sudah dibuka):
- Contact sheet 1 fps: `work/ref/sheets/v1_sheet_0.jpg` (0–43 s), `work/ref/sheets/v1_sheet_1.jpg` (44–58 s)
- Strip rapat (label = detik + frame): `work/ref/strips/v1_00_open.jpg`, `v1_03_logos.jpg`, `v1_08_chat_ui.jpg`, `v1_29_card_icons.jpg`,
  `v1_38_timer.jpg`, `v1_51_diagram.jpg`, `v1_54_ending.jpg`; `work/ref/v1/v1_02_logo_in_everyframe.jpg` (tiap frame),
  `v1_05_cut_bigsub.jpg`, `v1_11_bigsub_ui1.jpg`, `v1_15_ui_pan.jpg`, `v1_21_ui3_ui4.jpg`, `v1_25_ui4_flash.jpg`,
  `v1_29_lightleak_everyframe.jpg` (tiap frame), `v1_31_ai_icon_in.jpg` (tiap frame), `v1_35_skills.jpg`, `v1_44_pct_broll.jpg`
- Frame resolusi penuh: `work/ref/frames/v1_t005_headline.jpg`, `v1_t045_logos.jpg`, `v1_t065_bigsub.jpg`, `v1_t165_chatui.jpg`,
  `v1_t310_chatcard.jpg`, `v1_t345_aiicons.jpg`, `v1_t535_diagram.jpg`

Format video: satu pembicara, kamera tetap, latar ruangan gelap hangat, kaos hitam. Tidak ada CTA/handle/logo di akhir.
Video ini adalah tipe "tutorial/opini AI" — beritanya hanya satu (pembuka); sisanya demonstrasi UI, ikon, diagram, b-roll, dan teks kinetik.

---

## A. Potongan berita / halaman asli

### A1. Headline berita (satu-satunya berita di v1) — 0,00–4,80 s
Bukti: `frames/v1_t005_headline.jpg`, `frames/v1_t045_logos.jpg`, `strips/v1_00_open.jpg`, `v1/v1_02_logo_in_everyframe.jpg`.
- **Apa yang tampil:** kartu "lower-third headline" — strip hitam tipis berisi logo + nama media ("BT Bloomberg Technoz"),
  di bawahnya kotak putih berisi **judul saja** (2 baris, sans tebal rapat: "Lebih dari 90% Pekerja di Indonesia telah Gunakan AI"),
  plus satu baris abu kecil "tapi penggunaannya hanya sekedar sebagai tools aja". Tidak ada foto artikel, paragraf, tanggal, atau URL.
- **Baris abu itu adalah parafrase kalimat ke-2 pembicara** ("itu masih menggunakan AI sebagai tool"), bukan (dapat dipastikan) subjudul
  asli Bloomberg → kartu = judul asli + "poin video" dalam satu blok. Apakah judulnya diketik ulang atau dipotong dari screenshot:
  **tidak bisa dipastikan**; tipografinya sangat bersih dan satu keluarga dengan subtitle, jadi kemungkinan besar diketik ulang di template
  dengan logo media asli.
- **Bingkai:** tidak ada bingkai perangkat/browser, tidak ada sudut membulat, tidak ada bayangan, tidak miring. Persegi panjang datar.
- **Ukuran/posisi:** lebar ±88% layar (x 48–683 dari 720), y ±62–75% — tepat di bawah dagu, di atas dada; wajah tetap utuh.
- **Hiasan:** stiker ikon app ChatGPT menempel di sudut kanan atas kartu; "asterisk"/starburst oranye kecil menempel di sudut kiri bawah
  (setengah keluar kartu). Starburst besar oranye kedua muncul di kanan wajah ±2,5 s dan **berputar pelan** (`strips/v1_03_logos.jpg`).
- **Stabilo/garis bawah:** tidak ada di v1.
- **Masuk:** sudah ada di frame 0 (tidak ada layar kosong). Frame 0–12: kartu sedikit lebih besar + blur → mengecil sedikit dan tajam
  (±0,4 s, "blur-in + settle"). Wajah di frame awal juga sedikit lembut lalu tajam.
- **Keluar:** 4,80–4,87 s **flash putih** (frame terbakar putih + blur) langsung ke shot berikutnya; kartu tidak animasi keluar sendiri.
- **Jangkar ucapan:** seluruh kalimat 1 + 2 ("90% lebih … sebagai tool", 0,00–4,72). Kartu tinggal ±4,8 s = selama klaimnya diucapkan.
- **Satu kartu saja** di layar.

### A2. Halaman/UI asli sebagai "potongan" — ChatGPT (8,27–11,1 s dan 13,8–29,6 s)
Bukti: `strips/v1_08_chat_ui.jpg`, `frames/v1_t165_chatui.jpg`, `v1/v1_11_bigsub_ui1.jpg`, `v1/v1_15_ui_pan.jpg`,
`v1/v1_21_ui3_ui4.jpg`, `v1/v1_25_ui4_flash.jpg`.
- **Apa:** UI ChatGPT asli (teks UI asli: "Ready when you are.", "What are you working on?", "Create image", "Write or edit",
  "Look something up", tombol +, mic, kirim). Isi prompt = teks pembicara (Indonesia). Tampaknya screenshot/rekaman layar asli —
  tidak bisa dipastikan apakah screen recording atau screenshot yang dianimasikan.
- **Tanpa bingkai:** tidak ada browser bar, tab, perangkat, atau kartu. Latar putih halaman **menyatu** dengan pusat putih latar
  vinyet (lihat B), jadi UI tampak melayang tanpa tepi. Hanya bagian composer (kotak input + judul) yang dipotong.
- **Fokus per bagian:** prompt panjang dibagi 4 bagian. Bagian yang sedang diucapkan **tajam dan hitam**, bagian lain **pudar (opacity
  rendah) + blur**; penanda bulat merah bernomor (1, 2, 3, 4) pop di atas bagian itu; penanda sebelumnya memudar jadi merah muda.
  "Kamera" **pan + zoom** ke bagian aktif: 16,0–16,8 s geser ke kanan ke bagian 2 (±24 frame, terasa ease-in-out), lalu zoom keluar
  sedikit 17–19 s. Ukuran teks aktif besar (zoom ±2–3x dari UI asli; `frames/v1_t165_chatui.jpg`), sisi kanan teks keluar frame.
- **Kontinuitas:** UI yang sama kembali 3 kali (13,8 / 20,4 / 26,5 s) dengan status bertambah (1 → 1–2 → 3 → 4), diselingi wajah +
  teks besar "nah yang ke 3 / objektif", "nah yang ke empat". Insert = "papan tulis" yang terus diisi.
- **Masuk:** blur → tajam ±6–8 frame (13,80→14,07), kadang hard cut dari wajah. **Keluar:** hard cut ke wajah (blur) atau light-leak.
- **Jangkar:** penanda "1" saat "lu adalah expert" (13,60), "2" saat "kedua" (15,64; pan 16,0), "3" saat "ketiga…tujuannya" (20,30),
  "4" saat "kalau misalnya ada" (26,30). Sangat rapat ke kata.
- **Rekap overlay 29,75–31,6 s:** composer ChatGPT asli yang berisi prompt lengkap (kartu putih bersudut bulat — sudutnya milik UI
  asli, bukan dekorasi) muncul sebagai overlay di bawah subtitle, di atas dada pembicara ("ini secara basic bisa dibilang namanya
  'pull prompting'"). `frames/v1_t310_chatcard.jpg`, `v1/v1_29_lightleak_everyframe.jpg`.

### A3. Yang TIDAK ada di v1
Tidak ada artikel paragraf, tidak ada stabilo di teks, tidak ada label "SUMBER", tidak ada tanggal. (Itu ada di v2, bukan di sini — jangan
jadikan aturan dari v1.)

---

## B. Apa yang ada di belakang potongan

- **Headline (A1):** pembicara tetap terlihat penuh, tidak di-dim, tidak di-blur, tidak digeser. Hanya ikon logo + starburst ditambahkan
  di sekitar kepala. (`frames/v1_t045_logos.jpg`)
- **UI, ikon, timeline, diagram (A2, D):** latar yang SAMA untuk semua insert "penjelasan": **radial gradient** putih di tengah →
  abu gelap/hitam di tepi (vinyet sangat kuat, seperti lampu sorot di kertas putih). Statis; geraknya datang dari konten (pan/zoom/blur).
  Tidak ada grid, tekstur, atau bentuk bergerak. Bukti: `frames/v1_t165_chatui.jpg`, `v1_t345_aiicons.jpg`, `v1_t535_diagram.jpg`.
  → Satu "panggung" netral menyatukan UI asli, ikon dan diagram sehingga semuanya terlihat satu sistem.
- **B-roll:** layar penuh (footage/gambar CGI gelap biru: deretan monitor server, robot, ledakan neural, humanoid). Tidak ada latar desain.
  (`v1/v1_44_pct_broll.jpg`, `strips/v1_38_timer.jpg`)
- **Momen teks besar:** sering di atas **close-up ekstrem pembicara yang di-blur** (11,2–12,1 "padahal yang seharusnya", 19,4–20,3
  "nah yang ke 3 objektif"): mulut/dada memenuhi layar, gambar lembut → wajah menjadi latar tekstur gelap, teks yang jadi subjek
  (`v1/v1_11_bigsub_ui1.jpg`, `v1/v1_15_ui_pan.jpg`). Di 4,87–5,1 dan 43,1–43,5 shot masuk dalam keadaan blur lalu fokus.
- **Kapan meninggalkan pembicara:** saat ia mendemonstrasikan sesuatu yang bisa DILIHAT (prompt di ChatGPT; daftar aplikasi; cara kerja
  timer jam 9/jam 12; metafora "bukan menggantikan"; output 10 → 100). **Kapan tetap di pembicara:** klaim pembuka (dengan kartu),
  penghubung/penomoran ("padahal yang seharusnya", "nah yang ke-3"), angka punchline (0,1%), opini dan emosi penutup.
- Pembicara tersembunyi ±30 s dari 58,6 s (±52%) — lihat E.

---

## C. Subtitle / animasi teks

v1 memakai **dua sistem teks yang berganti menurut tata letak** (bukan satu gaya sepanjang video):

### C1. Caption kecil berkotak — dipakai di atas SEMUA insert dan overlay
Bukti: `frames/v1_t005_headline.jpg`, `v1_t165_chatui.jpg`, `v1_t345_aiicons.jpg`, `strips/v1_29_card_icons.jpg`.
- Sans grotesk berat normal (regular/medium), **huruf kecil** seperti ucapan, warna putih, di dalam **kotak hitam pekat persegi** (tanpa
  sudut bulat, padding rapat), tanpa bayangan.
- Ukuran ±5% lebar layar per huruf kapital (±36 px di 720 ≈ ±54 px di 1080). Posisi tengah, y ±73–80%.
- 2–4 kata per potong (frasa alami: "90% lebih" / "dari orang" / "yang menggunakan AI" / "di Indonesia").
- Ganti **per frasa, langsung (hard swap)**; tidak ada sorot per kata, tidak ada pop. Muncul tepat saat frasa diucapkan.
- Di diagram 51,8–54,1 caption **hilang**: teks serif di dalam diagram menggantikannya (`strips/v1_51_diagram.jpg`).

### C2. Teks kinetik besar — dipakai hampir di SETIAP momen pembicara-saja
Bukti: `frames/v1_t065_bigsub.jpg`, `v1/v1_05_cut_bigsub.jpg`, `v1/v1_11_bigsub_ui1.jpg`, `v1/v1_35_skills.jpg`,
`v1/v1_44_pct_broll.jpg`, `strips/v1_54_ending.jpg`.
- **Posisi:** tengah-bawah di atas dada, y ±55–75%; rata tengah atau sedikit kiri; tidak pernah menutup mata/mulut.
- **Hierarki 2–3 baris, 2 jenis huruf:**
  - kata penghubung kecil di atas: serif regular putih ("kalau kalian", "kalian", "ini", "yang") atau sans kecil kuning ("coba jujur", "dan");
  - kata kunci SANGAT besar: sans hitam-tebal (heavy), rapat, ±55–80% lebar layar ("pakai AI", "role-nya", "skills itu", "0,1%",
    "mengkalikan", "bakal jadi");
  - baris penutup: serif (kadang miring) diketik ("mereka apa", "dipasang", "dari semua user yang ada", "masa depan").
- **Warna:** putih + **satu aksen kuning-lemon** untuk konsep inti ("pakai AI", "role-nya", "skills", "0,1%", "seharusnya", "objektif").
  **Merah** sekali untuk emosi ("menyeramkan banget", 56,2–57 s) → warna dipilih menurut makna kata, bukan acak.
- **Cara muncul (dihitung frame):**
  - kata sans: **blur + fade masuk per kata** ±4–6 frame tepat saat kata diucapkan ("kasih tau" blur di 12,33 → tajam 12,47; "sama diri"
    5,13 blur → 5,40 tajam). Kadang naik sedikit dari bawah (43,1–43,5).
  - baris serif: **mesin ketik per huruf** mengikuti tempo bicara ("m" → "merek" → "mereka ap" → "mereka apa", 13,13–13,53;
    "s" → "se" → "seru" 55,63–56,13).
  - angka: diketik per karakter seiring ucapan ("0" 44,6 → "0," → "0,1" → "0,1%" 45,2).
  - baris dua-warna menengah (putih + kuning, ±45 px di 720) juga diketik per huruf ("di satu komputer / yang nyala 24 jam", 37,1–38,3).
  - frasa tetap di layar sampai frasa berikut, lalu diganti (tidak ada animasi keluar yang terlihat; kadang memudar 2–3 frame).
- Tanpa kotak. Bayangan lembut (glow gelap tipis). Tanpa outline.
- Huruf kecil di semua baris (kecuali "AI", angka).

### C3. Beda dengan kit kita (`video/src/Main.tsx` `Subs`)
| | Kit | v1 |
|---|---|---|
| Sistem | satu: baris kecil + kadang kata besar serif miring kuning | dua sistem yang berganti menurut tata letak |
| Baris kecil | putih + bayangan, tanpa kotak, sorot opacity per kata | putih dalam kotak hitam pekat, ganti per frasa, tanpa sorot per kata |
| Teks besar | sesekali (kata `*`), 1 kata, pop skala pegas | default di setiap shot pembicara; 2–3 baris, 3 ukuran, 2 jenis huruf |
| Animasi | pop skala 0,7→1 | blur-in per kata (4–6 f) + mesin ketik per huruf untuk serif/angka |
| Warna | putih + ACCENT | putih + 1 aksen, + warna makna (merah untuk "menyeramkan") |
| Posisi | y 1270–1530 (sepertiga bawah) | caption y ±73–80%; teks besar y ±55–75% (di dada, lebih tinggi) |

---

## D. Jenis visual lain

| Jenis | Kapan (detik, ucapan) | Asli atau gambar sendiri | Penyajian | Bukti |
|---|---|---|---|---|
| Logo app asli (ChatGPT ikon, wordmark Gemini) | 2,0–4,8 "yang menggunakan AI" | asli | melayang kiri-atas & kanan-atas kepala, fade+naik ±12 f, di atas pembicara | `v1/v1_02_logo_in_everyframe.jpg` |
| Stiker dekoratif (starburst oranye) | 0–4,8 | gambar sendiri (bentuk sederhana) | 2 buah, satu berputar pelan; aksen hangat di pembuka saja | `frames/v1_t045_logos.jpg` |
| UI ChatGPT asli | 8,3–11,1; 13,8–29,6 | asli | tanpa bingkai, zoom/pan ke bagian aktif, fokus-pudar, penanda nomor | lihat A2 |
| Ikon "AI chip" (outline hitam) + logo asli Google Sheets, Drive, Meta, ikon akuntansi | 31,6–36,1 "AI dikasih akses ke Google Sheets, Google Drive, Meta Ads, accounting software" | ikon pusat = ikon stok outline; logo = asli; ikon akuntansi = ikon flat stok | ikon pusat fade+blur-in ±12 f (31,7–32,1); tiap logo muncul **tepat saat disebut** (33,1 / 33,9 / 34,3 / 35,1), fade+skala, menyebar di sekitar pusat; ring hijau samar di belakang ikon | `v1/v1_31_ai_icon_in.jpg`, `strips/v1_29_card_icons.jpg`, `frames/v1_t345_aiicons.jpg` |
| B-roll/CGI layar penuh: monitor server biru gelap | 38,9–41,0 "dibikin timernya… cron atau heartbeat" | stok/CGI (sumber tidak dapat dipastikan) | dengan teks besar "dibikin / timernya" + serif diketik | `strips/v1_38_timer.jpg` |
| Diagram timeline jam (09:00 → 12:00) dengan ikon flat (robot, clipboard, logo Google Ads asli) | 41,1–43,0 "jam 9 ngelakuin apa, jam 12 ngelakuin apa" | ikon stok + gambar sendiri (bingkai, garis, angka serif) | latar vinyet putih; pan horizontal dengan motion blur dari 09:00 ke 12:00 tepat di "jam 12" | `strips/v1_38_timer.jpg` |
| B-roll CGI robot / ledakan neural biru / humanoid | 47,0–50,5 "harus ngelihat AI… bukan menggantikan kerjaan-kerjaan kalian" | stok/CGI | 3 klip ±1,1 s, cross-dissolve, caption kecil berkotak | `v1/v1_44_pct_broll.jpg` |
| Diagram sebelum/sesudah: piktogram orang + batang; orang+chip AI + batang tinggi; panah melengkung | 51,8–54,1 "output kalian itu 10 → dengan AI bisa jadi 100" | gambar sendiri, monokrom (piktogram hitam, teks serif) | teks diketik, batang tumbuh, pan kanan dengan motion blur, panah tergambar; caption disembunyikan | `strips/v1_51_diagram.jpg`, `frames/v1_t535_diagram.jpg` |
| Framing pembicara | sepanjang video | — | 2–3 framing: medium, sedikit lebih dekat, close-up ekstrem blur untuk teks besar; tiap kembali ke wajah = framing berbeda + blur→fokus | `v1/v1_05_cut_bigsub.jpg`, `v1/v1_11_bigsub_ui1.jpg` |
| Transisi | 4,8 flash putih; 29,5–29,75 dan 54,0–54,3 light-leak/film-burn (palang putih bertepi oranye menyapu vertikal ±8–10 f); lainnya hard cut + blur→fokus, dissolve antar b-roll | efek | | `v1/v1_29_lightleak_everyframe.jpg`, `strips/v1_54_ending.jpg` |

Diagram buatan sendiri di v1 **sangat minimal**: hitam di atas putih, piktogram generik, teks serif, tanpa warna, tanpa kartu/kotak UI palsu.
Semua yang punya wujud asli (ChatGPT, Gemini, Google, Meta) memakai aset asli.

Suara/SFX: **tidak bisa didengar**. Flash dan light-leak kemungkinan disertai whoosh/hit, tetapi tidak terverifikasi.

---

## E. Ritme — kalimat → visual

| Waktu (s) | Ucapan | Yang tampil | Tata letak | Durasi |
|---|---|---|---|---|
| 0,00–3,04 | "90% lebih dari orang yang menggunakan AI di Indonesia" | kartu headline Bloomberg Technoz (sudah ada di frame 0); 2,0 logo ChatGPT + Gemini; 2,5 starburst | pembicara + overlay | 4,8 s (kartu) |
| 3,04–4,72 | "itu masih menggunakan AI sebagai tool" | kartu tetap (baris abu = kalimat ini); flash putih 4,80 | pembicara + overlay | ↑ |
| 4,72–5,72 | "coba jujur sama diri sendiri" | shot baru blur→fokus; teks besar "coba jujur / sama diri / sendiri" | pembicara + teks besar | 1,0 |
| 5,72–6,52 | "kalau kalian pakai AI" | "kalau kalian / **pakai AI**" | pembicara + teks besar | 0,8 |
| 6,52–8,12 | "kalian nanyanya pasti sesimpel kayak gini" | 2 baris menengah putih/kuning | pembicara + teks | 1,6 |
| 8,12–11,06 | "tolong cariin list kompetitor untuk bisnis A di area B" | UI ChatGPT "Ready when you are." + prompt pendek | layar penuh (vinyet putih) | 2,9 |
| 11,06–12,02 | "padahal yang seharusnya" | close-up ekstrem blur + teks besar | pembicara (blur) + teks | 0,9 |
| 12,02–13,60 | "kalian kasih tau dulu role-nya mereka apa" | medium; "kalian / kasih tau / dulu" → "**role-nya** / mereka apa" (ketik) | pembicara + teks | 1,6 |
| 13,60–19,20 | "lu adalah expert market researcher… itu minimal satu. Kedua, gue adalah business development…" | UI ChatGPT prompt panjang; penanda 1 → pan ke 2 | layar penuh | 5,5 |
| 19,20–20,30 | "nah yang ketiga, objektif" | close-up blur + "nah yang ke 3 / **objektif**" | pembicara (blur) + teks | 0,9 |
| 20,30–24,68 | "tujuannya market research ini… untuk pengembangan produk" | UI yang sama, penanda 3 | layar penuh | 4,4 |
| 24,68–26,30 | "nah yang keempat, yang jarang orang prompt" | medium; "nah yang / **ke empat**" → "yang jarang / orang prompt" | pembicara + teks | 1,6 |
| 26,30–29,54 | "kalau misalnya ada yang kurang clear… tolong tanya balik ke gue" | UI, penanda 4; light-leak keluar | layar penuh | 3,1 |
| 29,54–31,62 | "ini secara basic bisa dibilang namanya pull prompting" | pembicara + kartu composer berisi prompt lengkap (rekap) | pembicara + overlay | 1,9 |
| 31,62–35,94 | "di saat AI dikasih akses ke Google Sheets, Google Drive, Meta Ads, accounting software kalian" | ikon AI pusat; logo muncul satu per satu saat disebut | layar penuh (vinyet putih) | 4,5 |
| 35,94–38,62 | "dan skills itu dipasang di satu komputer yang nyala 24 jam" | medium; "dan / **skills itu** / dipasang" → "di satu komputer / yang nyala 24 jam" (ketik) | pembicara + teks | 2,5 |
| 38,62–40,82 | "dibikin timernya atau namanya cron atau heartbeat" | CGI monitor server + "dibikin / timernya" + serif diketik | layar penuh (b-roll + teks) | 2,1 |
| 40,82–42,94 | "jam 9 ngelakuin apa, jam 12 ngelakuin apa" | timeline 09:00 → pan → 12:00 | layar penuh (vinyet) | 1,9 |
| 42,94–46,74 | "dan di titik itu baru kalian 0,1% dari semua user yang ada" | blur→fokus; "nah di titik itu / baru kalian" → "**0,1%**" diketik + "dari semua user yang ada" | pembicara + teks | 3,8 |
| 46,74–50,34 | "jadi kalian harus melihat AI fungsinya itu bukan menggantikan kerjaan-kerjaan kalian" | CGI robot → neural → humanoid (dissolve) | layar penuh (b-roll) | 3,5 |
| 50,34–51,66 | "tapi mengkalikan yang sebelumnya" | "tapi / **mengkalikan**" → "yang / sebelum / nih" | pembicara + teks | 1,2 |
| 51,66–53,90 | "output kalian itu 10, dengan AI bisa jadi 100" | diagram orang+batang → orang+AI+batang tinggi; light-leak keluar | layar penuh (vinyet) | 2,3 |
| 53,90–56,18 | "gue ngerasa ini bakal jadi masa depan yang seru" | "gw / ngerasa" → "ini / bakal jadi / masa depan" → "yang / seru" (ketik) | pembicara + teks | 2,3 |
| 56,18–57,04 | "tapi menyeramkan banget" | "tapi / **menyeramkan / banget**" MERAH | pembicara + teks | 0,9 |
| 57,04–58,58 | "buat yang nggak ngerti dan bakal ketinggalan" | 2 baris menengah putih/kuning; selesai di wajah | pembicara + teks | 1,5 |

### Angka
- **Beat visual:** ±30 perubahan visual dalam 58,6 s (kartu, 2 logo, starburst, flash, 4 masuk UI, 3 penanda/pan, 2 close-up blur,
  rekap, ikon pusat + 4 logo, 2 b-roll set + 3 klip, timeline + pan, diagram + pan, transisi light-leak, 1 kata merah) → **±1 per 2 s**.
  Pergantian tata letak besar (wajah ↔ layar penuh ↔ overlay): ±20 → 1 per ±3 s.
- **Porsi waktu (perkiraan dari tabel):** pembicara tersembunyi (layar penuh) ±30 s = **±52%**; pembicara + overlay grafis ±6,7 s = ±11%;
  pembicara + teks kinetik besar ±22 s = ±37%; **pembicara dengan subtitle kecil saja ≈ 0 s** (hampir tidak ada).
- **Rentang terpanjang tanpa perubahan:** tidak ada > ±2,5 s tanpa sesuatu berubah. Insert terpanjang (UI 13,8–19,3 = 5,5 s) berisi
  penanda + pan 16,0. Shot wajah terpanjang 54,3–58,6 (4,3 s) berganti teks besar tiap ±1 s.
- **Hook 3 s pertama:** frame 0 sudah berisi kartu headline berita dengan klaim angka (90%) + logo media; di 2,0 s logo ChatGPT/Gemini
  masuk. Tidak ada judul buatan sendiri — **headline berita pihak ketiga = judul video**.
- **Penutup:** tidak ada CTA, logo, handle, atau kartu akhir. Ditutup emosi + peringatan dengan teks besar (kata merah) di wajah.
  (Ini pilihan video ini; jangan dijadikan aturan.)

---

## F. Pemikiran di balik keputusan

1. **Berita = bukti klaim di detik pertama, bukan dekorasi.** Kalimat pertama adalah statistik yang mengejutkan → editor membuka
   dengan judul berita asli bermerek media (kredibilitas) dan menyisipkan "poin saya" di baris abu bawahnya. Penonton membaca klaim +
   sumber dalam satu pandangan tanpa kehilangan wajah. Lower-third (bukan layar penuh) karena kontak mata di hook lebih penting.
2. **Halaman asli dipotong sampai tinggal yang dibicarakan.** UI ChatGPT tidak ditampilkan sebagai "screenshot di dalam kartu";
   bingkai dan latar halaman dibuang, latar putihnya dilebur ke panggung vinyet. Yang tersisa hanya kalimat yang sedang diucapkan,
   diperbesar sampai terbaca di HP, bagian lain dipudarkan. Prinsip: **zoom ke kalimatnya, bukan ke halamannya.**
3. **Daftar bernomor → satu kanvas yang terisi bertahap + kembali ke wajah di setiap nomor.** Penomoran ("nah yang ke-3") diucapkan
   di wajah dengan teks besar (jeda/tanda bab), isinya ditunjukkan di UI. Ritme wajah–UI–wajah–UI membuat 16 detik daftar tidak monoton,
   dan penanda merah 1–4 memberi rasa kemajuan.
4. **Sebut nama → tunjukkan logo asli tepat di kata itu.** "Google Sheets, Google Drive, Meta Ads" → logo muncul satu per satu di
   kata masing-masing, mengelilingi "AI" di tengah = gagasan "AI diberi akses ke semua alat ini" terlihat sebagai gambar.
5. **Konsep abstrak tanpa wujud asli → diagram sangat minimal, atau b-roll metafora.** "Timer/cron" → monitor server (suasana);
   "jam 9 / jam 12" → timeline yang digeser; "10 → 100" → piktogram + batang. Diagramnya monokrom, satu gagasan, digerakkan kamera
   (pan, motion blur) bukan dihias. Tidak ada UI palsu buatan kode.
6. **Teks besar menggantikan b-roll untuk kalimat opini/penghubung.** Saat tidak ada benda untuk diperlihatkan, kata kunci kalimat
   dibesarkan dan diberi hierarki (kecil–besar–serif), jadi layar tetap "berubah" setiap ±1 s tanpa memaksakan gambar.
   Close-up blur dipakai agar teks besar jadi subjek dan wajah jadi latar.
7. **Warna mengikuti makna.** Satu aksen kuning untuk konsep inti; merah hanya sekali untuk "menyeramkan". Aksen oranye starburst
   hanya di pembuka (energi hook).
8. **Ukuran/durasi mengikuti waktu baca.** Kartu headline 4,8 s (2 kalimat), insert UI 3–5,5 s (dibaca), b-roll metafora ±1,1 s per klip
   (tidak perlu dibaca), diagram ±2 s (satu gagasan), teks besar ±0,8–1,6 s per frasa.
9. **Transisi sebagai penanda bagian.** Flash putih menutup hook; light-leak menutup blok "4 bagian prompt" dan blok "diagram 10→100";
   sisanya hard cut + blur→fokus (cepat, tidak mengganggu).

---

## Yang tidak bisa dipastikan
- Audio/SFX, musik, dan apakah ada sound design di flash/light-leak (tidak bisa mendengar).
- Nama font persis (sans grotesk tebal + serif "transitional"; tidak bisa dipastikan) dan kurva easing persis (hanya terlihat dari jarak
  frame: blur-in ±4–6 f, pan UI ±24 f ease-in-out, light-leak ±8–10 f).
- Apakah kartu headline diketik ulang atau dipotong dari screenshot Bloomberg Technoz, dan apakah baris abu adalah subjudul asli.
- Apakah UI ChatGPT adalah rekaman layar atau screenshot yang dianimasikan.
- Sumber/lisensi b-roll CGI dan ikon (stok? gambar generatif?).
- Apakah close-up ekstrem adalah shot kamera kedua atau punch-in digital dari shot medium (blur menyulitkan).
- Transkrip Whisper di 57,04 ("gue tidak ngerti") berbeda dengan subtitle video ("buat yang nggak ngerti"); subtitle video kemungkinan benar.
