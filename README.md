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

Catatan kontribusi anggota kelompok serta tautan ke riwayat Pull Request.

- [Activity Log](ACTIVITY_LOG.md)
- [Pull Requests](https://github.com/Rymz7/kantinku/pulls)

<!-- TAMBAHKAN BAGIAN D6 - TEST CASES DI SINI SETELAH FILE D6 SUDAH ADA. -->
### D7 - Unit-Tested Code (1 Function)

Implementasi dan pengujian 1 fungsi menggunakan kerangka kerja `pytest`. Pengujian berfokus pada logika validasi dan pemotongan ketersediaan stok menu pesanan kantin, mencakup skenario berhasil dan gagal.

- [Source Code Fungsi (`src/stock.py`)](src/stock.py)
- [Source Code Unit Test (`src/test_stok.py`)](src/test_stok.py)
- [Screenshot Hasil Pengujian (Passed)](src/IMG/hasil_test_stock.png)

**Cara Menjalankan Test:**
Pastikan module `pytest` sudah terinstal di lingkungan Python Anda. Buka terminal di direktori utama (root) proyek ini, lalu jalankan perintah berikut:

```bash
pytest src/test_stock.py -v
