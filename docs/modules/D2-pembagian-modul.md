
# D2. Pembagian Modul

KantinKu dibagi menjadi lima modul utama. Setiap modul memiliki tanggung jawab yang berbeda agar program lebih terstruktur, mudah dikembangkan, dan mudah diuji. Pembagian modul ini didasarkan pada fitur pemesanan makanan berbasis CLI (*Command-Line Interface*) yang dikembangkan menggunakan Python.

Pada implementasi saat ini, seluruh kode masih berada dalam satu file Python. Pembagian berikut merupakan pengelompokan tanggung jawab program secara konseptual, bukan berarti setiap modul sudah memiliki file Python tersendiri.

## 2.1 Modul Pemilihan Peran dan Navigasi

**Tanggung jawab:**

Mengatur alur navigasi program dan menentukan peran pengguna yang akan menggunakan sistem, yaitu mahasiswa atau penjual kantin.

**Fitur utama:**

- Menampilkan menu utama aplikasi.
- Memungkinkan pengguna memilih peran sebagai mahasiswa atau penjual kantin.
- Menampilkan menu sesuai dengan peran yang dipilih.
- Mengarahkan mahasiswa ke fitur katalog, pemesanan, dan pelacakan status pesanan.
- Mengarahkan penjual ke fitur pengelolaan pesanan.
- Memungkinkan pengguna kembali ke menu utama atau keluar dari aplikasi.

**Implementasi saat ini:**

Fitur ini dijalankan oleh fungsi `main()`, yang memanggil `menu_mahasiswa()` atau `menu_penjual()` berdasarkan pilihan pengguna.

Pemilihan peran belum menggunakan akun, kata sandi, atau autentikasi identitas pengguna.

## 2.2 Modul Katalog Menu

**Tanggung jawab:**

Menyimpan dan menampilkan informasi makanan serta minuman yang tersedia di kantin, termasuk nama menu, harga, dan jumlah stok. Informasi ini digunakan mahasiswa untuk menentukan makanan yang ingin dipesan.

**Fitur utama:**

- Menampilkan daftar menu makanan dan minuman.
- Menampilkan harga setiap menu.
- Menampilkan jumlah stok yang tersedia.
- Menampilkan status "HABIS" jika stok menu sudah tidak tersedia.
- Menyediakan informasi menu untuk proses pemesanan.

**Implementasi saat ini:**

Data menu disimpan dalam struktur data Python bernama `menu_kantin`. Fungsi `tampilkan_katalog()` digunakan untuk menampilkan daftar menu beserta harga dan stoknya.

Data menu sudah ditentukan di dalam kode. Penjual belum dapat menambahkan, mengubah, atau menghapus menu melalui program.

## 2.3 Modul Pemesanan dan Perhitungan Harga

**Tanggung jawab:**

Mengelola proses pemesanan makanan oleh mahasiswa, memvalidasi pilihan menu dan jumlah pesanan, menghitung total harga, serta menyimpan rincian pesanan yang berhasil dibuat.

**Fitur utama:**

- Memilih menu yang ingin dipesan.
- Menentukan jumlah porsi setiap menu.
- Memeriksa apakah nomor menu valid.
- Memastikan jumlah pesanan lebih besar dari nol.
- Memeriksa apakah stok mencukupi untuk jumlah pesanan.
- Menghitung subtotal setiap item berdasarkan jumlah dan harga satuan.
- Menghitung total harga seluruh item yang dipesan.
- Menampilkan struk berisi rincian item dan total harga.
- Memilih metode pembayaran berupa QRIS atau uang tunai.
- Memilih metode penerimaan pesanan, yaitu pengambilan langsung di kantin atau pengantaran ke kelas.
- Membuat ID pesanan secara otomatis.
- Menyimpan rincian pesanan, total harga, metode pembayaran, metode penerimaan, dan status awal pesanan.

**Implementasi saat ini:**

Sebagian besar proses pemesanan berada di dalam fungsi `menu_mahasiswa()`. Perhitungan subtotal dan total harga masih dilakukan langsung di dalam fungsi tersebut.

Fungsi `calculate_order_total()` belum dibuat secara terpisah. Fungsi ini dapat dikembangkan untuk mempermudah pengujian otomatis menggunakan `pytest` pada tahap pengujian kode.

Pembayaran QRIS saat ini masih berupa simulasi dan belum terhubung dengan penyedia pembayaran sungguhan.

Pilihan untuk mengambil pesanan langsung di kantin atau meminta pengantaran ke kelas juga belum tersedia di kode saat ini. Program masih selalu meminta lokasi atau lantai pengantaran. Fitur pemilihan metode penerimaan perlu ditambahkan agar implementasi sesuai dengan rancangan KantinKu.

## 2.4 Modul Pengelolaan Stok

**Tanggung jawab:**

Mengelola informasi jumlah stok setiap menu dan memastikan jumlah makanan yang dipesan tidak melebihi stok yang tersedia.

**Fitur utama:**

- Menyimpan jumlah stok awal setiap menu.
- Memeriksa apakah stok menu masih tersedia.
- Menampilkan pesan jika stok menu sudah habis.
- Memeriksa apakah jumlah pesanan positif dan tidak melebihi stok.
- Memeriksa total jumlah menu yang sama apabila mahasiswa memilih menu tersebut lebih dari sekali.
- Mengurangi stok setelah pesanan berhasil dicatat oleh sistem.
- Memastikan stok tidak menjadi negatif akibat pesanan yang tidak valid.

**Implementasi saat ini:**

Jumlah stok disimpan bersama informasi menu dalam struktur data `menu_kantin`. Program telah melakukan pemeriksaan awal terhadap ketersediaan stok dan jumlah porsi yang diminta.

Namun, kode saat ini masih mengurangi stok ketika mahasiswa menambahkan item ke keranjang. Pemeriksaan jumlah pesanan juga belum menolak angka nol atau negatif.

Perbaikan kode diperlukan agar jumlah pesanan wajib lebih besar dari nol dan stok baru dikurangi setelah pesanan berhasil dibuat. Jika proses pesanan gagal atau dibatalkan sebelum dicatat, stok tidak boleh berubah. Stok juga harus diperiksa terhadap total jumlah item yang sama dalam satu keranjang.

Penjual belum memiliki fitur untuk memperbarui stok secara manual melalui program.

## 2.5 Modul Pemenuhan dan Pelacakan Pesanan

**Tanggung jawab:**

Mengelola data pesanan yang masuk, membantu penjual memproses pesanan, serta memungkinkan mahasiswa memeriksa perkembangan pesanan berdasarkan ID pesanan.

**Fitur utama:**

- Menyimpan pesanan yang berhasil dibuat.
- Menampilkan daftar pesanan yang masuk kepada penjual.
- Menampilkan ID pesanan, rincian item, jumlah, lokasi pengantaran jika diperlukan, dan metode pembayaran.
- Menampilkan status awal pesanan.
- Memperbarui status pesanan menjadi "Sedang Disiapkan".
- Menandai pesanan sebagai "Siap Diambil" untuk pesanan yang diambil langsung di kantin.
- Memperbarui status menjadi "Sedang Diantar" untuk pesanan yang diantarkan ke kelas.
- Mengonfirmasi bahwa pesanan telah diterima mahasiswa.
- Mengubah status akhir pesanan menjadi "Selesai".
- Memungkinkan mahasiswa melacak status pesanan menggunakan ID pesanan.
- Menampilkan pesan jika ID pesanan tidak ditemukan.

**Implementasi saat ini:**

Data pesanan disimpan dalam struktur `pesanan_masuk`, dengan ID pesanan sebagai kunci. Fungsi `menu_penjual()` digunakan untuk melihat pesanan masuk dan memperbarui statusnya. Mahasiswa dapat menggunakan fitur pelacakan di dalam `menu_mahasiswa()` untuk melihat status pesanan.

Status yang tersedia pada kode saat ini adalah "Menunggu Konfirmasi Penjual", "Sedang Disiapkan", "Sedang Diantar", dan "Selesai (Sudah Diterima)".

Status "Siap Diambil" dan pilihan metode penerimaan pesanan perlu ditambahkan apabila KantinKu mendukung pengambilan langsung di kantin maupun pengantaran ke kelas.

## 2.6 Ketergantungan Antarmodul

| Modul | Bergantung pada | Alasan |
|---|---|---|
| Pemilihan Peran dan Navigasi | Tidak ada | Menjadi titik awal interaksi pengguna dengan program. |
| Katalog Menu | Tidak ada | Menyediakan data menu, harga, dan stok awal yang digunakan modul lain. |
| Pengelolaan Stok | Katalog Menu | Menggunakan informasi stok pada setiap menu untuk memeriksa dan memperbarui jumlah yang tersedia. |
| Pemesanan dan Perhitungan Harga | Katalog Menu dan Pengelolaan Stok | Menggunakan data menu dan hasil pemeriksaan stok untuk memvalidasi pesanan serta menghitung total harga. |
| Pemenuhan dan Pelacakan Pesanan | Pemesanan dan Perhitungan Harga | Menggunakan data pesanan yang telah dicatat untuk menampilkan rincian pesanan dan memperbarui statusnya. |

Ketergantungan tersebut menunjukkan alur penggunaan data antarmodul. Pengelolaan Stok menyediakan pemeriksaan dan pembaruan stok, sedangkan Pemesanan menggunakan fungsi tersebut tanpa perlu mengatur seluruh mekanisme penyimpanan stok secara langsung.

## 2.7 Alur Kerja Utama yang Dirancang

1. Pengguna memilih peran mahasiswa atau penjual kantin melalui menu utama.
2. Mahasiswa melihat katalog untuk memeriksa nama menu, harga, dan stok.
3. Mahasiswa memilih menu dan jumlah porsi. Sistem memvalidasi pilihan menu, memastikan jumlah pesanan positif, dan memeriksa ketersediaan stok.
4. Sistem menghitung subtotal setiap item dan total harga seluruh pesanan, kemudian menampilkan struk.
5. Mahasiswa memilih metode penerimaan, yaitu mengambil pesanan di kantin atau menerima pengantaran ke kelas. Jika memilih pengantaran, mahasiswa memasukkan lokasi atau lantai tujuan.
6. Mahasiswa memilih metode pembayaran berupa QRIS atau uang tunai. QRIS pada implementasi saat ini masih berupa simulasi.
7. Setelah pesanan berhasil dicatat, sistem menyimpan rincian pesanan dan memberikan ID pesanan kepada mahasiswa. Stok diperbarui setelah pesanan berhasil dibuat.
8. Penjual melihat pesanan masuk dan memperbarui status sesuai dengan proses penyiapan, pengambilan, atau pengantaran.
9. Mahasiswa memasukkan ID pesanan untuk memeriksa status terbaru.

Modul Pemesanan dan Perhitungan Harga menjadi bagian utama dalam proses transaksi. Modul Pengelolaan Stok mendukung validasi jumlah pesanan, sedangkan Modul Pemenuhan dan Pelacakan Pesanan mengelola proses setelah pesanan dicatat hingga selesai diterima mahasiswa.

Dokumentasi ini membedakan fitur yang sudah tersedia dalam kode dari fitur yang masih perlu dikembangkan. Deskripsi implementasi perlu diperbarui apabila program mengalami perubahan.

## Catatan Implementasi

Kode KantinKu saat ini merupakan implementasi awal berbasis CLI.
Beberapa fitur dalam rancangan, seperti pilihan pengambilan
pesanan di kantin atau pengantaran ke kelas, masih perlu
dikembangkan. Pembayaran QRIS yang tersedia juga masih berupa
simulasi. Fitur-fitur tersebut menjadi bagian dari rancangan
sistem dan perlu disesuaikan dengan implementasi sebelum
proyek diselesaikan.
