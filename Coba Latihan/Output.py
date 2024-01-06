a = 12345
b = 378.901234
c = "Kota Bandung"
print(a)
print(b)
print(a, b, c)

print("a= ", a, ", b= ", b, ", c=", c, "\n")

# Menulis Print Banyak Objek
nama_lengkap = "Muhamad Gilang Abdul Gani"
panggilan = "Gilang"
tempat_lahir = "Ciamis"
umur = 22
print("Hai nama saya", nama_lengkap, "biasa dipanggil dengan \"", panggilan,
      "\"", "lahir di ", tempat_lahir, "dan sekarang saya berumur", umur, "tahun", "\n")

# Mengganti Pemisah Di Function Print
a = 5
b = 7
c = "Kota Bandung"
print(a, b, c, sep='-')
print(a, b, c, sep='' "\n")

# Mengganti Akhir Function Print
print("AAAAAA")
print("AAAAAA", end=".")
print("AAAAAA", end=".\n")
print("BBBBBB", end="")
print("Sarah", "Hasan", "Alica", "Idris", sep=", ", end="." "\n")

# Memformat String Menggunakan %
a = 123
b = 456.789
c = "Kota Bandung"
print("A berisi %i" % a)
print("B berisi %f dan C berisi %s" % (b, c), "\n")

# Contoh Tidak Menggunakan Padding
a = "Budi"
b = "Kurniawan"
c = "Ai"
print("[%s]" % a)
print("[%s]" % b)
print("[%s]" % c, "\n")

# Contoh Menggunakan Padding (15 spasi)
a = "Budi"
b = "Kurniawan"
c = "Ai"
print("[%15s]" % a)
print("[%15s]" % b)
print("[%15s]" % c)
print("[%-15s]" % a)
print("[%-15s]" % b)
print("[%-15s]" % c, "\n")

# Contoh Menggunakan Padding (10 spasi) pada data integer
a = 12500
b = 1000
c = 250000
d = 2500000
print("Rp. %10i" % a)
print("Rp. %10i" % b)
print("Rp. %10i" % c)
print("Rp. %10i" % d)
print("Rp. %010i" % a)
print("Rp. %+10i" % a, "\n")

# Contoh Menggunakan Padding (15 spasi) pada data float
a = 12345.67890
print("a:%f" % a)
print("a:%15f" % a)
print("a:%15.2f" % a)
print("a:%15.3f" % a)
print("a:%+15.3f" % a, "\n")

# Memformat String Menggunakan str.format(objects)
nama = "Gilang"
kota = "Ciamis"
umur = 22
print("Nama saya {}, tinggal di {}. Umur saya {}".format(nama, kota, umur), "\n")

# Contoh Mengakses Menggunakan Index
nama = "Gilang"
kota = "Ciamis"
umur = 22
print("Nama saya {0}, tinggal di {1}. Umur saya {2}".format(nama, kota, umur))
print("Nama saya {2}, tinggal di {0}. Umur saya {1}".format(
    nama, kota, umur), "\n")

# Contoh mengakses menggunakan nama
harga_barang_per_item = 5000
print("Harga : Rp. {hb}".format(hb=harga_barang_per_item), "\n")

# Contoh str.format dengan pengaturan alignment
nama = "Muhamad Gilang Abdul Gani"
print("[{:30}]".format(nama))
print("[{:<30}]".format(nama))
print("[{:>30}]".format(nama))
print("[{:^30}]".format(nama), "\n")

# Menformat String Dengan f-String
nama = "Gilang"
kota = "Ciamis"
umur = 22
print(f"Nama saya {nama}, tinggal di {kota}. Saya berumur {umur} tahun", "\n")

# f-String menggunakan format tambahan (dipisah dengan lambang : setelah nama variabel)
teks = "ABCDEFGH"
print(f"[{teks:<20}]")
print(f"[{teks:>20}]")
print(f"[{teks:^20}]")
a = 12345678
print(f"A:{a:15}")
b = 123456789.012345
print(f"B:{b:15.2f}", "\n")
