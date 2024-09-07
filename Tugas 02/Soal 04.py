# Input benda
benda = input("Masukkan benda : ").upper()

# Klasifikasi benda
if benda[0]=='O':
    kategori = "Ammonia"
elif benda[0]=='B':
    kategori = "Carbon Monoxide"
elif benda[0]=='Y':
    kategori = "Hydrogen"
elif benda[0]=='G':
    kategori = "Oxygen"
else:
    kategori = "Konten tidak diketahui"

# Output klasifikasi benda
print(f"Kategori benda ini adalah {kategori}")