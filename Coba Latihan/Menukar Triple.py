# MenukarkanTriple
# I.S. : Pengguna memasukan 3 buah bilangan bulat (x,y,z)
# F.S. : Menampilkan pertukaran bilangan bulat (Bertukar)

x = int(input("Masukan Bilangan x : "))
y = int(input("Masukan Bilangan y : "))
z = int(input("Masukan Bilangan z : "))

print(f"Nilai Sebelum Bertukar x = {x}, y = {y}, z = {z}")

a = x
x = y
y = z
z = a

print(f"Nilai Sesudah Bertukar x = {x}, y = {y}, z = {z}")
