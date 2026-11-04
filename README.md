# Suara Rupiah: Detektor Nominal Uang untuk Tunanetra

Tugas Besar Kecerdasan Buatan, Kelompok 1.

Sistem yang mengenali nominal uang kertas Rupiah (Rp1.000 sampai Rp100.000) dari kamera atau foto, lalu mengucapkan nominalnya. Model YOLOv8n berjalan langsung di browser (ONNX Runtime Web), sehingga gambar tidak dikirim ke server.

## Fitur
- Deteksi langsung lewat kamera, dengan voting beberapa frame dan suara nominal
- Deteksi dari foto (boleh beberapa lembar)
- Dashboard riwayat deteksi dan unduhan CSV

## Hasil evaluasi
| Data | mAP50 |
|---|---|
| Validasi (foto kamera laptop dan dataset) | 0,981 |
| Uji dataset awal | 0,979 |

Hasil di atas diukur pada data uji. Pemakaian nyata dapat berbeda, terutama pada cahaya dan jarak uang. Belum diuji bersama pengguna tunanetra.

## Teknologi
Python, OpenCV, YOLOv8 (Ultralytics), PyTorch, ONNX Runtime Web.

## Struktur
- `index.html`: website (hero, layanan, upload, kamera, dashboard)
- `best_webcam.onnx`: model deteksi
- `kode/`: skrip aplikasi desktop dan pelatihan
