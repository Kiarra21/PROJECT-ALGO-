import csv
import os
from getpass import getpass
import sys


# ============================================================== Bagian Kiarra=====================================================================#
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
            print("login berhasil staff")
            # menu_fungsi_member()

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
            print("login berhasil pimpinan")
            # menu_fungsi_admin()

    if len(data_login) == 0:
        print("akun tidak ditemukan")
        input("Klik Enter Untuk Ulang...")
        menu_halaman_login()


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
            print("Terimakasih sudah menggunakan aplikasi kami.")
            sys.exit()
        elif pertanyaan == "n":
            print("Melanjutkan aplikasi.")
            menu_halaman_login()
        else:
            print("Masukkan pilihan yang tepat.")
    else:
        print("Masukkan Pilihan yang tepat")


# ============================================================== Bagian Kiarra=====================================================================#
menu_halaman_login()
