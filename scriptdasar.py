#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Menampilkan output
print("Hello, World!")

# Variabel dan tipe data
nama = "Budi"
umur = 25
tinggi = 175.5
menikah = False

print(f"Nama: {nama}, Umur: {umur}, Tinggi: {tinggi}")

# Input dari user
nama_user = input("Siapa nama Anda? ")
print(f"Halo {nama_user}, selamat datang!")

# Conditional
if umur >= 17:
    print("Sudah bisa membuat KTP")
else:
    print("Belum bisa membuat KTP")

# Looping
for i in range(5):
    print(f"Perulangan ke-{i+1}")

# List
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(f"Saya suka {item}")

# Dictionary
siswa = {
    "nama": "Ani",
    "kelas": "10A",
    "nilai": 90
}
print(f"{siswa['nama']} mendapat nilai {siswa['nilai']}")