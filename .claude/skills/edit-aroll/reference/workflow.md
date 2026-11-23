# Bagian 3. Alur kerja: 11 tahap dengan gate

> **Aturan cloud Editor Team (mengalahkan teks di bawah bila bertentangan):**
> - Job dibuat dengan `bash /home/user/editkit/new_job.sh <job-id>`; jangan jalankan `tools/setup.sh`.
> - Setiap perintah Python: `source .venv/bin/activate && ...` (termasuk `gdown`, `yt-dlp`).
> - Perintah BERAT wajib antre: `flock /home/user/jobs/.heavy.lock <perintah>`: `transcribe.py`, `verify_audio.py`,
>   `node stills.mjs`, `render.sh`. Render: `CONCURRENCY=2 flock /home/user/jobs/.heavy.lock bash tools/render.sh vN`
>   (video 112 dtk ≈ 25 menit; satu putaran QA gagal ≈ 30 menit terbuang).
> - Sebelum Tahap 6: baca `style-notes.md` sampai habis. Sebelum render penuh (Tahap 9): lolos "Quality bar" di style-notes.md
>   bagian 4, DAN kerjakan QA 5 (subtitle vs suara) lebih dulu lewat still + transkrip supaya tidak membuang satu render.
> - QA 1 ditambah deteksi frame hitam: `ffmpeg -i out/final_vN.mp4 -vf blackdetect=d=0.03:pix_th=0.05 -an -f null - 2>&1 | grep -c black_start` harus 0.
> - Nama brand/orang: Whisper tidak mengenal nama buatan. Kalau brief tidak memberi ejaan, cari beberapa varian ejaan di web
>   sebelum menyimpulkan "tidak ditemukan"; tandai ASUMSI.
> - Sumber: Pexels (cek bot) dan Wikimedia (HTTP 429) tidak bisa dipakai dari sini; YouTube butuh login. Jangan diakali.
>   Pakai halaman resmi brand (situs, Pinterest publik) lewat `shot.py`, Openverse (hindari lisensi NC untuk video brand), atau aset user.

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
