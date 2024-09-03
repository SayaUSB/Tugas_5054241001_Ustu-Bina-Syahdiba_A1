# Input tinggi bendungan dan banyaknya air yang masuk
tinggi = float(input("Masukkan tinggi bendungan --> "))
air = float(input("Masukkan air yang masuk --> "))
air *= 1e3

# Konstanta megawatt, efisiensi, gravitasi
megawatt = 1e6
efisiensi = 0.9
gravitasi = 9.8

# Kalkulasi power(watt)
power = float(air*gravitasi*tinggi)

# Karena efisiensi dalam soal adalah 90%
power *= efisiensi

# Watt menjadi megawatt
power /= 1e6

# Output megawatt yang dihasilkan
print("Output tenaganya %.2f Megawatt" % power)
