import json
import os

DATA_FILE = "data_keuangan.json"

def muat_data ();
    if not os.path.exists(DATA_FILE):
        return {"pemasukan": [], "pengeluaran": []}
   try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
   except json.JSONDecodeError:
       return {"pemasukan": [], "pengeluaran": []}

def simpan_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def tambah_transaksi(tipe, jumlah, kategori, keterangan):
    data = muat_data()
    transaksi = {
        "jumlah": float(jumlah), 
        "kategori": kattegori,
        "keterangan": keterangan
    }
    if tipe == "1":
        data["pemasukan"].append(transaksi)
        print("\n pemasukan berasil ditambahkan!")
    elif tipe == "2":
        data["pengeluaran"].append(transaksi)
        print("\n pengeluaran berhasil ditambahan!")
    simpan_data(data)

def lihat_ringkasan():
    data = muat_data()
    total_pemasukan = sum(item["jumlah"] for item in data["pemasukan"])
    total_pengeluaran  = sum(item["jumlah"] for item in data["pengeluaran"])
    saldo = total_pemasukan - total_pengeluaran

    print("\n" + "="*30)
    print("      RINNGKASAN KEUANGAN     ")
    print("="*30)
    print(f"Total Pemasukan  : Rp {total_pemasukan:,.2f}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:,.2f}")
    print(f"Sisa Saldo       : Rp {saldo:,.2f}")
    print("="*30)
