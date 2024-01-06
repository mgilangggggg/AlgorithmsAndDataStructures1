# Program Keterangan Lulus
# I.S. : Nilai diinputkan user, harus antara 0 s/d 100
# F.S. : Keterangan kelulusan ditampilkan

nilai = 0
while nilai >= 0 or nilai <= 100:
    nilai = int(input("Nilai : "))
    if nilai >= 45:
        print("Lulus")
    else:
        print("Tidak Lulus")
