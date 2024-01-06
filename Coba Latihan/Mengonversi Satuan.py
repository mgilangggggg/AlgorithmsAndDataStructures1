# Program Mengonversi Satuan
# I.S. : Pengguna memasukan panjang benda dalam satuan meter (p)
# F.S. : Menampilkan konversi satuan (ks)

# Input
p = int(input("Masukan Panjang Benda : "))

# Proses
inchi = p * 39.37
kaki = p * 3.281
yard = p * 1.094

# Output
print(f"Konversi Satuan Panjang Sebuah Benda Dari Satuan Meter Kedalam Satuan Inchi Adalah 1 inchi = {inchi} mm, 1 kaki = {kaki}, 1 yard = {yard} m")
