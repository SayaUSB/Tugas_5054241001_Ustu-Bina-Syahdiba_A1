# Input tipe dan ukuran roti
tipe = input("Masukkan tipe roti : ")
ukuran = input("Masukkan ukuran roti : ")

# Kalkulasi waktu dan operasi roti
waktu = 0
print("Masukkan operasi roti:")
if tipe=="putih":
    operasi = int(input())
    if operasi == 1:            # Primary kneading
        waktu += 15
    elif operasi == 2:          # Primary rising
        waktu += 60
    operasi = int(input())
    if operasi == 1:            # Secondary kneading
        waktu += 18
    elif operasi == 2:          # Secondary rising
        waktu += 20
    # Ditambah waktu final rising, baking, dan cooling
    waktu += 150
elif tipe=="manis":
    operasi = int(input())
    if operasi == 1:            # Primary kneading
        waktu += 20
    elif operasi == 2:          # Primary rising
        waktu += 60
    operasi = int(input())
    if operasi == 1:            # Secondary kneading
        waktu += 33
    elif operasi == 2:          # Secondary rising
        waktu += 30
    # Ditambah waktu final rising, baking, dan cooling
    waktu += 140

# Output lama waktu memasak roti dan ditambah waktu loaf shaping
if ukuran == "besar":
    waktu *= 1.5
    print(f"Waktu memasak roti adalah {waktu} menit 3 detik")
else:
    print(f"Waktu memasak roti adalah {waktu} menit 2 detik")


