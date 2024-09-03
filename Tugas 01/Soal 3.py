# Input waktu mati
waktu = list(map(int, input("Lama waktu mati : ").split()))

# Mengubah waktu menjadi satuan jam
jam = waktu[0]+waktu[1]/60

# Rumus temperatur
T = float((4*(jam**2))/(jam+2))
T -= 20

# Output temperatur sekarang
print("Temperatur sekarang : %.2f Celsius" %T)
