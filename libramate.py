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
        print("oke")
    elif opsi == 3:
        login_pimpinan()
        print("oke")
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
            print("Belum ada")
        elif memilih == "2":
            print("Belum ada")
        elif memilih == "3":
            print("Belum ada")
        elif memilih == "4":
            print("Belum ada")
        elif memilih == "5":
            menu_halaman_login()
        else:
            print("Mohon memilih opsi yang ada")


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
            print("Belum ada")
        elif memilih == "2":
            print("Belum ada")
        elif memilih == "3":
            print("Belum ada")
        elif memilih == "4":
            print("Belum ada")
        elif memilih == "5":
            menu_halaman_login()
        elif memilih == "6":
            print("belum ada")
        elif memilih == "7":
            tampilkan_tabel_staff()
        elif memilih == "8":
            menu_halaman_login()
        else:
            print("Mohon memilih opsi yang ada")


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
        print("Data member kosong.")
    menu_kelola_staff()


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
            tambah_member(username, password)
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

            edit_member(
                username, username_baru=username_baru, password_baru=password_baru
            )
            tampilkan_tabel_staff()
        elif memilih == "3":
            username = input("masukan username yang ingin dihapus:")
            hapus_member(username)
            tampilkan_tabel_staff()
            break
        elif memilih == "4":
            menu_fitur_pimpinan()
        else:
            print("Opsi tidak ditemukan")
            input("Tekan Enter Untuk Mengulang...")
            tampilkan_tabel_staff()
            menu_kelola_staff()


# fungsi tambah data akun staff
def tambah_member(username, password):
    os.system("cls")
    df = pd.read_csv("file_csv/akun_staff.csv")
    if username in df["username"].values:
        print(f"Username {username} sudah terdaftar. Masukkan username yang berbeda.")
        input("Klik enter untuk mengulang...")
        tampilkan_tabel_staff()
    else:
        new_member = pd.DataFrame({"username": [username], "password": [password]})
        df = pd.concat([df, new_member], ignore_index=True)
        df.to_csv("file_csv/akun_staff.csv", index=False)
        os.system("cls")
        print(f"Akun dengan username {username} berhasil ditambahkan.")
        input("Klik enter untuk melanjutkan...")


# fungsi edit data akun staff
def edit_member(username, username_baru=None, password_baru=None):
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
def hapus_member(username):
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

menu_halaman_login()
# ============================================================== Bagian Kiarra=====================================================================#
