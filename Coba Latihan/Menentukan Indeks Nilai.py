# Program Menentukan Indeks Nilai
# I.S. : Pengguna memasukan sebuah Nilai
# F.S. : Menampilkan indeks Nilai / Nilai Mutu

# Input
Nilai = int(input("Masukan Sebuah Nilai : "))

# Proses
if(Nilai >= 80) and (Nilai <= 100):
    Indeks = 'A'
elif(Nilai >= 70) and (Nilai <= 80):
    Indeks = 'B'
elif(Nilai >= 60) and (Nilai <= 70):
    Indeks = 'C'
elif(Nilai >= 50) and (Nilai <= 60):
    Indeks = 'D'
else:
    Indeks = 'E'

# Output
print("Indeks Nilai : ", Indeks)
