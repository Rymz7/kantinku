def proses_pesanan(data_menu, id_menu, jumlah_diminta):
    """
    Fungsi simpel untuk mengecek dan memotong stok berdasarkan menu yang dipilih.
    """
    item = data_menu[id_menu]
    stok_tersedia = item["stok"]

    if jumlah_diminta <= 0:
        return False, "Gagal: Jumlah pesanan minimal harus 1 porsi!"
    
    if jumlah_diminta <= stok_tersedia:
        # Jika stok cukup, potong stoknya
        data_menu[id_menu]["stok"] -= jumlah_diminta
        return True, f"Berhasil! Kamu memesan {jumlah_diminta} porsi {item['nama']}."
    else:
        # Jika stok tidak cukup, tolak pesanan
        return False, f"Gagal: Stok {item['nama']} tidak cukup! Kamu minta {jumlah_diminta}, tapi sisa stok cuma {stok_tersedia}."


def main():
    menu_kantin = {
        1: {"nama": "Nasi Goreng", "stok": 15},
        2: {"nama": "Ayam Geprek", "stok": 23},
        3: {"nama": "Kopi Hitam",  "stok": 5},
        4: {"nama": "Es Teh Manis", "stok": 0} 
    }
    
    print("=== SIMULASI TES LOGIKA STOK & MENU ===")
    
    while True:
        # Tampilkan menu dan stok terbaru
        print("\n--- DAFTAR MENU ---")
        for key, val in menu_kantin.items():
            print(f"{key}. {val['nama']} (Sisa Stok: {val['stok']})")
        print("0. Keluar")
        print("-" * 19)
        
        try:
            # 1. Pilih Menu
            pilih_menu = int(input("Pilih nomor menu yang mau dipesan (0 untuk keluar): "))
            
            if pilih_menu == 0:
                print("Keluar dari simulasi.")
                break
                
            if pilih_menu not in menu_kantin:
                print("Error: Nomor menu tidak ada di daftar!")
                continue
                
            if menu_kantin[pilih_menu]["stok"] == 0:
                print(f"Maaf, stok {menu_kantin[pilih_menu]['nama']} sudah habis total!")
                continue
            
            # 2. Masukkan Jumlah Porsi
            porsi = int(input(f"Berapa porsi {menu_kantin[pilih_menu]['nama']} yang mau dipesan?: "))
            
            # 3. Panggil fungsi proses pesanan
            status, pesan = proses_pesanan(menu_kantin, pilih_menu, porsi)
            
            # Tampilkan hasil berhasil/gagal
            print("\n" + pesan)
            
        except ValueError:
            print("\nError: Tolong masukkan angka, bukan huruf!")

if __name__ == "__main__":
    main()
