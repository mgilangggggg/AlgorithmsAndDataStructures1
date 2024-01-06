# Program Mengonversi Waktu Proyek
# I.S. : Pengguna memasukan jumlah (hari)
# F.S. : Menampilkan hasil konversi waktu (Kw)

# Input
hari = int(input("Masukan Hari : "))

# Proses
tahun = hari // 365
sisaHari = hari % 365
bulan = sisaHari // 30
hari = sisaHari % 30

# Output
print(f"Konversi Waktu Proyek Adalah : Tahun {tahun} Bulan {bulan} Hari {hari}")
