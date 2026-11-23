# Profil brand: Parcelin (custom packaging)

Dibaca worker **hanya** untuk job brand ini (lead menyebut file ini di brief). Isinya fakta brand dan permintaan pemilik untuk video
brand ini. Bukan aturan untuk video lain.

## Nama dan ejaan
- Brand dikonfirmasi user (job01): **PARCELIN**. Penulisan di situs dan Pinterest: "Parcelin" / "Parcelin Company"; hashtag "#BikinDiParcelin".
  Di berita JPNN dan di akun video brand: "Parcelinpack". Di subtitle: "Parcelin" (masuk `keep_case`).
- Whisper large-v3 mendengarnya sebagai "Parcelon" / "Parcellen" / "parcel ini", walau diberi kosakata: perbaiki lewat `text`/`script`.

## Akun (dari screenshot profil yang dikirim user di job02, 2026-11-23)
- Video terbit di akun kreator **@prahenditaputri** (Prahendita Putri Prasetyani, terverifikasi; pembicara di footage). Bio akun itu
  menyebut: Packaging **@parcelinpack**, Pouch & Bag **@parcelinbag**, tautan prahenditaputri.carrd.co.
- Jadi akun brand packaging = **@parcelinpack** (tertulis di bio milik user sendiri). `@parcelincompany` dari footer situs tidak dipakai.
- Angka di profil (kiriman, pengikut) berubah terus: untuk penutup profil, **minta screenshot baru setiap job** (paling baik dari HP,
  potret). Screenshot job02 berukuran 1069x830 (desktop, mode gelap) dan terlalu kecil untuk teks tajam.

## Sumber yang sudah ditemukan (dicek 2026-11-22)
- Situs resmi: https://www.parcelin.id (bisa di-screenshot dengan `shot.py`; halaman kategori produk punya foto produk asli).
- Pinterest: https://id.pinterest.com/parcelincompany/ (publik; tab "Dibuat" = pin buatan brand sendiri dengan watermark dP). User mengizinkan
  memakai foto dari Pinterest brand ini. Pin terbaik dari job01 ada di container lama `jobs/job01/work/cand/pin/` (`SOURCES.txt` berisi URL);
  folder job tidak ada di repo, jadi unduh ulang dari URL kalau perlu.
- Logo: https://parcelin.id/parcelin-icon.png (logo "dP" di header situs), dipakai apa adanya.
- Bukti pihak ketiga: artikel JPNN "Parcelinpack Tingkatkan Daya Saing UMKM dengan Packaging Kreatif" (dipakai editor referensi; cari ulang URL-nya).
- Instagram: dinding login dari container ini. Untuk profil atau DM, minta screenshot/rekaman layar ke user.
- Hindari foto produk di situs yang nama filenya menunjukkan gambar AI ("Gemini_Generated_Image...").
- Produk yang dipegang pembicara di footage bisa milik klien brand: jangan dijadikan visual utama tanpa izin.

## Look yang pernah diputuskan (job01, bisa dipakai ulang setelah dicek)
- Warna penekanan: oranye tombol "Lihat Produk" di parcelin.id, diambil dari pixel screenshot (job01: `#DE6B17`). Panel hangat seperti
  kertas karton, teks gelap kecokelatan.
- Font: Poppins (font situs), file statis OFL, terpasang sebagai font sistem; kata besar tegak, bukan miring.
- Video referensi brand memakai dua look berbeda (kuning + serif miring, dan palet brand) dan user menerima keduanya: yang dinilai adalah
  ketepatan dan kepadatan visual, bukan warna.

## Permintaan pemilik untuk video brand ini (dari umpan balik job01 v4)
- Pertanyaan atau ucapan pelanggan di pembuka sebagai **gelembung chat kiri/kanan** di atas pembicara, dengan gambar kecil kotak yang ditanyakan.
- Beat **gelap/hitam-putih** pada punchline "gimana? nggak bisa".
- **Penutup untuk Instagram = profil @prahenditaputri** (job02, kata user: "output akhir untuk Instagram seperti ini, dirapikan,
  dianimasikan bebas, serapi mungkin"). Dikerjakan dengan komponen kit `igprofile`: avatar dan tile grid = crop asli screenshot, teks
  diketik ulang persis, tidak meniru tampilan aplikasi. Semua fakta harus sama dengan screenshot.
- Penutup Pinterest brand layar penuh (permintaan job01) tetap pilihan kalau user tidak memberi screenshot profil atau video terbit di tempat lain.
- Lebih banyak visual dan lebih jelas, gambar nyata yang bagus, animasi rapi, keputusan layar penuh vs tidak yang disengaja.
- Video brand ini adalah video jualan: ajakan ("DM aja") ditunjukkan di tempat nyatanya, lalu hasil kerja terbaik dengan logo/akun.

## Catatan aset (job02)
- Halaman produk "Hampers Idul Fitri" di parcelin.id memakai foto bernama "Gemini_Generated_Image…" dan teks "Lorem ipsum": jangan dipakai.
- Foto portofolio brand menampilkan produk klien (box JNE "Eid Mubarak" di Pinterest, box L'Oréal di hero situs, box kubah emas
  "Fleur Bites" di footage). Brand sendiri yang memajangnya, tetapi izin klien tidak bisa dicek dari sini: sebut di laporan ke user setiap kali dipakai.
- User (job02): aset boleh dicari di internet dan user tidak mengirim foto. Batas yang tetap: produk pihak lain tidak ditampilkan sebagai karya brand.
- Whisper di job02 menulis brand sebagai "Parcelin" (benar, dengan kosakata), "parseling", "Diparselin", "Parselen", dan sekali "Juli pasir"
  (kemungkinan "dulu, Parcelin"; tidak terverifikasi, dikosongkan di subtitle).
- Look job02: aksen kuning-emas `#F2C230` (hue box kubah emas di footage dan warna kata kunci di caption akun kreator), panel krem
  `#FBF6EA`, Poppins. Oranye brand ditolak di footage itu karena tenggelam di dinding merah.

## Riwayat
- job02 (Box Lebaran, pengingat pesan packaging Lebaran dari sekarang; 2 take naskah yang sama, 62,8 dtk dan 86,6 dtk): final 52,7 dtk.
- job01 (Cara Hitung Hardbox): final_v4 dinilai "rada kurang" (terlalu jarang, konsep tidak digambarkan, penutup lemah). Studi pembanding:
  `docs/reference-studies/parcelin-study.md`.
