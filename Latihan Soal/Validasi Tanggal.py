# Program Validasi Tanggal
# I.S. : Pengguna memasukan tanggal, bulan, tahun
# F.S. : Menampilkan hasil validitas tanggal

# Input
Tanggal = int(input("Tanggal : "))
Bulan = int(input("Bulan   : "))
Tahun = int(input("Tahun   : "))

# Proses
if(Bulan == 2 and Tanggal <= 29):
    if(Tahun % 4 == 0):
        Hasil = ("Adalah Tanggal Valid")
    else:
        Hasil = ("Bukan Tanggal Valid")

else:
    if(Bulan <= 12):
        if(Bulan == 1 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 2 and Tanggal <= 28):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 3 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 4 and Tanggal <= 30):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 5 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 6 and Tanggal <= 30):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 7 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 8 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 9 and Tanggal <= 30):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 10 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 11 and Tanggal <= 30):
            Hasil = ("Adalah Tanggal Valid")
        elif (Bulan == 12 and Tanggal <= 31):
            Hasil = ("Adalah Tanggal Valid")
        else :
            Hasil = ("Bukan Tanggal Valid")

# Output
print("Tanggal", Tanggal, "/", Bulan, "/", Tahun, " ", Hasil, sep="")
