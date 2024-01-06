# Program Menghitung Jarak Hari
# I.S. : Pengguna memasukan dua buah tanggal (DD:MM:YY)
# F.S. : Menampilkan jarak kedua tanggal dalam bentuk tahun,bulan dan hari

# Input
DD1 = int(input("Masukan Hari Pertama  : "))
MM1 = int(input("Masukan Bulan Pertama : "))
YY1 = int(input("Masukan Tahun Pertama : "))
DD2 = int(input("Masukan Hari Kedua    : "))
MM2 = int(input("Masukan Bulan Kedua   : "))
YY2 = int(input("Masukan Tahun Kedua   : "))

# Proses
Hari = (DD2 - DD1) + (MM2 - MM1) * 30 + (YY2 - YY1) * 365

Tahun = Hari // 365
Sisa = Hari % 365
Bulan = Sisa // 30
Hari = Sisa % 30

# Output
print("Jarak Kedua Tanggal   :", Tahun, "Tahun", Bulan, "Bulan", Hari, "Hari")
