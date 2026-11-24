# Masalah dan perbaikannya

## A. Khusus cloud Editor Team (sudah teruji; menang atas tabel guide di bawah)

| Gejala | Penyebab | Perbaikan |
|---|---|---|
| Render macet: `delayRender() ... not cleared after 28000ms`, selalu setelah ±90 frame per tab | Web font (`@remotion/google-fonts`, `@remotion/fonts`, `FontFace`) membuat renderer Chrome hang di environment ini | Jangan pernah memuat web font. Font dipasang sebagai font SISTEM: taruh `.ttf/.otf` statis di `/home/user/editkit/fonts`, jalankan `bash /home/user/editkit/tools/install_fonts.sh`, cek `fc-list : family \| grep -i <nama>`, tulis nama family itu di `theme` pada `work/edit.json` (`edit-json.md` 4.5) |
| `stills.mjs`/render: `NetworkError` | Browser render tidak lewat proxy; ada aset/font yang diambil dari internet saat render | Semua aset harus file lokal di `video/public/`; font lihat baris di atas |
| `transcribe.py`: `open() got an unexpected keyword argument 'metadata_errors'` | PyAV ≥17 tidak cocok dengan faster-whisper 1.2.1 | `pip install "av<17"` di `/home/user/editkit/.venv` (sudah dikunci di `setup/install.sh`) |
| Playwright: `Executable doesn't exist` | Versi paket Python `playwright` tidak sama dengan browser bawaan di `/opt/pw-browsers` | Pasang versi yang sama dengan Node playwright global (dikerjakan `setup/install.sh`). JANGAN `playwright install` |
| `stock.py photo/video`: `nothing found` | Pexels menolak browser otomatis | Jangan ditembus. Pakai halaman resmi brand, `stock.py open` (Openverse), atau aset user |
| `stock.py commons`: `HTTP 429` terus-menerus | Wikimedia membatasi akses dari container ini | Jangan ditembus. Logo dari situs resmi brand / user |
| `yt-dlp`: `Sign in to confirm you're not a bot` | YouTube menolak tanpa login | Minta file mp4 ke user. Tanpa cookie, tanpa akal-akalan. Sambil menunggu, yang terbuka tanpa login: oEmbed (`https://www.youtube.com/oembed?url=<url>&format=json`: judul, kanal) dan `https://i.ytimg.com/vi/<id>/maxres{default,1,2,3}.jpg` (thumbnail + tiga frame asli 1280x720): cukup untuk elemen yang menetap (logo, timecode), tidak untuk animasi |
| Instagram/Pinterest menampilkan dinding login di `shot.py` | Halaman butuh login | Cari halaman publik lain (situs resmi, halaman pin, profil publik). Jangan login. Untuk tampilan IG/TikTok/aplikasi: minta screenshot atau rekaman layar ke user lewat lead (daftar "Butuh dari user"); jangan menggambar UI-nya dengan kode |
| `gdown: command not found` | venv belum aktif | `source .venv/bin/activate && gdown ...` |
| Satu frame hitam di hasil render | Glitch render Remotion (job01 v2) | Render ulang; `blackdetect` wajib di QA 1 |
| Subtitle telat/terlalu cepat >0,2 dtk di banyak kata | Waktu kata Whisper meleset (job01 v3) | Kerjakan QA 5 SEBELUM render penuh; betulkan lewat `timing` |
| `build_timeline.py`: `ERROR: work/edit.json has no "theme" block` atau `invalid "theme"` | Tampilan belum diputuskan, atau isinya salah | Isi blok `theme` (`edit-json.md` 4.5) dengan alasan di `why` |
| Still/render: `data.json has no "theme"` | `data.json` lama | Jalankan `python3 tools/build_timeline.py` |
| `build_timeline.py`: `stretch(es) longer than ...s with no visual change` | Rentang sepi terlalu panjang | Tambah visual yang menggambarkan kalimatnya, atau `quiet_ok` dengan alasan (`edit-json.md` 4.6). Bukan hiasan |
| Semua job melambat / RAM habis | Dua perintah berat jalan bersamaan | Selalu `flock /home/user/jobs/.heavy.lock ...`; render `CONCURRENCY=2` |
| `rm -rf` folder job ditolak pengaman | Folder kerja dilindungi | Laporkan ke lead; jangan diakali |

## B. Dari guide asli

| Gejala | Penyebab | Perbaikan |
|---|---|---|
| Video terasa flat walau banyak animasi | Visualnya hiasan, tidak menggambarkan kalimat | Ulangi rantai keputusan (`visual-thinking.md` Bagian 2). Setiap visual harus punya kata yang digambarkan dan, sebisanya, aset nyata |
| Visual muncul terlambat atau terlalu cepat | Frame diketik tangan, atau jangkar ke kata yang salah | Pakai jangkar kata. Cek indeks di `work/tx/*.txt`. Mulai 3 frame sebelum kata |
| Pembicara berkedip di antara dua insert | Ada celah beberapa frame | Rantaikan (jangkar sama) atau beri jarak minimal 24 frame |
| Zoom meloncat setelah insert hilang | Zoom berganti saat pembicara terlihat | Sudah ditangani `build_timeline.py`. Jangan menambah zoom manual |
| Kata terpotong atau dobel di sambungan | Potongan memakai waktu Whisper | Tahap 4 dengan envelope, lalu QA 4 |
| Bunyi klik di sambungan | Tidak ada fade audio | Fade 2 frame sudah ada di `Main.tsx`. Jangan dihapus |
| Benda tiba-tiba ada di tangan | Potongan di tengah gerakan | Geser potongan ke awal kalimat |
| Subtitle salah eja nama | Whisper salah dengar | `text` atau `script`, kosakata di `transcribe.py`, `keep_case` |
| Subtitle tidak pas dengan suara di awal segmen | Waktu kata pertama meleset | Betulkan di `timing` berdasarkan envelope |
| Wajah bergeser saat ganti klip | Framing antar klip berbeda | `framing` per klip, cek dengan still |
| Still gagal: file tidak ditemukan (404) | Aset belum ada di `video/public`, atau namanya berbeda dari yang ditulis di `edit.json` | Taruh filenya di `video/public`. Cek huruf besar kecil nama file |
| Bundler error `readFile` undefined | TypeScript terlalu baru | `npm i -D typescript@5.5.4` |
| Screenshot tertutup pop-up atau halaman login | Modal situs | `shot.py` sudah menghapus modal umum. Kalau masih, cari sumber publik lain. Jangan login |
| Foto stok tidak nyambung dengan omongan | Kata kunci pencarian terlalu abstrak | Cari bendanya secara konkret, lihat kandidat dengan `sheet.py assets` |
| Terlalu banyak potongan, terasa gelisah | Memotong setiap jeda kecil | Kembalikan jeda wajar. Gabungkan segmen yang hanya menghemat kurang dari 0,5 detik |
| Render sangat lama | Normal: beberapa menit sampai puluhan menit, tergantung CPU (Bagian 0.7) | Cek desain lewat still dulu, render penuh hanya saat still sudah bersih |
| `ModuleNotFoundError: faster_whisper` (atau `PIL`, `playwright`) | venv tidak aktif di shell itu | Awali perintah dengan `source .venv/bin/activate && ` |
| `error: externally-managed-environment` saat `pip install` | Memasang ke Python sistem | Pakai `.venv` (dibuat `tools/setup.sh`) |
| `npx: command not found`, atau Node di bawah 18 | Node belum terpasang atau terlalu lama | Pasang Node 20 (Bagian 0.2) |
| Unduhan gagal, `Could not resolve host`, model Whisper tidak terunduh | Shell agent tidak punya akses jaringan (bawaan Codex) | Nyalakan jaringan (Bagian 0.4), lalu `python3 tools/doctor.py` |
| Remotion: `Failed to launch the browser process`, `error while loading shared libraries` | Pustaka sistem untuk Chrome belum ada (Linux, WSL2) | Perintah pustaka di Bagian 0.2, butuh `sudo` dari user |
| Playwright: `Executable doesn't exist` | Chromium belum diunduh | `python3 -m playwright install chromium` |
| Render mati di tengah, `Killed`, atau komputer macet | RAM habis | `CONCURRENCY=2 bash tools/render.sh v1`, tutup aplikasi lain |
| Transkrip sangat lambat atau kehabisan RAM | Model besar di mesin kecil | `WHISPER_MODEL=medium`. Kalau ada GPU NVIDIA: `WHISPER_DEVICE=cuda WHISPER_COMPUTE=float16` |
| Teks tampil dengan font bawaan | Nama family di `theme` tidak sama dengan yang terpasang | Cloud: font hanya sebagai font sistem (lihat A); salin nama persis dari `fc-list : family` ke `theme` di `work/edit.json`. Jangan memuat font Google |
| `stock.py`: `nothing found`, atau Pexels menampilkan pemeriksaan bot | Kata kunci terlalu sempit, atau situs menolak browser otomatis | Kata kunci lain, `open` atau `commons`, atau minta user mengunduh. Jangan ditembus |
| Wikimedia `HTTP 429` | Mengunduh file asli atau ukuran thumbnail tidak standar | `stock.py commons` sudah memakai ukuran standar. Tunggu sebentar, kurangi `-n` |
| Situs efek suara atau musik menolak unduhan (`HTTP 403`) | Situs memblokir unduhan otomatis | Pakai `tools/make_sfx.sh`. Musik dari user |
| Video referensi tidak bisa diunduh | Diblokir wilayah, privat, atau butuh login | Minta file mp4 ke user. Jangan diakali |
| Warna pucat atau terlalu gelap setelah diunggah | File bukan `yuv420p` BT.709 | Kirim `out/final_vN.mp4` dari `render.sh`, bukan master. Cek QA 1 |
| Kepala terpotong panel, atau subtitle menutup dagu di layar terbagi | `shift` dan `h` tidak cocok dengan posisi wajah | Atur `shift` dan `h` event `split`, cek dengan still |
| Subtitle tidak terbaca di atas visual terang | Insert terang tanpa `light` | Tambah `"light": true` pada event itu |
| Kit hilang atau rusak sebagian | File terhapus atau terpotong | Salin atau ekstrak ulang kit (Bagian 2.3). `doctor.py` menyebut file yang hilang |
