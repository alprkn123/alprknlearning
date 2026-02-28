#!/bin/bash

# Ini adalah komentar
echo "Hello, World!"

# Menampilkan tanggal dan waktu
echo "Sekarang jam: $(date)"

# Membuat variabel
nama="User"
echo "Halo $nama, selamat datang!"

# Conditional statement
if [ -f "file.txt" ]; then
    echo "File file.txt ditemukan"
else
    echo "File file.txt tidak ditemukan"
fi

# Looping
for i in {1..5}; do
    echo "Perulangan ke-$i"
done

# Fungsi sederhana
fungsi_sapa() {
    echo "Halo $1!"
}

fungsi_sapa "Budi"