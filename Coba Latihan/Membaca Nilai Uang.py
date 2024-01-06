# Program Membaca Nilai Uang
# I.S. : Pengguna memasukan nilai (uang)
# F.S. : Menampilkan hasil konversi (hasil)

# Input
uang = int(input("Masukan Nilai Uang : "))

# Proses
seribu = uang // 1000
sisaSeribu = uang % 1000
limaRatus = sisaSeribu // 500
sisaLimaRatus = sisaSeribu % 500
limaPuluh = sisaLimaRatus // 50
sisaLimaPuluh = sisaSeribu % 50
duaLima = sisaLimaPuluh // 25

# Output
print(f"Hasil : {seribu}, {limaRatus}, {limaPuluh}, {duaLima}")