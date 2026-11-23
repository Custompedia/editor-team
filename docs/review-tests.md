# Tes review untuk LEAD (sebelum meneruskan hasil worker)

Diturunkan dari dua editor acuan (`docs/reference-studies/BENCHMARK_NOTES.md` bagian 6, `parcelin-study.md`) dan dipetakan ke 11 syarat
pemilik (2026-11-23). **M** = bisa dicek dari laporan build / file; **J** = penilaian lead di contact sheet, still, atau strip.
Tidak ada tes warna, font, atau bentuk: look diputuskan per video. Angka kepadatan dan porsi layar adalah **pembanding**, bukan syarat lulus,
kecuali batas rentang sepi (syarat pemilik, dijaga kit).

Bahan yang diminta dari worker: `work/visual_plan.md` (dengan uji diri terjawab), log `build_timeline.py` (baris `theme:`, `QUIET CHECK`,
daftar event + durasi), `work/qa_stills.jpg`, strip transisi, `final_vN.mp4`. Lead membuat contact sheet sendiri (`tools/sheet.py video <final> <scratch>/lead 2`).

Syarat pemilik: 1 kapan visual · 2 kapan memotong · 3 posisi rapi · 4 layar penuh atau tidak · 5 visual cocok · 6 tidak pernah lama sepi ·
7 aset nyata dulu · 8 gerak halus dan pas · 9 timing dipahami · 10 momen dipakai kreatif · 11 tidak terlalu jarang dan tidak terlalu ramai.

## Tes urut menurut pentingnya

| # | Pertanyaan | Lulus bila | Cara cek | Jenis | Syarat |
|---|---|---|---|---|---|
| T1 | Rentang terpanjang tanpa perubahan gambar? | QUIET CHECK lolos (bawaan `max_quiet_s` 6 dtk); setiap `quiet_ok` punya alasan yang benar (pendapat, cerita, emosi), bukan "aset tidak ada" | Log build | M | 6 |
| T2 | Rentang terpanjang tanpa elemen apa pun selain caption? | ≤ sekitar 7 dtk; setiap rentang > sekitar 4 dtk punya alasan tertulis | Log build + contact sheet | M/J | 6, 1 |
| T3 | Tutup caption: tiap visual memperlihatkan hal yang sedang diucapkan? | Semua; footage "suasana" hanya untuk konsep tanpa wujud, jarang | Still per visual | J | 5 |
| T4 | Tiap visual mulai di kata yang digambarkannya? | Jangkar di `edit.json` menunjuk kata itu; still di jangkar menunjukkan visual sudah terbaca | `edit.json` + still | M/J | 5, 9 |
| T5 | Tiap kalimat punya keputusan tertulis (visual apa / kenapa tanpa visual)? | Semua kalimat di `visual_plan.md`; setiap klaim, angka, nama punya visual atau alasan | `visual_plan.md` | J | 1 |
| T6 | Wajah (mata sampai mulut) pernah tertutup overlay atau caption? | Tidak pernah | Contact sheet | J | 3 |
| T7 | Elemen di zona aman, margin dan perataan konsisten? | Tidak ada yang penting di seperlima bawah layar atau kolom kanan bawah; elemen sejenis di tempat yang sama | Contact sheet | J | 3 |
| T8 | Satu fokus per frame? | Paling banyak satu blok baca + caption di setiap still | Contact sheet | J | 3, 11 |
| T9 | Potongan berita: sumber asli terlihat, kalimat yang diucapkan disorot saat diucapkan, hanya baris yang perlu, terbaca di HP? | Semua ya. (Kartu kit punya bingkai dan bayangan: bukan alasan gagal; label "SUMBER" buatan boleh dikosongkan) | Still | J | 5, 3, 7 |
| T10 | Pilihan layar penuh / panel / overlay / pembicara saja punya alasan ("dibaca / dikenali / dirasakan dari wajah")? | Semua baris visual_plan | `visual_plan.md` | J | 4 |
| T11 | Ada potongan audio di tengah kalimat? | Tidak ada (QA 4 `verify_audio`: kata utuh di setiap sambungan) | Log QA 4 | M | 2 |
| T12 | Gambar diam > sekitar 5 dtk tanpa gerak di dalamnya, atau visual lebih pendek dari waktu bacanya? | Tidak ada; durasi ≥ max(frasa, 0,5 dtk + N kata disorot ÷ 3,5) | Daftar event + durasi di log build | M | 9, 6 |
| T13 | Caption sinkron, terbaca di semua latar, nama benar, tidak dobel dengan judul? | QA 5 lolos; terbaca di setiap still | Still + log QA 5 | J | 3 |
| T14 | Belokan nada ditandai di kalimat pembaliknya, dan tidak di banyak tempat? | Ada di belokan utama; lebih dari tiga kali hanya di video komedi | `visual_plan.md` + contact sheet | J | 2, 10 |
| T15 | Pembuka: frame pertama sudah menyebut topik/bukti, perubahan kedua cepat menyusul? | Ya | Contact sheet detik 0–4 | M/J | 6, 10 |
| T16 | Onset: fade/blur sudah penuh saat kata mulai; masuk langsung 0 sampai +5 frame; subjek klausa boleh di awal klausa | Semua, pengecualian tertulis | Still di frame jangkar | M/J | 9 |
| T17 | Durasi: berakhir saat topiknya selesai, tidak menyeberang ke kalimat lain | Semua | Log build + `visual_plan.md` | M/J | 9 |
| T18 | Gerak halus di strip frame berurutan (enam cek `visual-craft.md` 6), satu kosakata gerak dengan arti tetap | Semua transisi lulus; tidak ada frame sisa, kedip, atau loncatan | Strip QA 3 | J | 8 |
| T19 | Aset nyata dulu: tiap visual buatan punya alasan "tidak ada aset nyata yang bisa memperlihatkan ini"; sumber + lisensi tercatat; tidak ada UI/artikel palsu sebagai bukti | Semua | `visual_plan.md` | J | 7, 10 |
| T20 | Tidak terlalu ramai: tiap elemen lulus "kalau dihapus, apa yang hilang?"; kepadatan tidak jauh di atas sekitar satu perubahan bermakna per 2 dtk tanpa alasan | Lulus; lead mempertanyakan bila jauh di luar video sejenis (`visual-thinking.md` 7) | Log build + contact sheet | J/M | 11 |

## Tambahan dari syarat pemilik yang tidak tercakup T1–T20
| # | Pertanyaan | Lulus bila | Syarat |
|---|---|---|---|
| T21 | Ucapan orang lain (pelanggan, komentar) terbedakan dari suara pembicara, dan momen lain dipakai (nama → bendanya, daftar → bertambah)? | Ya, atau alasan tertulis | 10 |
| T22 | Look diputuskan dengan alasan dari brand/footage/nada (baris `theme:` di log sama dengan `work/brief.md`)? | Ya | 3 (kerapian), preferensi user |
| T23 | Daftar "Butuh dari user" dilaporkan di Tahap 0, dan cadangannya jujur (bukan versi palsu, bukan visual yang dikecilkan)? | Ya | 7 |
| T24 | Setiap koreksi subtitle yang mengubah bunyi kata punya bukti? | Lead membandingkan `text`/`script` di `edit.json` dengan `work/tx/*.json` dan dengan transkrip ulang final di log QA 4: tidak ada nama, angka, atau kata yang ditulis padahal kedua transkrip mendengar hal lain; tidak ada kata di tepi potongan yang tampil tetapi terpotong dari audio | akurasi (job02) |

Cara cepat T24 dan sambungan (lead, tanpa mendengar): cetak kata transkrip sumber di sekitar setiap `in`/`out` dan setiap koreksi, lalu
envelope 20 ms dari `work/tx/<klip>.wav` di rentang itu. Blok nyaring = suku kata; hitung apakah teks subtitle muat. Transkrip ulang final
yang berbeda dari subtitle (kata tambahan di sambungan, kata hilang) selalu ditanyakan ke worker, bukan diabaikan.

**Tolak** edit yang lolos QA teknis tetapi gagal T1, T3, T5, T19, T24, atau yang terasa jarang di contact sheet (job01 v4: 16 dtk tanpa perubahan).
Saat menolak, sebut nomor tes dan frame/baris rencananya, supaya revisi hanya menyentuh itu.
