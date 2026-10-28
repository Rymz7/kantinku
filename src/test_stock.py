# Tambahkan fungsi ini agar bisa dibaca oleh pytest
def test_pesanan_sukses():
    menu_test = {1: {"nama": "Nasi Goreng", "stok": 15}}
    # Memesan 2 porsi Nasi Goreng
    status, pesan = proses_pesanan(menu_test, 1, 2)
    
    assert status is True
    assert menu_test[1]["stok"] == 13 # Memastikan stok berkurang jadi 13

def test_pesanan_gagal_karena_stok_kurang():
    menu_test = {3: {"nama": "Kopi Hitam", "stok": 5}}
    # Memesan 10 porsi Kopi Hitam padahal stok cuma 5
    status, pesan = proses_pesanan(menu_test, 3, 10)
    
    assert status is False
    assert menu_test[3]["stok"] == 5 # Memastikan stok tetap 5 (tidak terpotong)
