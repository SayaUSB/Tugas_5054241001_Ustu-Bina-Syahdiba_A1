# Konstanta
panas = 0.65
energi_galon = round(58e5/42,2)

# Input
jumlah_galon = int(input("Masukkan jumlah galon --> "))

# Output
total_panas = jumlah_galon*energi_galon*panas
print(f"Panas yang dihasilkan {jumlah_galon} galon adalah {total_panas:.2f} BTU")
