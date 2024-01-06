# Mengonversi Jarak Semut
# {I.S.  : Pengguna memasukan jarak dalam satuan centimeter}
# {F.S. : Menampilkan konversi jarak}

# Input
jarak = int(input("Masukan Jarak Anda : "))

# Proses
km = jarak // 100000
sisajarak = jarak % 100000
m = sisajarak // 100
cm = sisajarak % 100

# Output
print(f"Jadi Semut Menempuh Jarak Sejauh {km} km + {m} m + {cm} cm")
