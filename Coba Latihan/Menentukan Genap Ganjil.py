# Program Menentukan Genap Ganjil
#I.S. : User memasukan sebuah bilangan
#F.S. : Menampilkan  keterangan "Bilangan Genap" atau "Bilangan Ganjil"

# Input
Bilangan = int(input("Masukan Sebuah Bilangan : "))

# Proses
if(Bilangan % 2 == 0):
    Keterangan = ("Bilangan Ganjil")
else:
    Keterangan = ("Bilangan Genap")

# Output
print(Keterangan)
