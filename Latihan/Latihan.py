# Membuat dictionary daftar kontak
daftar_kontak = {
    'Ari': '081234567',
    'Dina': '082345678',
    'Rudi': '083456789'
}

# Tampilkan kontak Ari
print("Kontak Ari:", daftar_kontak.get('Ari'))

# Tampilkan semua kontak
print("Semua Kontak:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Tambah kontak baru Riko
daftar_kontak['Riko'] = '087654544'
print("\nSetelah menambahkan Riko:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Ubah kontak Dina dengan nomor baru
daftar_kontak['Dina'] = '088999776'
print("\nSetelah mengubah nomor Dina:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Tampilkan daftar Nama dan nomornya
print("\nDaftar Nama dan Nomor:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Hapus kontak Dina
del daftar_kontak['Dina']
print("\nSetelah menghapus kontak Dina:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")
