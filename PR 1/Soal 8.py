import math

# Input populasi
populasi = int(input("Masukkan banyaknya populasi --> "))
toilet_baru = math.ceil(populasi//3)

# Output
magnitude = 13*14*toilet_baru
biaya = toilet_baru*150
print(f"Banyaknya air yang dihemat : {magnitude} liter per hari")
print(f"Biaya total pemasangan toilet baru : ${biaya}")
