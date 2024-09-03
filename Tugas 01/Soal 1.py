# Tarif per kilometer
tarif = 1.5

# Input meteran awal dan meteran akhir
meteran_awal = float(input("Meteran awal : "))
meteran_akhir = float(input("Meteran akhir : "))

# Kalkulasi tarif total
total = abs(meteran_awal-meteran_akhir)*tarif

# Output tarif total
print("Biaya taxi adalah %.2f dollar" % total)
