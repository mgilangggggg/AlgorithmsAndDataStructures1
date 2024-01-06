# Program Seleksi Pemilu
# I.S. : Pengguna memasukan umur dan status pernikahan
# F.S. : Menampilkan boleh memilih atau tidak

# Input
Umur = int(input("Masukan Umur : "))

# Proses
if(Umur < 17):
    Menikah = input("Menikah[Y/T] : ").upper()
    if(Menikah == "Y"):
        # Output
        print("Anda Boleh Ikut Pemilu")
    else:
        # Output
        print("Anda Belum Bisa Ikut Pemilu")
else:
    # Output
    print("Anda Boleh Ikut Pemilu")
