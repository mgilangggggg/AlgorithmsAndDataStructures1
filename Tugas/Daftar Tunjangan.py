# Program Daftar Tunjangan
# I.S. : Memasukan data pegawai (Nama, Gol, Status, JumlahAnak, NIP)
# F.S. : Menampilkan daftar gaji pegawai (NIP, Nama, Gol, Status, GajiPokok, Tunjangan, JumlahAnak, PPN, GajiTotal)

# Input
Nama = str(input("Masukan Nama : "))
Gol = int(input("Masukan Golongan : "))
Status = str(input("Masukan Status : "))
JmlAnak = int(input("Jumlah Anak : "))
Nip = int(input("Masukan Nip : "))

# Proses
if (Gol == 1):
    Gapok = 1250000
    Tunjangan = Gapok + 0.1
elif (Gol == 2):
    Gapok = 1350000
    Tunjangan = Gapok + 0.125
elif (Gol == 3):
    Gapok = 1500000
    Tunjangan = Gapok + 0.15
elif (Gol == 4):
    Gapok = 1750000
    Tunjangan = Gapok + 0.2
else:
    print("Golongan Tidak Terdaftar")

while (JmlAnak <= 3):
    TunjanganAnak = JmlAnak * 150000
print()

    Gatot = Gapok + Tunjangan + TunjanganAnak
    Gatot = Gatot - 0.1
    Ppn = Gapok + Gatot

# Output
print("==================== Daftar Gaji Pegawai ====================\n")
print("Bulan/Tahun : Januari/2022")
print("Nip\t NamaPegawai\t Gol.\t GajiPokok\t Tunjangan\t Status\t JumlahAnak\t TunjanganAnak\t PPN\t GajiTotal")
print(f"{Nip}\t {Nama}\t {Gol}\t {Gapok}\t {Tunjangan}\t {Status}\t {JmlAnak}\t {TunjanganAnak}\t {Ppn}\t {Gatot}")
print("Jumlah Pegawai : \n"
      "Gaji Total Tertinggi : Rp.\t" ",atas nama : \n"
      "1. \n"
      "2. \n\n"
      "Gaji Total Terendah : Rp.\t" ",atas nama : \n"
      "1. \n"
      "2. \n")
