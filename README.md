# KantinKu - Sistem Pemesanan Makanan Kantin Kampus

KantinKu adalah aplikasi pemesanan makanan kantin kampus berbasis Command-Line Interface (CLI) menggunakan Python. Aplikasi ini dirancang untuk membantu mahasiswa memesan makanan sebelum jam istirahat, melihat harga dan stok menu, menghitung total pembayaran, serta melacak status pesanan.

## Anggota Kelompok

| Nama Lengkap | NIM | GitHub |
|---|---|---|
| Sharim Azhar Siraz | 26110300013 | [@Rymz7](https://github.com/Rymz7) |
| Ali Akbar Alhamid | 26110300026 | [@aliakbar598](https://github.com/aliakbar598) |
| Raditya Nur Ancha | 26110300037 | [@Radityanurancha-119](https://github.com/Radityanurancha-119) |

## Deliverables

### D1 - Topik dan Pernyataan Masalah
Dokumen berisi deskripsi aplikasi, permasalahan utama, aktor, cakupan, dan batasan sistem.

[Dokumen D1](docs/profile/D1.%20Topik%20dan%20Pernyataan%20Masalah.md)

### D2 - Pembagian Modul
Dokumen berisi pembagian modul, tanggung jawab setiap modul, fitur, dan ketergantungan antar modul.

[Dokumen D2](docs/modules/D2-pembagian-modul.md)

### D3 - Use Case Diagram
Diagram yang menggambarkan aktor dan interaksi mereka dengan sistem KantinKu.

- [Source PlantUML D3](docs/diagram/D3-use-case-diagram.puml)
- [Gambar Use Case Diagram](docs/diagram/img/D3%20Use%20Case.png)

### D4 - Sequence Diagrams
Dokumentasi tiga skenario utama dan interaksi antar aktor serta modul sistem.

- [Skenario dan Penjelasan D4](docs/diagram/D4-skenario-sequence-diagram.md)
- [D4.1 - Mahasiswa Membuat Pesanan (PlantUML)](docs/diagram/D4-sequence-order.puml)
- [D4.1 - Gambar Sequence Diagram](docs/diagram/img/D4-sequence-order.png)
- [D4.2 - Penjual Memproses Pesanan (PlantUML)](docs/diagram/D4-sequence-seller-status.puml)
- [D4.2 - Gambar Sequence Diagram](docs/diagram/img/D4.2%20-%20Penjual%20Memproses%20Pesanan%20dan%20Memperbarui%20Status.png)
- [D4.3 - Pelacakan dan Penerimaan Pesanan (PlantUML)](docs/diagram/D4-sequence-receive-order.puml)
- [D4.3 - Gambar Sequence Diagram](docs/diagram/img/D4.3%20-%20Mahasiswa%20Melacak%20dan%20Menerima%20Pesanan.png)

### D5 - Kolaborasi dan Activity Log
Catatan kontribusi anggota kelompok, commit, dan Pull Request.

- [Activity Log](ACTIVITY_LOG.md)
- [Pull Requests](https://github.com/Rymz7/kantinku/pulls)

### D6 - Test Cases
Berisi minimal 10 test cases untuk satu skenario, terdiri dari 5 common cases dan 5 edge cases, beserta alasan pemilihan edge cases.

[Dokumen D6](docs/testing/D6-test-cases.md)

### D7 - Unit Testing
Berisi implementasi fungsi yang diuji, minimal 8 unit tests, dan bukti bahwa seluruh test berhasil dijalankan.

- [Unit Tests](tests/test_calculate_order_total.py)
- Hasil pengujian: screenshot akan ditambahkan setelah proses testing selesai.

> Catatan: tautan D6 dan D7 menggunakan lokasi file yang direncanakan. Pastikan file dibuat pada lokasi tersebut atau ubah tautannya sesuai lokasi file sebenarnya.

## Cara Menjalankan Tests

Pastikan Python sudah terpasang. Jalankan perintah berikut dari root repository.

1. Instal pytest:

   ```bash
   python -m pip install pytest
