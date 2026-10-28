# --- 1. Fungsi Utama yang akan diuji ---
def proses_pesanan(data_menu, id_menu, jumlah_diminta):
    item = data_menu[id_menu]
    stok_tersedia = item["stok"]

    if jumlah_diminta <= 0:
        return False, "Gagal: Jumlah pesanan minimal harus 1 porsi!"
    
    if jumlah_diminta <= stok_tersedia:
        data_menu[id_menu]["stok"] -= jumlah_diminta
        stok_terbaru = data_menu[id_menu]["stok"]
        return True, f"Berhasil! Kamu memesan {jumlah_diminta} porsi {item['nama']}. Stok telah diperbarui (sisa: {stok_terbaru})."
    else:
        return False, f"Gagal: Stok {item['nama']} tidak cukup! Kamu minta {jumlah_diminta}, tapi sisa stok cuma {stok_tersedia}."


# --- 2. Skenario Pengujian (Unit Test) ---
def test_pesanan_sukses():
    menu_test = {1: {"nama": "Nasi Goreng", "stok": 15}}
    
    # Memesan 2 porsi Nasi Goreng
    status, pesan = proses_pesanan(menu_test, 1, 2)
    
    assert status is True
    assert menu_test[1]["stok"] == 13 # Memastikan stok berkurang jadi 13
    assert "Stok telah diperbarui" in pesan # Memastikan teks info stok telah diperbarui ada di pesan

def test_pesanan_gagal_karena_stok_kurang():
    menu_test = {3: {"nama": "Kopi Hitam", "stok": 5}}
    
    # Memesan 10 porsi Kopi Hitam padahal stok cuma 5
    status, pesan = proses_pesanan(menu_test, 3, 10)
    
    assert status is False
    assert menu_test[3]["stok"] == 5 # Memastikan stok tetap 5 (tidak terpotong)
