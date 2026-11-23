# Bagian 3. Alur kerja: 11 tahap dengan gate

> **Aturan cloud Editor Team (mengalahkan teks di bawah bila bertentangan):**
> - Job dibuat dengan `bash /home/user/editkit/new_job.sh <job-id>`; jangan jalankan `tools/setup.sh`.
> - Setiap perintah Python: `source .venv/bin/activate && ...` (termasuk `gdown`, `yt-dlp`).
> - Perintah BERAT wajib antre: `flock /home/user/jobs/.heavy.lock <perintah>`: `transcribe.py`, `verify_audio.py`,
>   `node stills.mjs`, `render.sh`. Render: `CONCURRENCY=2 flock /home/user/jobs/.heavy.lock bash tools/render.sh vN`
>   (video 112 dtk ≈ 25 menit; satu putaran QA gagal ≈ 30 menit terbuang).
> - Sebelum menulis brief (Tahap 0): baca `visual-thinking.md` Bagian 6 (look) dan Bagian 4 (yang bisa dijangkau dari sini).
>   Sebelum Tahap 6: baca `visual-thinking.md` dan `visual-craft.md` sampai habis. Sebelum render penuh (Tahap 9): jawab uji diri
>   `visual-thinking.md` Bagian 8 dengan bukti, DAN kerjakan QA 5 (subtitle vs suara) lebih dulu lewat still + transkrip supaya
>   tidak membuang satu render.
> - QA 1 ditambah deteksi frame hitam: `ffmpeg -i out/final_vN.mp4 -vf blackdetect=d=0.03:pix_th=0.05 -an -f null - 2>&1 | grep -c black_start` harus 0.
> - Nama brand/orang: Whisper tidak mengenal nama buatan. Kalau brief tidak memberi ejaan, cari beberapa varian ejaan di web
>   sebelum menyimpulkan "tidak ditemukan"; tandai ASUMSI.
> - Sumber yang bisa dan tidak bisa dijangkau dari container ini, dan cara meminta ke user: `visual-thinking.md` Bagian 4. Yang
>   diblokir (Pexels, Wikimedia, YouTube, halaman berlogin) tidak diakali.

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
- **Look video** (warna penekanan, warna panel dan teks, font, gaya penekanan): diputuskan di sini dengan cara di `visual-thinking.md`
  Bagian 6. Tulis pilihan, alasan, dan yang ditolak. Nilainya nanti ditulis di blok `theme` di `work/edit.json` (`edit-json.md` 4.5);
  build menolak job tanpa `theme`. Pasang font yang dipilih sebagai font sistem sekarang, supaya tidak tertunda di Tahap 7.
- **Butuh dari user:** daftar semua yang hanya bisa didapat dari user (rekaman layar aplikasi yang disebut, screenshot profil berlogin,
  logo, foto produk, ejaan nama, akun). Tulis di `work/STATE.md` bagian "Butuh dari user" dan laporkan ke lead SEKARANG, bukan di Tahap 6.
  Lanjutkan dengan cadangan bertanda `ASUMSI` selama menunggu.
- **Tanya di awal (permintaan pemilik, job02):** daftar itu selalu memuat, dengan usulan bawaan untuk tiap butir supaya user cukup
  menjawab "ya": (1) isi penutup: logo dan tanda brand apa saja, akun, situs, ajakan; (2) file logo resmi; (3) musik: lagu pilihan
  user atau bebas dicari; (4) foto/footage yang kemungkinan dibutuhkan naskah; (5) akun dan ejaan. Setelah Tahap 3 (naskah sudah
  terbaca), kirim **pertanyaan naskah** ke lead dalam satu daftar kedua: kalimat mana yang butuh aset dari user, kalimat terakhir
  dan penutup yang diusulkan untuknya, kata yang tidak terverifikasi. Jangan menunggu jawaban; jangan pula menyimpan pertanyaan sampai laporan akhir.
- Referensi gaya kalau ada: dipelajari untuk memahami KENAPA sebuah keputusan bekerja, bukan untuk ditiru bentuknya.
- Apa pun yang tidak disebut user: isi dengan default dan tandai `ASUMSI`.

Kalau user memberi video referensi:

```bash
mkdir -p work/ref && yt-dlp -f "mp4/best" -o "work/ref/ref.%(ext)s" "<url>"
python3 tools/sheet.py video work/ref/ref.mp4 work/ref/sheet 1
```

Buka `work/ref/sheet_*.jpg` dan catat: posisi dan gaya subtitle, seberapa sering visual muncul, jenis visualnya, tata letaknya (layar penuh atau terbagi), cara masuk dan keluarnya, dan untuk tiap pola: kenapa itu cocok untuk isi video referensi itu. Kalau unduhan gagal karena video diblokir wilayah, privat, atau butuh login: **jangan diakali** (tanpa VPN, proxy, cookie pinjaman). Minta user mengirim file mp4-nya, dan lanjutkan dulu dengan default di guide ini.

Preferensi desain yang pernah dinyatakan user (di percakapan ini, di file catatan project, atau di memori agent) dicatat di brief dan berlaku untuk seluruh video.

**Gate:** klip ada di `raw/`. Jenis konten, durasi target, dan CTA terisi. Look diputuskan dengan alasan. Daftar "Butuh dari user" sudah dilaporkan (atau tertulis "tidak ada"). Semua asumsi ditandai.

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

**Take dasar (permintaan pemilik, job02).** Kalau ada lebih dari satu take dari naskah yang sama, pilih SATU take sebagai dasar
seluruh video: take yang paling utuh dari awal sampai akhir (paling sedikit tersendat, energi stabil, gambar baik). Take lain hanya
menjadi sumber untuk kalimat yang di take dasar rusak atau tidak ada, dan setiap pengambilan dari take lain adalah satu potongan yang
harus ditutup gambar (Tahap 3). Tulis di `roll_map.md`: take dasar, alasannya, dan berapa potongan yang dibutuhkan tiap pilihan take
dasar. Mencampur dua take kalimat demi kalimat menghasilkan audio yang rapi dan gambar yang meloncat: job02 v4 punya 5 potongan
dalam 52,7 dtk dan pemilik menilainya "kebanyakan cut… patah-patah".

Cara memilih take untuk satu kalimat (dalam take dasar yang punya take ulang di dalamnya): (1) kalimatnya selesai tanpa tersendat, (2) tidak ada kata yang diulang atau dikoreksi, (3) energi dan kecepatan bicaranya cocok dengan kalimat sebelum dan sesudahnya, (4) kalau setara, pilih yang lebih pendek. Jangan otomatis memilih take terakhir.

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
6. Sebelum membuang pengulangan di akhir, tanyakan apakah itu kesimpulan yang bisa menyambung ke visual awal (`visual-thinking.md` 2.2).
   Take dengan audio terbaik tetapi gambar bermasalah boleh dipakai kalau gambarnya akan tertutup visual yang memang relevan.
7. Pertahankan: jeda napas wajar, kata sambung yang membuat kalimat terdengar alami, dan gaya bicara pembicara. Ini video orang bicara, bukan teks yang dibacakan.

Uji sambungan: baca naskah final dari atas ke bawah. Di setiap pergantian segmen, cek tiga hal. Pertama, kalimat sesudah potongan tidak merujuk ke sesuatu yang ikut terbuang ("yang tadi", "itu", "kedua" tanpa "pertama"). Kedua, tata bahasanya nyambung, tidak ada kata sambung menggantung. Ketiga, tidak ada informasi yang disebut dua kali.

Jumlah potongan: untuk satu pembicara yang lancar, biasanya 3 sampai 8 segmen per 2 menit. Roll yang banyak tersendat boleh lebih. Lebih baik satu segmen panjang yang utuh daripada tiga potongan kecil yang masing-masing menghemat setengah detik.

**Gambar harus mengalir (syarat pemilik 12).** Naskah yang enak didengar belum tentu enak dilihat: di setiap potongan, posisi kepala,
tangan, dan benda yang dipegang berpindah seketika, dan penonton melihatnya sebagai video yang ter-skip. Karena itu untuk SETIAP
potongan di `script.md`, tulis tiga hal:

1. **Kenapa harus dipotong.** Alasan yang sah: take ulang, salah ucap, mulai ulang, jeda mati yang panjang, kalimat yang menyimpang.
   Bukan alasan: menghemat setengah detik, kalimat di take lain sedikit lebih rapi, jeda napas, kata pengisi yang wajar.
2. **Apa yang terlihat di sambungan.** Pilihan, urut dari yang terbaik: (a) tidak dipotong (biarkan jeda atau kata pengisinya);
   (b) sambungan tertutup visual layar penuh yang MEMANG menggambarkan kalimat di situ, sudah penuh di layar sebelum potongan dan
   masih ada sesudahnya; (c) sambungan jatuh di pergantian yang memang terlihat sebagai pergantian (pindah tempat, pindah bagian
   dengan judul); (d) sambungan terbuka dengan alasan tertulis (`cut_ok`). Visual yang dipasang hanya untuk menutup potongan, tanpa
   hubungan dengan kalimatnya, adalah hiasan dan ditolak: kalau tidak ada visual yang cocok di situ, kurangi potongannya.
3. **Frame di kedua sisi.** Buka frame terakhir sebelum dan pertama sesudah potongan (contact sheet Tahap 1 atau `sheet.py`): kalau
   pembicara sedang bergerak, memegang benda, atau menoleh, geser potongan ke tempat ia diam.

Hitung dan tulis: jumlah potongan, satu potongan per berapa detik, dan berapa yang terbuka. Sebagai pembanding (bukan kuota): di atas
kira-kira satu potongan per 15 dtk untuk pembicara yang lancar, periksa lagi alasan tiap potongan. Menukar durasi dengan aliran itu
wajar: video 58 dtk yang mengalir lebih baik daripada 52 dtk yang patah-patah.

**Gate:** hook di 3 detik pertama. Uji sambungan lolos di setiap pergantian segmen. Durasi perkiraan masuk target brief. Setiap bagian yang dibuang punya alasan. Satu take dasar dipilih; setiap potongan punya alasan, rencana gambar di sambungannya, dan frame kedua sisinya sudah dilihat. Pertanyaan naskah sudah dikirim ke lead.

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
- **Koreksi butuh bukti, bukan tebakan** (job02: Whisper menulis "Juli pasir", worker menggantinya dengan "dulu di Parcelin"; transkrip ulang hanya mendengar "dulu"). Mengganti salah dengar hanya boleh kalau (a) bunyinya cocok dan jumlah suku katanya muat di rentang waktu kata itu, dan (b) potongan audio kata itu (±0,3 dtk) ditranskrip ulang **tanpa prompt kosakata** dan hasilnya mendukung. Nama brand, orang, angka, dan harga tidak pernah ditulis atas dasar "kalimatnya jadi masuk akal". Kalau tidak ada yang cocok: kosongkan kata itu (`""`) dan laporkan indeks katanya ke lead sebagai "tidak terverifikasi". Kata yang hilang dari subtitle adalah cacat kecil; kata yang tidak diucapkan adalah cacat besar.
- **Daftar koreksi di laporan**: setiap entri `text`/`script` yang mengubah BUNYI kata (bukan hanya ejaan, tanda baca, `*`, atau `""`) dilaporkan sebagai "Whisper: … → subtitle: … (bukti: …)". Lead memeriksa daftar ini.
- **Kata di tepi potongan**: kata terakhir sebelum `out` dan kata pertama setelah `in` hanya diberi subtitle kalau envelope menunjukkan kata itu utuh di dalam segmen. Waktu Whisper di tepi kalimat sering terlambat 0,1 sampai 0,2 dtk.
- **Cara menguji satu kata** (dipakai di job02): potong audio sumber di sekitar kata itu dengan konteks ±0,3 dtk, transkrip pada kecepatan normal tanpa prompt kosakata (beam 5 dan beam 1), dan sekali lagi dengan batas potong digeser. Kecepatan 0,7x hanya pendapat kedua karena sering berhalusinasi di awal dan akhir potongan ("Tunggu", "Sampai jumpa di video selanjutnya"). Run dengan prompt kosakata bukan bukti untuk sebuah nama. Hal yang sama dipakai untuk kata tambahan di sambungan: kalau transkrip ulang file final mendengar kata yang tidak ada di subtitle, anggap kata itu terdengar sampai potongan audio membuktikan sebaliknya.
- **Kata penting**: beri awalan `*`. Kata bertanda tampil di baris besar dengan font dan warna penekanan dari `theme`. Pilih 1 sampai 2 kata per kalimat, dan hanya kata yang membawa makna: angka, nama, kata kunci topik, kata yang ditekan pembicara. Kalau semua ditandai, tidak ada yang menonjol.
- **Kata yang disembunyikan**: isi `""` di `text`, atau `_` di `script`, untuk kata tersendat yang masih terdengar tapi tidak perlu dibaca.
- **Waktu kata yang salah**: kalau subtitle muncul terlalu cepat atau lambat dibanding suaranya (biasanya kata pertama setelah potongan), betulkan waktunya di `timing` berdasarkan envelope.
- **Huruf besar**: subtitle ditampilkan huruf kecil semua kecuali kata yang diawali entri `keep_case` (nama brand, singkatan). Kalau user ingin huruf besar normal, ubah fungsi `clean` di `Main.tsx`.

Jalankan `python3 tools/build_timeline.py` dan baca seluruh daftar subtitle yang dicetak, dari atas ke bawah, sebagai penonton. Perhatikan juga setiap `WARNING`: kata yang separuhnya terpotong berarti titik potong atau `timing` perlu dibetulkan.

**Gate:** daftar subtitle terbaca sebagai naskah yang utuh. Tidak ada salah eja nama. Kata besar tidak lebih dari kira-kira satu per 2 sampai 3 detik.

### Tahap 6. Rencana visual dan aset

#### 6.1 Putuskan per kalimat

Jalankan rantai keputusan `visual-thinking.md` Bagian 2 untuk setiap kalimat naskah, lalu lintasan keseluruhan (2.2). Tulis
`work/visual_plan.md` dengan format 2.3. Peluang per situasi: Bagian 3. Yang bisa dijangkau dari sini: Bagian 4. Kapan memakai kode:
Bagian 5. Cara menyajikan, kapan memotong, posisi, timing, gerak: `visual-craft.md`. Apa yang kit bisa sekarang: `visual-craft.md` 9.

Mekanik yang berlaku untuk semua visual (keterbacaan, bukan gaya):
- Jangkar ke kata yang digambarkan, dengan offset sesuai cara masuknya (`visual-craft.md` 5). Insert kit masuk dengan fade 7 frame,
  jadi mulai sekitar 3 frame sebelum kata (offset `-3`) supaya sudah terlihat saat kata terdengar.
- Durasi tiap visual ≥ waktu baca atau waktu mengenali (resep `visual-craft.md` 5), dan berakhir saat topik kalimatnya selesai.
- Di antara dua insert yang tidak berantai, pembicara terlihat minimal 24 frame; kurang dari itu terlihat seperti kedipan. Kalau lebih
  pendek, rantaikan (jangkar yang sama untuk `end` insert pertama dan `start` insert kedua).
- Panel `split` dan overlay tidak dipakai bersamaan (keduanya memakai bagian atas layar).
- Angka di diagram berasal dari ucapan pembicara atau sumber yang bisa ditunjuk; angka ilustrasi ditandai "contoh".

#### 6.2 Kumpulkan aset

Urutan mencari: aset user → halaman publik asli lewat `shot.py` → Openverse → image generation lewat permintaan (`visual-thinking.md` 4).

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
2. Kalau tampilan aslinya terkunci login atau hanya ada di HP: minta rekaman layar atau screenshot ke user lewat lead (daftar "Butuh dari
   user", `visual-thinking.md` 4). Kode boleh menggerakkan screenshot asli itu (kursor, scroll, sorotan), tetapi tidak menggambar ulang
   aplikasinya. Selama menunggu: halaman publik lain dari brand yang sama, atau logo asli + nama akun di atas pembicara.
3. UI karangan (kartu bergaya dashboard, layar chat buatan sebagai bukti, ikon generik, latar dekoratif) tidak dipakai. Gelembung chat
   untuk menggambarkan apa yang DIUCAPKAN seseorang boleh: itu ilustrasi ucapan, bukan bukti.

**Foto dan footage stok, tanpa API key**

> Cloud: `stock.py photo`/`video` (Pexels) dan `stock.py commons` (Wikimedia) diblokir dari container ini; yang bisa dipakai di sini
> adalah `stock.py open` (Openverse). Perintah lain dipertahankan untuk lingkungan lain.

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
python3 tools/stock.py commons "TikTok logo" -n 6      # cloud: diblokir (HTTP 429). Logo dari situs resmi brand atau dari user
```

Logo berformat SVG diunduh sebagai PNG transparan (dan vektornya kalau server mengizinkan). Pakai logo resmi apa adanya: jangan digambar ulang, diwarnai ulang, atau diubah bentuknya. Logo dari user selalu didahulukan. Foto orang nyata hanya dari sumber seperti ini atau dari user, tidak dari image generation.

**Diagram SVG**: digambar sebagai komponen di `Visuals.tsx` (lihat 4.4). Bukan gambar diam, supaya garis dan batangnya bisa tumbuh mengikuti ucapan.

**Image generation (opsional)**: hanya untuk benda spesifik yang tidak ada foto aslinya, setelah aset nyata benar-benar dicari. Prompt gaya foto realistis, vertikal (1024x1536), tanpa teks di dalam gambar. Jangan dipakai untuk orang nyata, logo, tampilan aplikasi, atau bukti (berita, testimoni). Simpan di `video/public/gen/`.

- Codex: minta gambar langsung di percakapan atau sebut `$imagegen`, lalu simpan hasilnya ke `video/public/gen/<nama>.png`.
- Claude Code dan agent tanpa pembuat gambar: tulis daftar prompt di `work/gen_prompts.md`, minta user membuatnya di aplikasi lain dan menaruh filenya di `video/public/gen/`. Kalau user tidak mau menunggu, ganti dengan foto stok atau diagram.
- Buka setiap gambar hasilnya sebelum dipakai: tidak ada teks rusak, tangan aneh, atau benda yang salah.

**Efek suara**: empat efek di `video/public/sfx/` dibuat `tools/make_sfx.sh` dengan ffmpeg. Tidak perlu mengunduh apa pun. Situs efek suara gratis sering menolak unduhan otomatis (HTTP 403), jadi jangan bergantung padanya.

**Musik (wajib dipertimbangkan; syarat pemilik 13: "pastikan backsound sesuai dengan momen").** Setiap video diberi musik latar
kecuali user menolak atau isinya memang lebih kuat tanpa musik (tulis alasannya). Urutannya: lagu dari user kalau ada; kalau tidak,
lagu bebas royalti yang lisensinya mengizinkan pemakaian komersial di platform tujuan (catat judul, pembuat, URL, lisensi, dan
atribusi yang diminta); kalau tidak ada sumber yang bisa dijangkau dari container ini, laporkan ke lead dan jangan memakai lagu
berhak cipta. Memilih: tulis dulu nada tiap bagian naskah (pembuka, isi, belokan, ajakan), lalu pilih lagu yang nadanya cocok dengan
bagian terpanjang dan tidak melawan belokan. "Sesuai momen" berarti musik ikut berubah di belokan naskah: turun atau berhenti sesaat
di kalimat pembalik, naik lagi di ajakan, selesai bersama penutup (bukan terpotong). Kit sekarang hanya punya satu lagu dengan satu
volume dan fade di awal dan akhir (`edit-json.md`, `music`): perubahan per momen butuh komponen generik kecil (kebijakan kode) dan
dilaporkan ke lead. Agent tidak mendengar: periksa lagu dengan angka (durasi, kenyaringan, bagian yang berubah lewat envelope) dan
katakan di laporan bahwa rasa musiknya belum dinilai telinga. Aturan lama tetap: Taruh di `video/public/music/`, isi `music` di `edit.json`, volume 0,05 sampai 0,08 (jauh di bawah suara). Jangan mengunduh lagu berhak cipta.

**Gate:** setiap kalimat punya baris di `visual_plan.md` yang menjawab rantai keputusan (termasuk kalimat tanpa grafik, dengan alasan).
Setiap visual punya aset yang sudah dibuka dan dilihat, dan sumbernya terjangkau dari container (atau sudah diminta ke user, dengan cadangan
bertanda `ASUMSI`). Setiap visual buatan kode punya alasan satu kalimat. Kata jangkar dan durasi rencana tiap visual tertulis. Hasil lintasan
keseluruhan (2.2) tertulis.

### Tahap 7. Bangun timeline

Isi `events` di `work/edit.json` dari `visual_plan.md` (format di Bagian 4), lalu:

```bash
python3 tools/build_timeline.py
```

Baca laporannya setiap kali:

- `theme:` baris tampilan yang dipakai. Cek sama dengan keputusan di `work/brief.md`.
- `QUIET CHECK`: jumlah perubahan visual, rata-rata dan rentang terpanjang, porsi layar (penuh / split / pembicara + overlay / pembicara saja).
  Setiap `TOO QUIET` membuat build gagal: tambah visual yang menggambarkan kalimat di rentang itu, atau `quiet_ok` dengan alasan
  (`edit-json.md` 4.6). Bandingkan porsi dan kepadatan dengan `visual-thinking.md` 7; kalau jauh lebih jarang atau jauh lebih padat
  dari video sejenis, periksa ulang rencana dan tulis alasannya. Jangan menambah atau membuang visual hanya demi angka.
- Daftar event dengan durasi: cek tiap durasi terhadap resep waktu baca (`visual-craft.md` 5).
- `exposed jump cuts`: sambungan potongan yang terlihat. Di titik itu zoom otomatis berganti (punch-in). Kalau jumlahnya banyak dan berdekatan, pertimbangkan menutup sebagian dengan insert yang memang relevan, atau kurangi potongan.
- `WARNING` event lebih pendek dari 20 frame, atau pembicara hanya terlihat beberapa frame di antara dua insert: perbaiki jangkarnya.
- Error `full-screen events overlap`: dua insert bertabrakan. Geser salah satunya.
- Error `split ... overlaps`: panel `split` bertabrakan dengan insert atau panel lain. Buat bersentuhan (jangkar yang sama) atau pisahkan.
- `WARNING: overlay ... during split`: overlay dan panel sama-sama memakai bagian atas layar. Pindahkan salah satunya.

**Gate:** tidak ada error (termasuk `theme` dan QUIET CHECK) dan tidak ada warning yang belum dijelaskan. Setiap `quiet_ok` punya alasan yang juga tertulis di `visual_plan.md`.

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
- Satu sistem tampilan untuk elemen buatan sendiri; aset nyata tidak diwarnai ulang. Setiap logo dan tampilan aplikasi atau situs terlihat seperti aslinya.
- Posisi rapi: wajah tidak tertutup, tidak ada yang penting di zona antarmuka platform, elemen sejenis di zona dan margin yang sama, satu fokus per frame (`visual-craft.md` 4).
- Gerak: untuk setiap transisi atau gerak yang baru dibuat atau diubah, render still di frame berurutan (`node stills.mjs f f+1 f+2 ...` melintasi
  transisinya) dan jalankan enam cek halus `visual-craft.md` 6. Elemen sudah terbaca penuh saat katanya mulai.

Perbaiki, build, render still lagi. Ulangi sampai bersih. Jangan lanjut ke render penuh dengan still yang masih bermasalah.

**Gate:** setiap event punya minimal satu still yang sudah dilihat dan lolos. Uji diri `visual-thinking.md` Bagian 8 dijawab dengan bukti di `visual_plan.md`. Transisi baru lolos cek frame berurutan.

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
