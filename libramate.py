import csv
import pandas as pd
from tabulate import tabulate
import os
from getpass import getpass
import sys


# ============================================================== Bagian Kiarra=====================================================================#


# =================================Fitur registrasi Staff===============================#
def registrasi_staff():
    os.system("cls")
    username = input("masukkan username anda : ")
    password_check = False
    while password_check == False:
        password = getpass("masukkan password anda : ")
        password_confirm = getpass("konfirmasi password anda : ")
        if password != password_confirm:
            print("pasword tidak sesuai!")
            password_check = False
        elif password == password_confirm:
            password_check = True

    data_regis = []
    with open("file_csv/akun_staff.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    username_already = False

    for regis in data_regis:
        if username == regis["username"]:
            print("Username sudah ada mohon ganti dengan yang lain !")
            username_already = True
            enter = input("klik enter untuk melanjutkan...")
            print(enter, menu_halaman_login())

    if username_already == False:
        new_data = {"username": username, "password": password}
        with open("file_csv/akun_staff.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=new_data.keys())
            writer.writerow(new_data)

        print("Data berhasil ditambahkan!")
        enter = input("klik enter untuk melanjutkan...")
        print(enter, menu_halaman_login())


# =================================Fitur registrasi Staff===============================#

# =================================Fitur Login Staff dan Pimpinan===============================#


# login Staff
def login_staff():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = getpass("masukkan password anda : ")

    data_regis = []
    with open("file_csv/akun_staff.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            os.system("cls")
            print(f"Login berhasil!,halo {username}")
            input("Klik enter untuk melanjutkan...")
            menu_fitur_staff()

    if len(data_login) == 0:
        print("akun tidak ditemukan")
        input("Klik Enter Untuk Ulang...")
        menu_halaman_login()


# login Pimpinan
def login_pimpinan():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = getpass("masukkan password anda : ")

    data_regis = []
    with open("file_csv/akun_pimpinan.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            os.system("cls")
            print(f"Login berhasil!,halo {username}")
            input("Klik enter untuk melanjutkan...")
            menu_fitur_pimpinan()

    if len(data_login) == 0:
        print("akun tidak ditemukan")
        input("Klik Enter Untuk Ulang...")
        menu_halaman_login()


# =================================Fitur Login Staff dan Pimpinan===============================#


# =================================Fitur kelola Akun Staff===============================#
def menu_kelola_staff():
    print("1. Tambah Staff")
    print("2. Edit Staff")
    print("3. Hapus Staff")
    print("4. Kembali")
    memilih = input("pilih opsi : ")
    while True:
        if memilih == "1":
            username = input("masukan username:")
            password = input("masukan password:")
            tambah_staff(username, password)
            tampilkan_tabel_staff()
            break
        elif memilih == "2":
            username = input("Masukkan username yang ingin diedit: ")
            username_baru = input(
                "Masukkan username baru (tekan Enter jika tidak ingin mengubah): "
            )
            password_baru = input(
                "Masukkan password baru (tekan Enter jika tidak ingin mengubah): "
            )

            if username_baru == "":
                username_baru = None
            if password_baru == "":
                password_baru = None

            edit_staff(
                username, username_baru=username_baru, password_baru=password_baru
            )
            tampilkan_tabel_staff()
        elif memilih == "3":
            username = input("masukan username yang ingin dihapus:")
            hapus_staff(username)
            tampilkan_tabel_staff()
            break
        elif memilih == "4":
            menu_fitur_pimpinan()
        else:
            print("Opsi tidak ditemukan")
            input("Tekan Enter Untuk Mengulang...")
            tampilkan_tabel_staff()
            menu_kelola_staff()


def tampilkan_tabel_staff():
    os.system("cls")
    df = pd.read_csv("file_csv/akun_staff.csv")
    if not df.empty:
        # Menambah kolom 'Nomor' jika belum ada
        if "Nomor" not in df.columns:
            df.insert(0, "Nomor", range(1, len(df) + 1))
        print("Tabel Data Akun Staff:")
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
    else:
        print("Data staff kosong.")
    menu_kelola_staff()


# fungsi tambah data akun staff
def tambah_staff(username, password):
    os.system("cls")
    df = pd.read_csv("file_csv/akun_staff.csv")
    if username in df["username"].values:
        print(f"Username {username} sudah terdaftar. Masukkan username yang berbeda.")
        input("Klik enter untuk mengulang...")
        tampilkan_tabel_staff()
    else:
        staff_baru = pd.DataFrame({"username": [username], "password": [password]})
        df = pd.concat([df, staff_baru], ignore_index=True)
        df.to_csv("file_csv/akun_staff.csv", index=False)
        os.system("cls")
        print(f"Akun dengan username {username} berhasil ditambahkan.")
        input("Klik enter untuk melanjutkan...")


# fungsi edit data akun staff
def edit_staff(username, username_baru=None, password_baru=None):
    os.system("cls")
    df = pd.read_csv("file_csv/akun_staff.csv")

    if username not in df["username"].values:
        print(f"Username {username} tidak ditemukan.")
        input("Klik enter untuk kembali...")
        return

    if username_baru:
        if username_baru in df["username"].values:
            print(
                f"Username {username_baru} sudah terdaftar. Masukkan username yang berbeda."
            )
            input("Klik enter untuk mengulang...")
            return
        df.loc[df["username"] == username, "username"] = username_baru

    if password_baru:
        df.loc[df["username"] == (username_baru or username), "password"] = (
            password_baru
        )

    df.to_csv("file_csv/akun_staff.csv", index=False)
    os.system("cls")
    print(f"Akun dengan username {username} berhasil diedit.")
    input("Klik enter untuk melanjutkan...")


# fungsi hapus data akun staff
def hapus_staff(username):
    os.system("cls")
    df = pd.read_csv("file_csv/akun_staff.csv")
    if "username" in df.columns:
        df = df[df["username"] != username]
        df.to_csv("file_csv/akun_staff.csv", index=False)
        os.system("cls")
        print(f"Akun dengan username {username} berhasil dihapus.")
        input("Klik enter untuk melanjutkan...")
    else:
        print("Tidak ditemukan.")


# =================================Fitur kelola Akun Staff===============================#


# ============================================================== Bagian Kiarra=====================================================================#


# ============================================================== Bagian Lovya=====================================================================#
# =================================Fitur Kategori Buku===============================#
def tambah_kategori_buku():
    os.system("cls")
    nomor_kategori = input("Masukkan nomor kategori: ")
    nama_kategori = input("Masukkan nama kategori: ")

    if not os.path.exists("file_csv"):
        os.makedirs("file_csv")
    if not os.path.exists("file_csv/kategori_buku.csv"):
        pd.DataFrame(columns=["nomor_kategori", "nama_kategori"]).to_csv(
            "file_csv/kategori_buku.csv", index=False
        )

    df = pd.read_csv("file_csv/kategori_buku.csv")
    if nomor_kategori in df["nomor_kategori"].astype(str).values:
        print(f"Nomor kategori {nomor_kategori} sudah terdaftar.")
    else:
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    {
                        "nomor_kategori": [nomor_kategori],
                        "nama_kategori": [nama_kategori],
                    }
                ),
            ]
        )
        df.to_csv("file_csv/kategori_buku.csv", index=False)
        print(f"Kategori dengan nomor {nomor_kategori} berhasil ditambahkan.")


# Tampilkan tabel kategori buku
def tampilkan_kategori_buku():
    os.system("cls")
    if not os.path.exists("file_csv/kategori_buku.csv"):
        print("Data kategori buku kosong.")
        return

    df = pd.read_csv("file_csv/kategori_buku.csv")
    if not df.empty:
        print("Tabel Data Kategori Buku:")
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
    else:
        print("Data kategori buku kosong.")


def edit_kategori_buku():
    os.system("cls")
    if not os.path.exists("file_csv/kategori_buku.csv"):
        print("Data kategori buku tidak ditemukan.")
        return
    nomor_kategori = input("Masukkan nomor kategori yang ingin diedit: ")
    df = pd.read_csv("file_csv/kategori_buku.csv")
    if nomor_kategori not in df["nomor_kategori"].astype(str).values:
        print(f"Nomor kategori {nomor_kategori} tidak ditemukan.")
    else:
        nama_baru = input("Masukkan nama kategori baru: ")
        df.loc[df["nomor_kategori"].astype(str) == nomor_kategori, "nama_kategori"] = (
            nama_baru
        )
        df.to_csv("file_csv/kategori_buku.csv", index=False)
        print(f"Kategori dengan nomor {nomor_kategori} berhasil diperbarui.")


def hapus_kategori_buku():
    os.system("cls")
    if not os.path.exists("file_csv/kategori_buku.csv"):
        print("Data kategori buku tidak ditemukan.")
        return
    nomor_kategori = input("Masukkan nomor kategori yang ingin dihapus: ")
    df = pd.read_csv("file_csv/kategori_buku.csv")
    if nomor_kategori not in df["nomor_kategori"].astype(str).values:
        print(f"Nomor kategori {nomor_kategori} tidak ditemukan.")
    else:
        df = df[df["nomor_kategori"].astype(str) != nomor_kategori]
        df.to_csv("file_csv/kategori_buku.csv", index=False)
        print(f"Kategori dengan nomor {nomor_kategori} berhasil dihapus.")


# =================================Fitur Kategori Buku===============================#


# =================================Fitur Data Buku===============================#
def tampilkan_data_buku():
    os.system("cls")
    file_path = "file_csv/data_buku.csv"

    if not os.path.exists("file_csv"):
        os.makedirs("file_csv")
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        pd.DataFrame(
            columns=["nomor_buku", "nama_buku", "stock_buku", "nomor_kategori"]
        ).to_csv(file_path, index=False)

    df = pd.read_csv(file_path)
    if df.empty:
        print("Data buku kosong.")
    else:
        print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))


def tambah_data_buku():
    os.system("cls")
    file_path = "file_csv/data_buku.csv"

    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku: ")
    nama_buku = input("Masukkan nama buku: ")
    stock_buku = input("Masukkan stok buku: ")
    tampilkan_kategori_buku()
    nomor_kategori = input("Masukkan nomor kategori: ")

    if not os.path.exists("file_csv"):
        os.makedirs("file_csv")
    if not os.path.exists(file_path):
        pd.DataFrame(
            columns=["nomor_buku", "nama_buku", "stock_buku", "nomor_kategori"]
        ).to_csv(file_path, index=False)

    df = pd.read_csv(file_path)
    if nomor_buku in df["nomor_buku"].astype(str).values:
        print(f"Nomor buku {nomor_buku} sudah terdaftar.")
    else:
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    {
                        "nomor_buku": [nomor_buku],
                        "nama_buku": [nama_buku],
                        "stock_buku": [stock_buku],
                        "nomor_kategori": [nomor_kategori],
                    }
                ),
            ]
        )
        df.to_csv(file_path, index=False)
        print(f"Buku dengan nomor {nomor_buku} berhasil ditambahkan.")


def edit_data_buku():
    os.system("cls")
    file_path = "file_csv/data_buku.csv"

    if not os.path.exists(file_path):
        print("Data buku tidak ditemukan.")
        return

    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku yang ingin diedit: ")
    df = pd.read_csv(file_path)

    if nomor_buku not in df["nomor_buku"].astype(str).values:
        print(f"Nomor buku {nomor_buku} tidak ditemukan.")
    else:
        nama_baru = input("Masukkan nama buku baru (tekan Enter untuk skip): ").strip()
        stok_baru = input("Masukkan stok buku baru (tekan Enter untuk skip): ").strip()
        tampilkan_kategori_buku()
        kategori_baru = input(
            "Masukkan nomor kategori baru (tekan Enter untuk skip): "
        ).strip()

        if nama_baru:
            df.loc[df["nomor_buku"].astype(str) == nomor_buku, "nama_buku"] = nama_baru
        if stok_baru.isdigit():
            df.loc[df["nomor_buku"].astype(str) == nomor_buku, "stock_buku"] = stok_baru
        if kategori_baru.isdigit():
            df.loc[df["nomor_buku"].astype(str) == nomor_buku, "nomor_kategori"] = (
                kategori_baru
            )

        df.to_csv(file_path, index=False)
        print(f"Buku dengan nomor {nomor_buku} berhasil diperbarui.")


def hapus_data_buku():
    os.system("cls")
    file_path = "file_csv/data_buku.csv"

    if not os.path.exists(file_path):
        print("Data buku tidak ditemukan.")
        return

    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku yang ingin dihapus: ")
    df = pd.read_csv(file_path)

    if nomor_buku not in df["nomor_buku"].astype(str).values:
        print(f"Nomor buku {nomor_buku} tidak ditemukan.")
    else:
        df = df[df["nomor_buku"].astype(str) != nomor_buku]
        df.to_csv(file_path, index=False)
        print(f"Buku dengan nomor {nomor_buku} berhasil dihapus.")


# =================================Fitur Data Buku===============================#

# ============================================================== Bagian Lovya=====================================================================#


# ============================================================== Bagian Nazwa=====================================================================#


# =================================Fitur Peminjaman Include Pengembalian===============================#
# Fungsi untuk menampilkan catatan peminjaman
def tampilkan_catatan_peminjaman():
    os.system("cls")
    file_path = "file_csv/catatan_peminjaman.csv"
    if not os.path.exists(file_path):
        print("Data catatan peminjaman kosong.")
        return

    df = pd.read_csv(file_path)
    if df.empty:
        print("Data catatan peminjaman kosong.")
    else:
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# Fungsi untuk menambah catatan peminjaman
def tambah_catatan_peminjaman():
    os.system("cls")
    file_path = "file_csv/catatan_peminjaman.csv"

    # Pastikan file CSV tersedia dengan header
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        pd.DataFrame(
            columns=[
                "nomor_antrian",
                "nomor_buku",
                "tanggal_peminjaman",
                "tanggal_pengembalian",
                "status",
            ]
        ).to_csv(file_path, index=False)

    tampilkan_catatan_peminjaman()
    nomor_antrian = input("Masukkan nomor antrian: ")
    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
    tanggal_pengembalian = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
    status = input("Masukkan status peminjaman: ")

    df = pd.read_csv(file_path)
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                [
                    {
                        "nomor_antrian": nomor_antrian,
                        "nomor_buku": nomor_buku,
                        "tanggal_peminjaman": tanggal_peminjaman,
                        "tanggal_pengembalian": tanggal_pengembalian,
                        "status": status,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )
    df.to_csv(file_path, index=False)
    print(
        f"Catatan peminjaman untuk nomor antrian {nomor_antrian} berhasil ditambahkan."
    )
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk mengedit catatan peminjaman
def edit_catatan_peminjaman():
    os.system("cls")
    file_path = "file_csv/catatan_peminjaman.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Data catatan peminjaman kosong.")
        input("Tekan Enter untuk melanjutkan...")
        return

    tampilkan_catatan_peminjaman()
    nomor_antrian = input("Masukkan nomor antrian yang ingin diedit: ")

    df = pd.read_csv(file_path)
    if nomor_antrian not in df["nomor_antrian"].values:
        print(f"Nomor antrian {nomor_antrian} tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan...")
        return

    tampilkan_data_buku()
    nomor_buku = input(
        "Masukkan nomor buku baru (kosongkan jika tidak ingin mengubah): "
    )
    tanggal_peminjaman = input(
        "Masukkan tanggal peminjaman baru (kosongkan jika tidak ingin mengubah): "
    )
    tanggal_pengembalian = input(
        "Masukkan tanggal pengembalian baru (kosongkan jika tidak ingin mengubah): "
    )
    status = input("Masukkan status baru (kosongkan jika tidak ingin mengubah): ")

    if nomor_buku:
        df.loc[df["nomor_antrian"] == nomor_antrian, "nomor_buku"] = nomor_buku
    if tanggal_peminjaman:
        df.loc[df["nomor_antrian"] == nomor_antrian, "tanggal_peminjaman"] = (
            tanggal_peminjaman
        )
    if tanggal_pengembalian:
        df.loc[df["nomor_antrian"] == nomor_antrian, "tanggal_pengembalian"] = (
            tanggal_pengembalian
        )
    if status:
        df.loc[df["nomor_antrian"] == nomor_antrian, "status"] = status

    df.to_csv(file_path, index=False)
    print(f"Catatan peminjaman untuk nomor antrian {nomor_antrian} berhasil diedit.")
    input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menghapus catatan peminjaman
def hapus_catatan_peminjaman():
    os.system("cls")
    file_path = "file_csv/catatan_peminjaman.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Data catatan peminjaman kosong.")
        input("Tekan Enter untuk melanjutkan...")
        return

    tampilkan_catatan_peminjaman()
    nomor_antrian = input("Masukkan nomor antrian yang ingin dihapus: ")

    df = pd.read_csv(file_path)
    if nomor_antrian not in df["nomor_antrian"].values:
        print(f"Nomor antrian {nomor_antrian} tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan...")
        return

    df = df[df["nomor_antrian"] != nomor_antrian]
    df.to_csv(file_path, index=False)
    print(f"Catatan peminjaman untuk nomor antrian {nomor_antrian} berhasil dihapus.")
    input("Tekan Enter untuk melanjutkan...")


# =================================Fitur Peminjaman Include Pengembalian===============================#

# ============================================================== Bagian Nazwa=====================================================================#


# ============================================================== Bagian Wulan=====================================================================#
# =================================Fitur Pemasukkan Buku===============================#
# Fungsi Tambah Pemasukkan Stock Buku
def tambah_pemasukkan_stock():
    os.system("cls")
    tampilkan_pemasukkan_stock()
    nomor_pemasukkan = input("Masukkan nomor pemasukkan: ")
    tanggal_pemasukkan = input("Masukkan tanggal pemasukkan (YYYY-MM-DD): ")
    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku: ")
    stock_masuk = int(input("Masukkan jumlah stock yang masuk: "))
    keterangan = input("Masukkan keterangan: ")

    # Memastikan direktori dan file ada
    if not os.path.exists("file_csv"):
        os.makedirs("file_csv")

    file_path = "file_csv/pemasukkan_stock.csv"

    if not os.path.exists(file_path):
        # Membuat file baru dengan kolom-kolom yang benar jika belum ada
        pd.DataFrame(
            columns=[
                "nomor_pemasukkan",
                "tanggal_pemasukkan",
                "nomor_buku",
                "stock_masuk",
                "keterangan",
            ]
        ).to_csv(file_path, index=False)

    # Membaca data dari file CSV
    df = pd.read_csv(file_path)

    if nomor_pemasukkan in df["nomor_pemasukkan"].astype(str).values:
        print(f"Nomor pemasukkan {nomor_pemasukkan} sudah terdaftar.")
    else:
        # Menambahkan data baru ke DataFrame
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    {
                        "nomor_pemasukkan": [nomor_pemasukkan],
                        "tanggal_pemasukkan": [tanggal_pemasukkan],
                        "nomor_buku": [nomor_buku],
                        "stock_masuk": [stock_masuk],
                        "keterangan": [keterangan],
                    }
                ),
            ]
        )
        df.to_csv(file_path, index=False)
        print(
            f"Pemasukkan stock buku dengan nomor {nomor_pemasukkan} berhasil ditambahkan."
        )


# Fungsi Tampilkan Pemasukkan Stock Buku
def tampilkan_pemasukkan_stock():
    os.system("cls")

    # Memeriksa apakah file CSV ada dan tidak kosong
    file_path = "file_csv/pemasukkan_stock.csv"

    if not os.path.exists(file_path):
        print("File pemasukkan stock buku tidak ditemukan.")
        return

    # Membaca file CSV
    df = pd.read_csv(file_path)

    # Cek apakah data di file kosong
    if df.empty:
        print("Data pemasukkan stock buku kosong.")
    else:
        print("Tabel Data Pemasukkan Stock Buku:")
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# Fungsi Edit Pemasukkan Stock Buku
def edit_pemasukkan_stock():
    os.system("cls")
    if not os.path.exists("file_csv/pemasukkan_stock.csv"):
        print("Data pemasukkan stock buku tidak ditemukan.")
        return

    tampilkan_pemasukkan_stock()
    nomor_pemasukkan = input("Masukkan nomor pemasukkan yang ingin diedit: ")
    df = pd.read_csv("file_csv/pemasukkan_stock.csv")
    if nomor_pemasukkan not in df["nomor_pemasukkan"].astype(str).values:
        print(f"Nomor pemasukkan {nomor_pemasukkan} tidak ditemukan.")
    else:
        tanggal_pemasukkan = input("Masukkan tanggal pemasukkan baru (YYYY-MM-DD): ")
        tampilkan_data_buku()
        nomor_buku = input("Masukkan nomor buku baru: ")
        stock_masuk = int(input("Masukkan jumlah stock yang masuk baru: "))
        keterangan = input("Masukkan keterangan baru: ")
        df.loc[
            df["nomor_pemasukkan"].astype(str) == nomor_pemasukkan,
            [
                "tanggal_pemasukkan",
                "nomor_buku",
                "stock_masuk",
                "keterangan",
            ],
        ] = [tanggal_pemasukkan, nomor_buku, stock_masuk, keterangan]
        df.to_csv("file_csv/pemasukkan_stock.csv", index=False)
        print(
            f"Pemasukkan stock buku dengan nomor {nomor_pemasukkan} berhasil diperbarui."
        )


# Fungsi Hapus Pemasukkan Stock Buku
def hapus_pemasukkan_stock():
    os.system("cls")
    if not os.path.exists("file_csv/pemasukkan_stock.csv"):
        print("Data pemasukkan stock buku tidak ditemukan.")
        return

    tampilkan_pemasukkan_stock()
    nomor_pemasukkan = input("Masukkan nomor pemasukkan yang ingin dihapus: ")
    df = pd.read_csv("file_csv/pemasukkan_stock.csv")
    if nomor_pemasukkan not in df["nomor_pemasukkan"].astype(str).values:
        print(f"Nomor pemasukkan {nomor_pemasukkan} tidak ditemukan.")
    else:
        df = df[df["nomor_pemasukkan"].astype(str) != nomor_pemasukkan]
        df.to_csv("file_csv/pemasukkan_stock.csv", index=False)
        print(
            f"Pemasukkan stock buku dengan nomor {nomor_pemasukkan} berhasil dihapus."
        )


# =================================Fitur Pengurangan Buku===============================#
# Fungsi Pengurangan Stock Buku
def tambah_pengurangan_stock_buku():
    os.system("cls")
    tampilkan_pengurangan_stock()
    nomor_pengurangan = input("Masukkan nomor pengurangan: ")
    tanggal_pengurangan = input("Masukkan tanggal pengurangan (YYYY-MM-DD): ")
    tampilkan_data_buku()
    nomor_buku = input("Masukkan nomor buku: ")
    stock_pengurangan = int(input("Masukkan jumlah stock yang dikurangi: "))
    keterangan = input("Masukkan keterangan: ")

    # Memastikan direktori dan file ada
    if not os.path.exists("file_csv"):
        os.makedirs("file_csv")

    file_path = "file_csv/pengurangan_stock.csv"

    if not os.path.exists(file_path):
        # Membuat file baru dengan kolom-kolom yang benar jika belum ada
        pd.DataFrame(
            columns=[
                "nomor_pengurangan",
                "tanggal_pengurangan",
                "nomor_buku",
                "stock_pengurangan",
                "keterangan",
            ]
        ).to_csv(file_path, index=False)

    # Membaca data dari file CSV
    df = pd.read_csv(file_path)

    if nomor_pengurangan in df["nomor_pengurangan"].astype(str).values:
        print(f"Nomor pengurangan {nomor_pengurangan} sudah terdaftar.")
    else:
        # Menambahkan data baru ke DataFrame
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    {
                        "nomor_pengurangan": [nomor_pengurangan],
                        "tanggal_pengurangan": [tanggal_pengurangan],
                        "nomor_buku": [nomor_buku],
                        "stock_pengurangan": [stock_pengurangan],
                        "keterangan": [keterangan],
                    }
                ),
            ]
        )
        df.to_csv(file_path, index=False)
        print(
            f"Pengurangan stock buku dengan nomor {nomor_pengurangan} berhasil ditambahkan."
        )


# Fungsi Tampilkan Pengurangan Stock Buku
def tampilkan_pengurangan_stock():
    os.system("cls")

    # Memeriksa apakah file CSV ada dan tidak kosong
    file_path = "file_csv/pengurangan_stock.csv"

    if not os.path.exists(file_path):
        print("File pengurangan stock buku tidak ditemukan.")
        return

    # Membaca file CSV
    df = pd.read_csv(file_path)

    # Cek apakah data di file kosong
    if df.empty:
        print("Data pengurangan stock buku kosong.")
    else:
        print("Tabel Data Pengurangan Stock Buku:")
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# Fungsi Edit Pengurangan Stock Buku
def edit_pengurangan_stock():
    os.system("cls")
    if not os.path.exists("file_csv/pengurangan_stock.csv"):
        print("Data pengurangan stock buku tidak ditemukan.")
        return
    tampilkan_pengurangan_stock()
    nomor_pengurangan = input("Masukkan nomor pengurangan yang ingin diedit: ")
    df = pd.read_csv("file_csv/pengurangan_stock.csv")
    if nomor_pengurangan not in df["nomor_pengurangan"].astype(str).values:
        print(f"Nomor pengurangan {nomor_pengurangan} tidak ditemukan.")
    else:
        tanggal_pengurangan = input("Masukkan tanggal pengurangan baru (YYYY-MM-DD): ")
        tampilkan_data_buku()
        nomor_buku = input("Masukkan nomor buku baru: ")
        stock_pengurangan = int(input("Masukkan jumlah stock yang dikurangi baru: "))
        keterangan = input("Masukkan keterangan baru: ")
        df.loc[
            df["nomor_pengurangan"].astype(str) == nomor_pengurangan,
            [
                "tanggal_pengurangan",
                "nomor_buku",
                "stock_pengurangan",
                "keterangan",
            ],
        ] = [
            tanggal_pengurangan,
            nomor_buku,
            stock_pengurangan,
            keterangan,
        ]
        df.to_csv("file_csv/pengurangan_stock.csv", index=False)
        print(
            f"Pengurangan stock buku dengan nomor {nomor_pengurangan} berhasil diperbarui."
        )


# Fungsi Hapus Pengurangan Stock Buku
def hapus_pengurangan_stock():
    os.system("cls")
    if not os.path.exists("file_csv/pengurangan_stock.csv"):
        print("Data pengurangan stock buku tidak ditemukan.")
        return
    tampilkan_pengurangan_stock()
    nomor_pengurangan = input("Masukkan nomor pengurangan yang ingin dihapus: ")
    df = pd.read_csv("file_csv/pengurangan_stock.csv")
    if nomor_pengurangan not in df["nomor_pengurangan"].astype(str).values:
        print(f"Nomor pengurangan {nomor_pengurangan} tidak ditemukan.")
    else:
        df = df[df["nomor_pengurangan"].astype(str) != nomor_pengurangan]
        df.to_csv("file_csv/pengurangan_stock.csv", index=False)
        print(
            f"Pengurangan stock buku dengan nomor {nomor_pengurangan} berhasil dihapus."
        )


# ============================================================== Bagian Wulan=====================================================================#


# =================================Menu Login===============================#
def menu_halaman_login():
    os.system("cls")
    namafile = "file_txt/halaman_awal.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    opsi = int(input("masukkan pilihan : "))

    if opsi == 1:
        registrasi_staff()
    elif opsi == 2:
        login_staff()
    elif opsi == 3:
        login_pimpinan()
    elif opsi == 4:
        pertanyaan = input("apakah anda yakin untuk keluar aplikasi ? (y/n):")
        if pertanyaan == "y":
            os.system("cls")
            namafile = "file_txt/closing.txt"
            with open(namafile, "r") as file:
                isi_file = file.read()
                print(isi_file)
            sys.exit()
        elif pertanyaan == "n":
            print("Melanjutkan aplikasi.")
            menu_halaman_login()
        else:
            print("Masukkan pilihan yang tepat.")
    else:
        print("Masukkan Pilihan yang tepat")


# =================================Menu Login===============================#


# =================================Menu Fitur Staff===============================#
def menu_fitur_staff():
    os.system("cls")
    print("Halo Staff!")
    namafile = "file_txt/menu_fitur_staff.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih (1/2/3/4/5) : ")

        if memilih == "1":
            while True:
                tampilkan_data_buku()

                print("1. Tambah Data Buku")
                print("2. Edit Data Buku")
                print("3. Hapus Data Buku")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_data_buku()
                elif opsi == "2":
                    edit_data_buku()
                elif opsi == "3":
                    hapus_data_buku()
                elif opsi == "4":
                    menu_fitur_staff()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "2":
            while True:
                tampilkan_kategori_buku()

                print("1. Tambah Kategori")
                print("2. Edit Kategori")
                print("3. Hapus Kategori")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_kategori_buku()
                elif opsi == "2":
                    edit_kategori_buku()
                elif opsi == "3":
                    hapus_kategori_buku()
                elif opsi == "4":
                    menu_fitur_staff()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "3":
            while True:
                tampilkan_catatan_peminjaman()

                print("1. Tambah Peminjaman")
                print("2. Edit Peminjaman")
                print("3. Hapus Peminjaman")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_catatan_peminjaman()
                elif opsi == "2":
                    edit_catatan_peminjaman()
                elif opsi == "3":
                    hapus_catatan_peminjaman()
                elif opsi == "4":
                    menu_fitur_staff()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "4":
            menu_halaman_login()
        else:
            print("Mohon memilih opsi yang ada")


# =================================Menu Fitur Staff===============================#


# =================================Menu Fitur Pimpinan===============================#
def menu_fitur_pimpinan():
    os.system("cls")
    print("Halo Pimpinan!")
    namafile = "file_txt/menu_fitur_pimpinan.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih (1/2/3/4/5/6/7/8) : ")

        if memilih == "1":
            while True:
                tampilkan_data_buku()

                print("1. Tambah Data Buku")
                print("2. Edit Data Buku")
                print("3. Hapus Data Buku")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_data_buku()
                elif opsi == "2":
                    edit_data_buku()
                elif opsi == "3":
                    hapus_data_buku()
                elif opsi == "4":
                    menu_fitur_staff()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "2":
            while True:
                tampilkan_kategori_buku()

                print("1. Tambah Kategori")
                print("2. Edit Kategori")
                print("3. Hapus Kategori")
                print("4. kembali")
                opsi = input("Pilih (1/2/3/4) : ")
                if opsi == "1":
                    tambah_kategori_buku()
                elif opsi == "2":
                    edit_kategori_buku()
                elif opsi == "3":
                    hapus_kategori_buku()
                elif opsi == "4":
                    menu_fitur_pimpinan()
                else:
                    print("Masukkan Opsi Yang Tepat!")

        elif memilih == "3":
            while True:
                tampilkan_catatan_peminjaman()

                print("1. Tambah Peminjaman")
                print("2. Edit Peminjaman")
                print("3. Hapus Peminjaman")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_catatan_peminjaman()
                elif opsi == "2":
                    edit_catatan_peminjaman()
                elif opsi == "3":
                    hapus_catatan_peminjaman()
                elif opsi == "4":
                    menu_fitur_pimpinan()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "4":
            while True:
                tampilkan_pemasukkan_stock()

                print("1. Tambah Pemasukkan Buku")
                print("2. Edit Pemasukkan Buku")
                print("3. Hapus Pemasukkan Buku")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_pemasukkan_stock()
                elif opsi == "2":
                    edit_pemasukkan_stock()
                elif opsi == "3":
                    hapus_pemasukkan_stock()
                elif opsi == "4":
                    menu_fitur_pimpinan()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "5":
            while True:
                tampilkan_pengurangan_stock()

                print("1. Tambah Pengurangan Buku")
                print("2. Edit Pengurangan Buku")
                print("3. Hapus Pengurangan Buku")
                print("4. Kembali")
                opsi = input("Pilih (1/2/3/4) : ")

                if opsi == "1":
                    tambah_pengurangan_stock_buku()
                elif opsi == "2":
                    edit_pengurangan_stock()
                elif opsi == "3":
                    hapus_pengurangan_stock()
                elif opsi == "4":
                    menu_fitur_pimpinan()
                else:
                    print("Masukkan Opsi Yang Tepat!")
        elif memilih == "6":
            tampilkan_tabel_staff()
        elif memilih == "7":
            menu_halaman_login()
        else:
            print("Mohon memilih opsi yang ada")


# =================================Menu Fitur Pimpinan===============================#

menu_halaman_login()
