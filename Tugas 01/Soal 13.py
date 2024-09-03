# Input banyak murid
murid = int(input("Banyaknya murid --> "))

# Kalkulasi
murid_sisa = murid%30
murid_masuk = murid-murid_sisa
banyak_kelas = murid//30

# Output
print(f"Murid yang mengikuti kelas : {murid_masuk}")
print(f"Banyak kelas : {banyak_kelas}")
print(f"Murid yang tidak mengikuti kelas : {murid_sisa}")