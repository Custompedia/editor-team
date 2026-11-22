# STYLE NOTES — kenapa edit referensi user lebih bagus, dan cara menerapkannya di roll APA PUN

Ditulis 2026-11-22 dari studi 3 video referensi user (dikirim setelah user menilai job01 final_v4 "jujur rada kurang").
Baca SETELAH `GUIDE-edit-aroll.md` dan `/home/user/CLAUDE.md`. Kalau bertentangan: CLAUDE.md (preferensi user) > catatan ini > guide.

**Ini PRINSIP, bukan template.** Jangan menyalin warna kuning, font Playfair, chat bubble, atau layar hitam-putih ke setiap video.
Yang disalin adalah *cara memutuskan*: kalimat mana yang diberi visual, visual jenis apa, seberapa besar, berapa lama, dan bagaimana
masuk-keluarnya. Warna/font/gaya tetap diputuskan per video dari brief, brand, dan footage.

---

## 0. Bahan yang dipelajari (bisa dibuka ulang)

| File | Isi | Durasi |
|---|---|---|
| `/home/user/jobs/job01/work/ref/Cara-Hitung-Hardbox_final_v3.mp4` | **Footage yang SAMA dengan job01**, diedit lebih bagus → referensi utama | 128,4 s, 1080x1920 |
| `/home/user/jobs/job01/work/ref/Parcelin_Box_Lebaran.mp4` | Brand sama, roll lain (Lebaran, pesan dari kapan) | 53,4 s, 1440x2560 |
| `/home/user/jobs/job01/work/ref/Parcelin_MOQ_Softbox.mp4` | Brand sama, roll lain (minimal order softbox) | 94,4 s, 1440x2560 |
| `/home/user/jobs/job01/out/final_v4.mp4` | Edit kita yang dinilai "kurang" | 112,3 s |

Contact sheet 1 fps: `work/ref/hardbox_sheet_*.jpg`, `v4_sheet_*.jpg`, `lebaran_sheet_*.jpg`, `moq_sheet_*.jpg`.
Strip rapat (2–30 fps) di momen penting: `work/ref/strips/*.jpg` (nama file = video_detik-mulai). Transkrip kalimat referensi:
`work/ref/tx/*.txt` (large-v3, dijalankan lewat heavy lock).

Catatan: Hardbox v3 jelas dibuat dengan **kit yang sama** dengan kita (subtitle kecil + kata besar serif miring, label `SUMBER`,
`title` dengan stabilo, `bubbles` dengan foto + silang merah, `chips`, insert berantai geser 12 frame). Jadi bedanya **bukan alat**,
tetapi **keputusan**: lebih banyak momen yang divisualkan, visual yang tepat menggambarkan konsepnya, beberapa komponen custom kecil,
dan penutup yang megah.

---

## 1. Angka: referensi vs v4 (footage sama)

| Ukuran | Hardbox ref v3 (128 s) | Kita v4 (112 s) |
|---|---|---|
| Jumlah "beat" visual (insert, panel, overlay, efek) | ±25 → 1 tiap ±5 s | 13 → 1 tiap ±8,6 s |
| Insert layar penuh | ±45 s = **±35%** | 18 s = **15%** (+ split 8%) |
| Rentang terpanjang hanya wajah (tanpa overlay/insert) | ±6–7 s (95–102 s, 82–89 s) | **±16 s** (28–44 s), ±11 s (92–103 s) |
| Kata besar | ±40 → 1 tiap ±3 s | 18 → 1 tiap ±6 s |
| Opening (0–13 s) | judul → 2 chat bubble (pakai thumbnail box) → **layar hitam-putih** di "gimana? nggak bisa" | judul → hanya subtitle |
| Penutup | profil IG asli + kursor klik "DM", lalu **foto brand layar penuh** + logo/handle di atasnya | chip kecil "DM IG @…" 6 s + kartu krem polos |
| Struktur | recap "jangan langsung tanya" DIPERTAHANKAN dan dijadikan callback (bubble yang sama + silang merah + 2 chip) | recap dibuang |

Kesimpulan kasar: **dua kali lebih padat, dua kali lebih banyak layar penuh, tidak ada lubang panjang**, dan visualnya **menggambarkan
konsep** yang diucapkan (bukan sekadar "foto produk brand").

---

## 2. Prinsip (dengan contoh dan kesalahan v4)

Format: **Aturan** → kapan / kapan tidak → durasi → contoh referensi (detik) → kesalahan v4.

### P1. Gambarkan KONSEP yang diucapkan, bukan sekadar "sesuatu dari brand"
- Setiap kata benda konkret, angka, atau istilah teknis yang jadi inti kalimat dapat gambar yang **persis memperlihatkan hal itu**.
  Penonton harus mengerti kata itu dari gambarnya saja, dalam <1 detik.
- Ref Hardbox 20,6–26,7: "ukuran" = **diagram box 3D yang menggambar diri** dengan label P/L/T; "desain" = foto tangan melipat
  kertas cetak; "finishing" = makro foil emas timbul. Ref 89–93: "budget sekian → kuantiti sekian" = **kurva harga/pcs vs quantity**
  dengan titik "budget kamu / quantity segini"; "inner" = foto box parfum dengan foam insert.
- **v4:** "ukuran / desain / finishing" diwakili 3 foto portofolio kecil di kartu krem (tas kertas, tube merak, book box natal):
  foto bagus, tapi tidak satu pun **memperlihatkan** ukuran/desain/finishing. "Desain, kuantiti, inner" hanya chip teks.
- Aturan sumber tetap: aset nyata dulu. Tapi "nyata" artinya **foto/rekaman nyata dari HAL yang dibicarakan** (bahan, mesin, proses,
  uang, gudang), tidak harus dari akun brand. Foto brand dipakai saat yang dibicarakan memang brand/produknya (bukti, portofolio, CTA).
  Untuk konsep yang tidak ada fotonya → diagram SVG custom yang digambar bertahap.

### P2. Ucapan orang lain → chat bubble, ditumpuk, dengan thumbnail bendanya
- Kapan: pembicara menirukan pertanyaan/ucapan pelanggan ("Mbak, …harganya berapa?", "aku belum tau mbak…", "Mbak, budget 20 ribu…").
  Bubble muncul tepat di awal kutipan, bertumpuk (bubble ke-2 di bawah, sedikit bergeser ke kanan), tetap sampai punchline, lalu hilang.
- Bubble pertanyaan di ref memakai **thumbnail benda yang ditanyakan** (tube box gelap, softbox krem) → penonton langsung paham "kayak gini".
- Posisi: sepertiga atas, kecil (lebar ±60–70% layar), tidak menutup wajah. Masuk = pop skala 0→1 dalam ±5 frame.
- Ref Hardbox 3,0–10,7 (2 bubble), 44–47 (kutipan "aku belum tau mbak" 2 bubble), 69–74 (kutipan budget 2 bubble), **109,8–112,6
  callback**: bubble "Mbak, mau bikin box kayak gini…" muncul lagi lalu dicap **silang merah** tepat di "nggak bisa".
- Kiri/kanan: user menyebut bubble "kiri dan kanan". Pakai kiri untuk pelanggan 1, kanan untuk pelanggan 2 kalau ada dua penanya
  berbeda; pakai satu sisi kalau satu orang. Jangan bubble untuk kalimat pembicara sendiri.
- **v4:** opening (3–10 s) tanpa bubble sama sekali; pertanyaan hanya terbaca sebagai subtitle. Bubble kutipan 44–47 dan 62–67 ada,
  tapi tanpa thumbnail dan tanpa callback.

### P3. Punchline = ubah "dunia" gambar sejenak (dim / hitam-putih / gelap)
- Kapan: kalimat yang membalik ekspektasi atau jadi poin utama ("Gimana? Nggak bisa, nggak bisa dijawab"). **1–2 kali per video saja.**
- Ref Hardbox 10,30–12,85: pada kata "gimana?" gambar **langsung (hard cut, 1 frame)** jadi hitam-putih + sedikit gelap + vinyet; bubble
  pertanyaan memudar ±0,4 s kemudian (10,66–10,83) tepat sebelum "nggak bisa"; kata besar "nggak bisa" muncul di atas gambar abu-abu.
  Efek bertahan sampai kalimat selesai lalu digantikan insert berikutnya (artikel) dengan fade → warna kembali tersembunyi di balik insert.
- Pilihan lain yang setara: brightness 0,4–0,5 (dim), zoom-in cepat 1.0→1.12, atau layar gelap dengan satu kata. Pilih satu per video.
- **v4:** "nggak bisa nggak bisa" (11–13 s) hanya subtitle biasa; tidak ada beat.

### P4. Pilih tata letak dengan aturan, bukan selera
| Tata letak | Pakai saat | Durasi wajar | Contoh referensi |
|---|---|---|---|
| **Wajah saja** (+ kata besar) | opini, emosi, kalimat penghubung, ajakan langsung ("jadi jangan lagi ya…"), saat pembicara memegang/menunjukkan benda | ≤ 6–7 s berturut-turut | Hardbox 95–101, 106–109; MOQ 0–6 (ia memegang lembaran box) |
| **Overlay kecil di atas wajah** (bubble, chip, tag harga, chip brand) | kutipan, daftar ringkas, angka kecil, nama brand/akun | 2–7 s | Hardbox 60,5–61,6 tag "Rp10.000 /pcs" di samping wajah; 114–117 chip "1 Spesifikasi lengkap / 2 atau… budget kamu"; Lebaran 5,7–10 chip "Parcelin ✓ @parcelinpack · Custom Packaging" |
| **Panel atas + wajah di bawah** (split) | info yang **bertambah** sambil ia menjelaskan (daftar MOQ, timeline bulan) | 4–12 s, isi panel tumbuh | MOQ 46–56 panel "Minimal order softbox" yang barisnya muncul satu per satu (100 / 300 / 1.000 pcs); Lebaran 16,4–20,2 timeline NOV–MAR yang terisi saat "2–3 bulan… 4 bulan" |
| **Wajah atas kecil + UI besar di bawah** (inverted split) | CTA/aksi di aplikasi yang diucapkan panjang (DM, konsultasi) | 8–12 s | MOQ 80,5–92: wajah di 35% atas, profil IG → ketik DM → balasan admin di bawah |
| **Layar penuh** | konsep yang lebih jelas dilihat daripada didengar; bukti; daftar berantai; showcase penutup | 1,5–4 s (screenshot/grid yang dibaca: 3–7 s) | semua contoh P1, P6–P9, P11 |
- Saat pembicara **menunjukkan benda ke kamera**, jangan ditutup insert; overlay di atas masih boleh (ref 8–10 s: box hijau terlihat,
  bubble tetap di atas).
- **v4:** layar penuh hanya 15%; split dipakai untuk foto yang sebenarnya lebih baik layar penuh (parfum 53–59, rekomendasi 88–91);
  chip CTA kecil dipakai di momen yang paling butuh layar penuh (DM).

### P5. Daftar berurutan → rantai layar penuh, ATAU panel yang menumpuk
- "mulai dari ukurannya, mulai dari desainnya, mulai dari finishingnya" → 3 insert berantai, masing-masing dengan label bernomor
  (`01 UKURAN` + sub "panjang × lebar × tinggi"), digeser 12 frame dari kanan tepat di kata berikutnya (ref 20,6 / 23,1 / 25,1).
- Kalau item daftar harus tetap terlihat bersama (perbandingan, tingkat MOQ) → panel yang barisnya bertambah (MOQ 46–56), atau
  stepper dengan centang (Lebaran 20,6–26: "1 Promosi → 2 Foto produk → 3 Repeat order", foto berganti, langkah lalu dicentang).
- **v4:** rantai ada, tapi kartu kecil di latar krem yang sama ×3 → terasa seperti slide template.

### P6. Angka dan hubungan → tunjukkan di bendanya
- Harga diucapkan → **label harga menempel di produk** ("Rp10.000", "Rp20.000" pop di box hitam, ref 31,3–33,4) atau tag kecil di
  samping wajah ("Rp10.000 /pcs", 60,5).
- Hubungan dua besaran → kurva/diagram yang menggambar diri (budget ⇄ quantity, 89–93).
- Tanggal/tenggat → timeline (Lebaran 16–20 bulan; 32–35 garis waktu vertikal "Hari ini → 25 Des → 8 Feb → 9 Mar, ±10 minggu").
- Angka yang hanya contoh → tulis "contoh" kecil, jangan dijual sebagai data.
- **v4:** "10 ribu / 20 ribu / ready stock" (32–35 s) hanya kata besar di wajah.

### P7. Negasi dan kontras → cap / coret / pasangan
- "kita nggak jual packaging ready stock" → foto rak gudang, cap "READY STOCK" lalu **dicoret merah**, lalu label "CUSTOM · dibuat per
  pesanan" (ref 33,5–34,7). "nggak bisa" di recap → silang merah di bubble (112,2).
- Kontras dua kelas → dua visual berurutan dengan label sejajar: "PACKAGING REGULER · contoh: box parfum" (53–55, box putih polos) vs
  "PACKAGING PREMIUM · budget-nya berapa?" (62–64, box hijau foil). Ref bahkan menyusun potongan dari dua take (C + E) supaya
  kontras reguler/premium terdengar utuh.

### P8. Syarat abstrak → dokumen yang terisi, dan kembali lagi nanti (callback)
- "kalian harus ada spesifikasi lengkapnya" → kartu formulir "SPESIFIKASI · custom packaging form order" dengan baris kosong
  Ukuran/Bahan/Desain/Finishing/Quantity/Inner yang muncul berurutan, lalu cap "WAJIB ADA" (ref 37,2–39,9).
- Saat "kalau kamu udah ada spesifikasi lengkap, semuanya lebih memudahkan" → **formulir yang sama** kini terisi tulisan tangan
  (20×15×8 cm, Board 2 mm, Full color, Doff + foil, 500 pcs, Foam), tiap baris dicentang, cap hijau "LENGKAP ✓" (102–106).
- Callback membuat cerita terasa dirancang. Bentuk formulirnya mengikuti dunia nyata (form order), logo brand kecil di pojok.

### P9. Platform/aplikasi → tunjukkan ISINYA, bukan bingkainya; ada aksi
- "kirimin gambar di Pinterest… cari di Pinterestnya Parcelin… referensi banyak banget" → layar penuh **grid pin 2 kolom besar** (logo
  Pinterest + kolom cari "hardbox parfum custom" saja sebagai penanda), scroll pelan, tombol merah "Simpan" muncul di pin saat disorot
  (ref 74,5–81,7, ±7 s).
- "DM aja" → profil IG asli dalam kartu, pil "DM @parcelinpack", kursor bergerak dan klik (120,2–122,8). MOQ: profil → layar DM, pesan
  diketik huruf demi huruf, terkirim, balasan admin muncul (82–92). Lebaran: situs di mockup laptop → kursor klik tombol WA → halaman
  WhatsApp "Admin 2 Parcelinpack", sambil chip "Konsultasi ✓ Prototipe ✓ Sampel ✓" tercentang sesuai ucapan (43–48).
- **v4:** Pinterest 70–75 = screenshot halaman profil, sebagian besar layar berisi header/bio; pin-nya kecil di bawah. Isi yang
  membuat orang terpesona (packaging-nya) hampir tidak terlihat.

### P10. Klaim tentang brand/waktu → bukti pihak ketiga dengan kalimat distabilo
- "Karena Parcelin itu jual custom packaging" → artikel berita (JPNN, "Parcelinpack Tingkatkan Daya Saing UMKM dengan Packaging Kreatif")
  dengan stabilo pada "Parcelinpack" lalu "Packaging Kreatif" tepat saat kata itu diucapkan (ref 12,9–16,6).
  Lebaran 29,6–31,9: artikel detik + 2 callout tanggal (1 Ramadan / Idul Fitri) untuk "ini mepet banget waktunya".
- Bukti pihak ketiga > halaman brand sendiri. Kalau tidak ada, halaman brand dengan stabilo kalimat yang relevan.
- **v4:** situs parcelin.id 13–16 (bagus, tapi hanya banner; tidak ada kalimat yang distabilo).

### P11. Standar gambar nyata yang "bagus"
- Full-bleed (mengisi layar) atau satu kartu besar; **satu subjek jelas**, cahaya bagus, latar bersih, warna menyatu dengan palet video.
- Terbaca di HP dalam 1 detik. Tidak ada watermark asing, teks kecil yang tak terbaca, atau kolase ramai.
- Portrait atau bisa di-crop 9:16 tanpa memotong subjek. Selalu bergerak pelan (push 1.0→1.06 atau scroll).
- Latar diagram berganti mengikuti suasana scene (navy untuk diagram ukuran, hijau gelap untuk kurva, cokelat gelap untuk formulir),
  tetapi **satu warna aksen** sepanjang video.
- Catatan kejujuran: banyak foto konsep di ref (box hitam, uang, gudang, foil, box parfum hijau) terlihat seperti foto stok premium atau
  gambar generatif. Sumbernya tidak bisa kita verifikasi dari video. Untuk kita: cari foto nyata (Openverse, situs resmi, Pinterest brand,
  aset user); kalau tidak ada, **tanya user** atau minta gambar generatif lewat `work/gen_prompts.md` (guide 6.2). Jangan menurunkan
  standar ke foto yang tidak menggambarkan konsepnya.

### P12. Kapan TIDAK memberi visual
- Kalimat penghubung, opini, emosi, ajakan langsung yang butuh kontak mata ("jadi jangan lagi ya kalau ketemu aku langsung tanya").
- Saat ia menunjukkan benda (lihat P4).
- Napas sebelum/ sesudah beat besar: ±1–3 s wajah bersih di antara dua visual kuat membuat visual berikutnya terasa.
- Di 3 detik pertama: wajah + judul, bukan insert.
- Batas atas: jangan sampai >50% layar penuh (slideshow). Ref Hardbox ±35%, MOQ dan Lebaran juga ±30–40% plus panel.

### P13. Opening hook
- 0,3–2,8 s: judul dua baris kecil-besar (ref "CARA HITUNG HARGA / **Hardbox**" dengan stabilo yang menyapu kiri→kanan dalam ±8 frame;
  Lebaran "LEBARAN 2027 / Packaging Lebaran, pesan dari **kapan?**"; MOQ chip topik "Softbox bisa **100 pcs**?" dengan logo, bertahan ±6 s).
  Judul = pertanyaan/topik video, satu kata kunci disorot.
- ±3 s: elemen kedua langsung masuk (bubble pertanyaan) → tidak ada jeda kosong.
- ±10–13 s: beat punchline (P3) lalu insert layar penuh pertama. Dalam 15 detik pertama penonton sudah melihat 4 perubahan visual.
- **v4:** judul "PACKAGING CUSTOM / harganya berapa?" lalu 10 detik hanya subtitle.

### P14. Penutup / CTA: megah, layar penuh, nyata
- Saat CTA diucapkan ("DM aja"): profil/akun asli **layar penuh** atau inverted split, dengan aksi (kursor klik DM, ketik pesan).
- Kata-kata terakhir ("…packaging sesuai sama impian kamu") → **showcase brand layar penuh**: foto produk brand terbaik (ref 125,4–128,4:
  deretan hardbox cokelat-zaitun, masuk dengan dissolve 3 frame, push pelan), kata besar "impian kamu" di atasnya, lalu logo bulat +
  handle + pil CTA "konsultasi packaging? DM aja" muncul di atas foto yang sama (±2 s). Tidak ada kartu polos terpisah.
- Lebaran/MOQ menutup dengan kartu logo krem — tetap boleh, tetapi CTA-nya spesifik untuk video itu ("Amanin slot Lebaran kamu").
- **Permintaan user untuk Parcelin:** penutup = **Pinterest Parcelin layar penuh** (grid pin terbaik yang asli, bergerak/scroll, bukan chip
  kecil atau kartu). Pin terbaik yang sudah diunduh ada di `jobs/job01/work/cand/pin/` (sumber di `SOURCES.txt`): mis. p09 (Klavuu pink),
  p11 (Clean & Fresh), p13/p21 (TIME hitam), p17 (leopard), p18 (bola tenis hijau), p03 (tube merak), p24 (book box natal).
- **v4:** chip "DM IG @parcelincompany" 104–109 s + kartu krem 110–112 s → user menilai lemah.

### P15. Struktur: potongan yang melayani visual
- Recap yang bisa dijadikan callback visual **layak dipertahankan** (ref 106–118: bubble lama kembali + silang + chip 2 opsi). Jangan
  otomatis membuang "pengulangan" kalau pengulangan itu adalah kesimpulan.
- Take yang gambarnya rusak tapi audionya terbaik boleh dipakai bila gambarnya ditutup insert yang relevan (ref 48,5–51,9: kalimat budget
  dari take A — yang di v1 kita ketahuan berakhir dengan pembicara mengangkat gelas — ujung kalimatnya DAN sambungan ke take C tertutup
  foto uang layar penuh, lalu dissolve ke take C; v4 justru mengganti take). Insert yang relevan = cara paling rapi menyembunyikan jump
  cut antar-take.
- Menggabung take untuk membuat kontras jelas (reguler dari take C + premium dari take E) itu sah selama sambungannya bersih (QA4).
- Durasi boleh sedikit lebih panjang (ref 128 s vs v4 112 s) bila tiap detik tambahan membawa visual/cerita.

### P16. Rasa gerak (semua dari `useCurrentFrame`, tanpa CSS animation)
| Elemen | Gerak di referensi |
|---|---|
| Bubble, chip, tag harga, cap | pop skala dengan sedikit overshoot, 4–6 frame; cap sedikit miring |
| Insert dari wajah | fade 6–7 frame + skala 1.06→1 (default kit) |
| Insert berantai | geser horizontal 12 frame, insert lama tetap di bawah |
| Panel atas / laptop | geser vertikal (wajah terdorong), pegas |
| Beat punchline | hard cut 1 frame ke hitam-putih/dim |
| Penutup foto | dissolve 3 frame, push pelan |
| Diagram | digambar mengikuti kata (kerangka → isi → label satu per satu) |
| Screenshot | kartu naik dari bawah, stabilo menyapu saat kata diucapkan, push pelan |
| Kursor | bergerak lengkung, klik sekali, tombol tertekan |
Semua elemen muncul **tepat di kata** yang digambarkannya (jangkar kata, offset −2…−4). Tidak ada yang berdenyut terus.

### P17. Subtitle
- User tidak mengeluhkan subtitle. Ketiga referensi berbeda gaya: Hardbox = gaya kit (huruf kecil, kata besar serif miring kuning);
  Lebaran/MOQ = kalimat biasa dengan tanda baca, 1–2 baris, kata kunci diwarnai dalam baris (oranye/kuning), tanpa baris kata besar.
  → Prinsipnya: satu sistem per video, kata kunci ±1 tiap 3 s, terbaca di semua latar (gelap di atas insert terang).
- Di insert layar penuh referensi, subtitle tetap di area bawah atau tepat di bawah kartu (Lebaran/MOQ) — tidak pernah menabrak isi.

### P18. Tampilan per video (bukan satu gaya)
- Hardbox ref memakai kuning + navy/hijau gelap/cokelat gelap; Lebaran & MOQ memakai palet brand (oranye #DE6B17-ish, cokelat, krem) +
  Plus Jakarta Sans. Ketiganya bersih: sedikit elemen, satu aksen. Ikuti brand bila ada (CLAUDE.md), tetapi **variasikan latar scene**
  supaya tidak terasa satu template krem.

---

## 3. Perbandingan per kalimat: Hardbox ref v3 vs v4

| Kalimat | Ref v3 (detik → visual) | v4 (detik → visual) |
|---|---|---|
| "aku sering banget ditanyain" | 0,3–2,8 judul CARA HITUNG HARGA / Hardbox | 0–3 judul PACKAGING CUSTOM / harganya berapa? |
| "Mbak, mau pesen packaging ini… berapa?" | 3,0 bubble 1 + thumbnail tube box | subtitle saja |
| "Mbak, mau pesen softbox… berapa?" | 6,2 bubble 2 + thumbnail softbox; box hijau di tangan tetap terlihat | subtitle saja (box di tangan terlihat) |
| "Gimana? Nggak bisa… dijawab" | 10,3–12,9 hitam-putih, bubble hilang, kata besar "nggak bisa" | subtitle saja |
| "Karena Parcelin itu jual custom packaging" | 12,9–16,6 artikel JPNN + stabilo | 13,4–16,1 screenshot parcelin.id |
| "faktornya/variabelnya banyak banget" | wajah + kata besar | wajah |
| "ukuran / desain / finishing" | 20,6–26,7 diagram box 3D → foto tangan melipat → makro foil, berantai | 21,3–27,7 3 kartu foto portofolio |
| "Apa aja… buat ngitung harga" | wajah + kata besar "harga" | wajah |
| "oh ini 10.000, oh ini 20.000" | 31,3–33,4 box hitam + label harga pop | kata besar |
| "nggak jual ready stock" | 33,5–34,7 gudang + cap READY STOCK dicoret + "CUSTOM" | kata besar |
| "harus ada spesifikasi lengkapnya" | 37,2–39,9 formulir kosong + "WAJIB ADA" | kata besar |
| "aku belum tau mbak… ini itunya" | 44–47 2 bubble | 44–48 1 bubble |
| "nyebutin budgetnya ada berapa" | 48,5–51,2 foto uang + label BUDGET | (take B) kata besar |
| "packaging reguler, misalnya parfum… 10 ribu" | 53–55 box putih "REGULER"; 60,5 tag Rp10.000/pcs | 53,6–59,8 split foto Full Moon Box |
| "packaging premium… budgetnya berapa" | 62–64 box hijau foil "PREMIUM" | (dalam split di atas) |
| "konsultasi dulu sama aku" | wajah + kata besar | wajah + kata besar |
| "Mbak, budget 20 ribu… modelnya gimana" | 69–74 2 bubble | 62–67 1 bubble |
| "kirimin gambar di Pinterest… referensi banyak" | 74,5–81,7 grid pin besar, scroll, "Simpan" | 69,7–75,2 screenshot profil Pinterest (pin kecil) |
| "bantu hitungin… budget sekian… kuantiti… inner" | 89–93 kurva budget⇄quantity; 93–94 foto inner | 80–87 chip teks 1 desain/2 kuantiti/3 inner |
| "ngasih rekomendasi packaging" | wajah + kata besar | 88,4–91,5 split foto portofolio |
| "budgetnya / spesifikasi lengkap… memudahkan" | 102–106 formulir yang sama terisi + LENGKAP ✓ | kata besar |
| recap "jangan langsung tanya… nggak bisa… spesifikasi atau budget" | 109,8–117 bubble callback + silang + 2 chip | dibuang |
| "DM aja, nanti aku bantu konsultasi" | 120,2–122,8 profil IG + pil DM + kursor klik | 103–109 chip kecil "DM IG @…" |
| "packaging sesuai impian kamu" | 125,4–128,4 foto brand layar penuh + logo + handle + CTA | wajah; lalu 109,6–112 kartu krem logo |

---

## 4. Quality bar — wajib lolos sebelum render penuh

Tulis jawabannya di `work/visual_plan.md` (satu baris per butir).

1. [ ] Hook: judul/topik dalam 0,5 s; perubahan visual kedua ≤ 3,5 s; ada beat (bubble/punchline/insert) sebelum 13 s.
2. [ ] Setiap kutipan orang lain = bubble; pertanyaan tentang benda pakai thumbnail benda itu.
3. [ ] Ada tepat 1–2 beat punchline (dim/BW/zoom) di kalimat pembalik utama — tidak lebih.
4. [ ] Setiap angka, istilah teknis, dan item daftar punya visual yang **memperlihatkan konsepnya** (tes: tutup subtitle, apakah gambarnya
       masih menjelaskan kata itu?).
5. [ ] Tidak ada >7 s wajah tanpa elemen apa pun; tidak ada >50% layar penuh. Target jualan/edukasi: layar penuh 30–40%, beat tiap ±5 s.
6. [ ] Tiap keputusan tata letak punya alasan dari tabel P4 (wajah / overlay / panel / inverted split / layar penuh). Minimal 3 tata letak
       dipakai, dan latar insert tidak sama semua.
7. [ ] Platform yang disebut tampil dari aslinya, isinya besar (bukan header), dan ada aksi bila diucapkan aksi (klik, DM, simpan).
8. [ ] Klaim brand/waktu punya bukti dengan stabilo di kalimat yang tepat.
9. [ ] Penutup: CTA layar penuh/inverted split dengan aksi + showcase brand layar penuh dengan logo/handle di atasnya. Tidak ada chip kecil
       sebagai CTA utama. Handle sudah dikonfirmasi.
10. [ ] Callback: kalau ada recap, visual pembuka (bubble/formulir) kembali dengan status baru (silang / terisi).
11. [ ] Semua gambar lolos P11 (satu subjek, terbaca di HP, tanpa watermark asing, bergerak pelan) dan sumber + lisensinya tercatat.
12. [ ] Gerak: semua elemen muncul di kata yang digambarkannya; transisi dari tabel P16; tidak ada elemen berkedip terus.
13. [ ] Still diambil di tengah SETIAP beat dan di 2–3 frame awal/akhirnya; semua dibuka. QA5 (subtitle vs suara) sudah dicek dengan still
       sebelum render penuh.

---

## 5. Gap list — kit sekarang vs yang perlu komponen baru

### Sudah bisa dengan kit (`video/src` Main.tsx / Visuals.tsx)
| Kebutuhan | Event kit | Catatan |
|---|---|---|
| Judul pembuka + stabilo | `title` (line1, line2) | stabilo menyapu sudah ada |
| Chat bubble kiri/kanan + thumbnail + silang merah | `bubbles` (`side`, `img`, `x_at`) | thumbnail & silang sudah ada; ukuran bubble di kit agak besar (font 40, img 132) — perkecil per job bila perlu |
| Chip bernomor muncul satu per satu | `chips` | |
| Artikel/halaman asli + stabilo + kursor klik + scroll | `screenshot` (`highlights`, `scroll`, `click`, `click_at`) | profil IG + klik "DM" bisa (kalau screenshot publik ada) |
| Insert berantai geser 12 frame | jangkar `end` = `start` berikutnya | |
| Foto layar penuh, push pelan, label bernomor + sub | `photo` (`num`, `label`, `sub`, `pos`, `dim`) | dipakai untuk desain/finishing/uang/gudang/reguler/premium |
| B-roll | `clip` | |
| Panel atas + wajah turun (gambar diam/video) | `split` | panel hanya gambar/video; tidak bisa berisi daftar yang tumbuh |
| Grafik batang | `custom` `bars` | |
| Kartu penutup di atas foto (logo bulat, handle, pil CTA) | `outro` (`img`, `logo`, `handle`, `cta`) | ini persis pola penutup ref Hardbox; ganti `img` dengan foto brand terbaik |
| Kata besar beraksen | `*kata` di `text`/`script` | |
| Kartu foto di latar terang, kartu logo | job01 `custom card`, `endcard` (hanya di job01/video/src) | |

### Perlu komponen baru (bangun di `video/src` job yang membutuhkannya; semua digerakkan `useCurrentFrame`, tanpa CSS animation)
1. **`grade` — beat punchline (BW / dim) di atas pembicara.** Event non-layar-penuh `{type:"grade", start, end, mode:"bw"|"dim",
   amount?:1, vignette?:0.35}`. Implementasi: di `Main.tsx` Speaker, hitung k(frame) = 1 di [f,t) (hard cut; opsional fade 3 frame di
   akhir), terapkan `filter: grayscale(k) brightness(1-0.25k) contrast(1+0.1k)` pada layer video + vinyet ekstra. Overlay lain yang
   aktif boleh diberi `fade_at` agar menghilang 0,4 s setelah grade mulai. Subtitle tidak ikut di-grade.
2. **`tags` — label harga/sticker yang menempel di gambar atau di samping wajah.** `{type:"tags", items:[{at, text:"Rp10.000",
   sub?:"/pcs", x, y, rot?:-8}]}`; pil aksen dengan titik/lubang tag, pop overshoot 5 frame. Bisa sebagai overlay (di atas wajah) dan
   sebagai child di dalam `photo` (`e.tags`), koordinat dalam px layar.
3. **`stamp` — cap/coret di atas foto.** Field opsional di `photo`: `{stamp:{text:"READY STOCK", at, strike_at, after:{text:"CUSTOM ·
   dibuat per pesanan", at}}}`: kotak bergaris putih miring −4°, garis coret merah menyapu 8 frame, label pengganti pop di bawahnya.
   Juga dipakai untuk cap "WAJIB ADA"/"LENGKAP ✓" di komponen form.
4. **`form` — formulir spesifikasi yang terisi.** `custom` `{name:"form", title, sub, logo?, rows:[{label, at, value?, value_at?,
   check_at?}], stamp?:{text, at, color}}` kartu krem 820 px di latar gelap brand; baris muncul di `at`, nilai "tulisan tangan" (font
   script sistem bila ada, kalau tidak serif miring) di `value_at`, centang hijau pop di `check_at`, cap di akhir. Pakai dua kali
   (kosong → terisi) untuk callback.
5. **`box3d` — diagram dimensi P×L×T.** `custom` `{name:"box3d", label, sub, color?}` isometrik SVG: kerangka digambar
   (strokeDashoffset 10 frame) → sisi terisi warna karton → garis ukur + bulatan P, L, T pop berurutan. Latar gelap (navy/brand).
6. **`curve` — kurva hubungan dua besaran.** `custom` `{name:"curve", label, sub, x_label, y_label, ticks:[...], mark:{x, y, label_x,
   label_y, at}}` sumbu digambar → kurva menurun digambar mengikuti kata → garis putus-putus + 2 label di `mark.at`. Tulis "contoh
   ilustrasi" bila angkanya tidak dari ucapan.
7. **`pingrid` — showcase grid Pinterest/portofolio layar penuh (PENUTUP yang diminta user).** `custom` `{name:"pingrid", imgs:[...8–14
   pin asli], header:{logo:"logos/pinterest.png"?, query?:"hardbox parfum custom", profile?:"Parcelin Company"}, scroll:px, save_at?:[{i,
   at}], end:{logo, handle, cta, at}}`. Masonry 2 kolom (lebar 500 px, sudut 24, gap 16) dengan tinggi mengikuti rasio asli; scroll
   pelan ke atas sepanjang durasi; pil merah "Simpan" pop di pin `i` saat `at`; di akhir (`end.at`) grid sedikit di-dim + blur 8 px dan
   logo bulat + handle + pil CTA muncul di tengah (pola `outro`). Header hanya penanda platform (tinggi ≤ 140 px). Hanya pin asli publik.
8. **`topsheet` — panel atas yang barisnya bertambah (MOQ/timeline).** Varian `split` dengan isi komponen, bukan gambar:
   `{type:"split", h:560, body:{name:"rows", title, rows:[{at, img?, text, sub?, badge}]}}` atau `{name:"months", items, fill:[{at, from,
   to, label}]}`. Perlu perubahan kecil di `SplitPanel`: bila `e.body`, render `CUSTOM[e.body.name]` di dalam panel (latar `bg`).
9. **`invsplit` — wajah di atas kecil, UI besar di bawah.** `{type:"invsplit", start, end, h_top:620, body:{...}}`: Speaker diskalakan
   0.55 dan dipusatkan di 0–620 px (crop wajah), panel bawah 620–1920 berisi screenshot/komponen. Subtitle pindah ke y ≈ 540. Masuk:
   panel naik dari bawah 12 frame dengan pegas, wajah mengecil bersamaan.
10. **`dmchat` — percakapan DM/WA yang mengetik.** `custom` atau body `invsplit`: header profil asli (avatar logo, nama, centang)
    dari screenshot nyata sebagai acuan; teks diketik per karakter (`text.slice(0, n(frame))`), tombol kirim diklik kursor, bubble
    terkirim pop, indikator "…" lalu balasan. Tampilan harus meniru UI asli (warna IG/WA), bukan karangan.
11. **`brandchip` — lower-third nama brand/akun.** Overlay kecil `{type:"brandchip", logo, name, verified?, sub:"@handle · Custom
    Packaging"}` di bawah subtitle area atas atau tepat di atas subtitle, pop masuk, 3–5 s, saat brand pertama kali disebut.
12. **`laptop` — mockup perangkat untuk situs.** Bingkai laptop/HP SVG sederhana yang membungkus `screenshot` (dengan scroll & klik)
    dan bisa berganti halaman (`pages:[{img, at}]`), plus deret checklist chip di bawahnya (`checks:[{text, at}]`).
13. **(Opsional) gaya subtitle "kalimat"** (Lebaran/MOQ): sentence case + tanda baca, kata kunci diwarnai dalam baris, tanpa baris kata
    besar. Flag `sub_style:"inline"` di `edit.json` → cabang di `Subs`.

Urutan prioritas membangun (dampak terbesar dulu): 7 `pingrid` (penutup) → 1 `grade` → 2 `tags` + 3 `stamp` → 4 `form` → 9 `invsplit`
+ 10 `dmchat` → 5/6 diagram → sisanya.

---

## 6. Fakta yang ditemukan dan perlu dikonfirmasi user (job01 / Parcelin)

- **Handle Instagram:** ketiga referensi memakai **@parcelinpack** (profil IG "parcelinpack", "ParcelinPack | Custom Packaging | PR Packaging |
  Hardbox", ±132 rb pengikut, terlihat di ref Hardbox 120–123 s dan MOQ 81 s). v4 memakai **@parcelincompany** (dari tautan footer
  parcelin.id). Konfirmasi ke user sebelum dipakai lagi.
- Nama brand di berita JPNN: "Parcelinpack". Di video: "Parcelin". Situs: "Parcelin Company".
- Judul ref Hardbox = nama folder Drive user: "Cara Hitung Harga Hardbox".
- Ref Hardbox memakai kuning + serif miring (default kit), Lebaran/MOQ memakai palet brand → user menerima keduanya; yang dinilai adalah
  kepadatan, ketepatan visual, dan kerapian, bukan warna.
