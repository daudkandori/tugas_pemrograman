# Import library untuk date and time
from datetime import datetime

# Data inventaris awal (contoh)
inventaris = {
    101: {"nama": "Mouse", "stok": 10, "harga": 50000},
    102: {"nama": "Keyboard", "stok": 5, "harga": 150000},
    103: {"nama": "Monitor", "stok": 2, "harga": 1200000},
}

# Fungsi untuk menambah/kurangi stok
def ubah_stok():
    try:
        id_barang = int(input("Masukkan ID barang: "))
        if id_barang in inventaris:
            jumlah = int(input("Masukkan jumlah (positif untuk tambah, negatif untuk kurangi): "))
            if inventaris[id_barang]["stok"] + jumlah < 0:
                print("Stok tidak mencukupi!")
            else:
                inventaris[id_barang]["stok"] += jumlah
                print(f"Stok berhasil diupdate. Stok baru {inventaris[id_barang]['stok']} unit.")
        else:
            print("Barang tidak ditemukan!")
    except ValueError:
        print("Input tidak valid, harap masukkan angka.")

# Fungsi untuk menampilkan peringatan stok rendah
def peringatan_stok_rendah():
    batas = int(input("Masukkan batas minimum stok: "))
    print("Barang dengan stok rendah:")
    for id_barang, info in inventaris.items():
        if info["stok"] < batas:
            print(f"- {info['nama']} (ID: {id_barang}), Stok: {info['stok']}")

# Main program
while True:
    print("\n--- Sistem Inventaris ---")
    print("1. Tambah/Kurangi Stok")
    print("2. Peringatan Stok Rendah")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        ubah_stok()
    elif pilihan == "2":
        peringatan_stok_rendah()
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
