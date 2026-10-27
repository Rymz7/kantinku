# D4. Sequence Diagrams

Bagian ini menjelaskan tiga skenario utama KantinKu dalam bentuk sequence diagram. Diagram menunjukkan interaksi antara aktor, antarmuka CLI, modul sistem, dan penyimpanan data berdasarkan pembagian modul pada D2 dan use case pada D3.

> **Catatan:** Diagram berikut menggambarkan rancangan alur sistem. Beberapa fitur, seperti pilihan ambil sendiri atau pengantaran ke kelas, validasi perubahan status, dan konfirmasi penerimaan, belum sepenuhnya tersedia pada kode saat ini. Pembayaran QRIS masih berupa simulasi.

## 4.1 Mahasiswa Membuat Pesanan

**Skenario:** Mahasiswa melihat katalog, memilih menu dan jumlah, lalu sistem memeriksa ketersediaan stok dan menghitung total harga. Setelah mahasiswa memilih metode penerimaan dan pembayaran, sistem menyimpan pesanan, memperbarui stok, dan menampilkan ID pesanan.

**Alasan penting:** Ini adalah alur utama KantinKu karena menghubungkan katalog, validasi stok, perhitungan harga, pembayaran, dan pencatatan pesanan. Diagram ini juga memperjelas bahwa stok seharusnya dikurangi setelah pesanan berhasil dicatat.

**Diagram:** [D4-sequence-order.puml](../diagram/D4-sequence-order.puml)

## 4.2 Penjual Memproses Pesanan dan Memperbarui Status

**Skenario:** Penjual melihat daftar pesanan masuk, memilih ID pesanan, lalu mengubah status sesuai tahap pemenuhan dan metode penerimaan. Sistem memvalidasi ID serta status sebelum menyimpan perubahan.

**Alasan penting:** Status yang benar membantu penjual mengetahui pesanan yang harus diproses dan memberi mahasiswa informasi mengenai perkembangan pesanannya. Validasi juga mencegah perubahan status untuk ID yang tidak ditemukan atau status yang tidak sesuai.

**Diagram:** [D4-sequence-seller-status.puml](../diagram/D4-sequence-seller-status.puml)

## 4.3 Mahasiswa Melacak dan Menerima Pesanan

**Skenario:** Mahasiswa memasukkan ID pesanan untuk melihat status dan metode penerimaannya. Jika pesanan siap diambil atau sedang diantar, proses penyerahan dilanjutkan dan penjual memperbarui status menjadi selesai. Jika ID tidak ditemukan atau pesanan belum siap, sistem menampilkan informasi yang sesuai.

**Alasan penting:** Pelacakan menghubungkan pencatatan pesanan dengan proses penerimaan makanan, baik melalui pengambilan di kantin maupun pengantaran ke kelas. Skenario ini juga mencakup kondisi ketika pesanan belum siap atau ID yang dimasukkan tidak valid.

**Diagram:** [D4-sequence-receive-order.puml](../diagram/D4-sequence-receive-order.puml)

## 4.4 Pembagian Tanggung Jawab

Setiap anggota kelompok bertanggung jawab atas satu sequence diagram. Pembagian tugas harus sesuai dengan pekerjaan yang benar-benar dilakukan oleh setiap anggota.

Setiap anggota perlu mencatat nama, aktivitas, waktu pengerjaan, serta tautan commit atau Pull Request pada file `ACTIVITY_LOG.md`.
