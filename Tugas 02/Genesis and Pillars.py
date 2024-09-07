# Input banyak pilar
jarak = list(map(int, input("Masukkan tinggi pilar : ").split()))

# Nilai lompat maksimum di pilar paling awal
lompat = jarak[0]

# Mencari jarak terjauh
maks = max(jarak)

# Cek apakah bisa melompati pilar terjauh
if lompat>=maks:
    print("YES HE CAN")
else:
    print("NO HE CAN'T")
    
