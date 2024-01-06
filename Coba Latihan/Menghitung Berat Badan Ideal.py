# Program Menghitung Berat Badan Ideal
# I.S. : Tinggi badan (tinggi)
# F.S. : Menampilkan tinggi badan ideal (ideal)

# Input
tinggi = int(input("Masukan Tinggi Badan Anda : "))

# Proses
ideal = (tinggi - 100) - 1 / 100

# Output
print(f"Berat badan anda dengan tinggi {tinggi} Cm adalah {ideal} Kg")
