# Input kecepatan awal, jarak takeoff
v_akhir = float(input("Masukkan kecepatan jett lepas landas --> "))
s = float(input("Masukkan panjang landasan --> "))

# Kalkulasi waktu dan akselerasi
t = 2*s/v_akhir
a = v_akhir/t

print(f"Akselerasi jett pada saat lepas landas : {a:.2f} meter per second kuadrat")
print(f"Waktu yang dibutuhkan jett untuk lepas landas : {t:.2f} detik")
