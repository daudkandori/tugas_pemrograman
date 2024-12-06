from datetime import datetime
import csv

#isi gudang sekarang
inventaris = {
    1: {"nama": "Mouse", "stok": 0, "harga": 50000},
    2: {"nama": "Keyboard", "stok": 0, "harga": 150000},
    3: {"nama": "Monitor", "stok": 0, "harga": 1200000},
}

#laporan barang yg so ta jual
laporan_penjualan = []

#buat show semua inventaris
def tampilkan_inventaris():
    print("\n--- Daftar Inventaris ---")
    for id_barang, info in inventaris.items():
        print(f"ID: {id_barang}, Nama: {info['nama']}, Stok: {info['stok']}, Harga: Rp{info['harga']:,}")

#kse tambah krg stock
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

#peringatan for stock renda
def peringatan_stok_rendah():
    batas = int(input("Masukkan batas minimum stok: "))
    print("Barang dengan stok rendah:")
    for id_barang, info in inventaris.items():
        if info["stok"] < batas:
            print(f"- {info['nama']} (ID: {id_barang}), Stok: {info['stok']}")

#ITONG TOTAL NILAI BARANG YG ADAAAAAAAAAAAA
def hitung_total_nilai():
    total_nilai = sum(info["stok"] * info["harga"] for info in inventaris.values())
    print(f"Total nilai inventaris: Rp{total_nilai:,}")

#list catat penjualan
def catat_penjualan():
    try:
        id_barang = int(input("Masukkan ID barang: "))
        if id_barang in inventaris:
            jumlah = int(input("Masukkan jumlah barang terjual: "))
            if jumlah > inventaris[id_barang]["stok"]:
                print("Stok tidak mencukupi untuk penjualan!")
            else:
                harga_total = jumlah * inventaris[id_barang]["harga"]
                inventaris[id_barang]["stok"] -= jumlah
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                laporan_penjualan.append({"waktu": waktu, "id_barang": id_barang, "nama": inventaris[id_barang]["nama"], "jumlah": jumlah, "total": harga_total})
                print(f"Penjualan berhasil dicatat! Total pendapatan: Rp{harga_total:,}")
#kalo barang nd ada
        else:
            print("Barang tidak ditemukan!")
#kalo error
    except ValueError:
        print("Input tidak valid, harap masukkan angka.")

#simpang data tabel pake csv
def ekspor_data():
    filename = "inventaris.csv"
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Stok", "Harga"])
            for id_barang, info in inventaris.items():
                writer.writerow([id_barang, info["nama"], info["stok"], info["harga"]])
        print(f"Data berhasil diekspor ke {filename}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengekspor data: {e}")

#tampilan menu
while True:
    print("\n--- Sistem Inventaris ---")
    print("1. Tampilkan Daftar Barang")
    print("2. Tambah/Kurangi Stok")
    print("3. Peringatan Stok Rendah")
    print("4. Hitung Total Nilai Barang")
    print("5. Catat Penjualan")
    print("6. Ekspor Data")
    print("7. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_inventaris()
    elif pilihan == "2":
        ubah_stok()
    elif pilihan == "3":
        peringatan_stok_rendah()
    elif pilihan == "4":
        hitung_total_nilai()
    elif pilihan == "5":
        catat_penjualan()
    elif pilihan == "6":
        ekspor_data()
    elif pilihan == "7":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
