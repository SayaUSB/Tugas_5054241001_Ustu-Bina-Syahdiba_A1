# Input panjang lebar rumah dan halaman
panjang_halaman = float(input("Masukkan panjang halaman --> "))*3
lebar_halaman = float(input("Masukkan lebar halaman --> "))*3
panjang_rumah = float(input("Masukkan panjang rumah --> "))*3
lebar_rumah = float(input("Masukkan lebar rumah --> "))*3

# Kalkulasi luas halaman dan rumah
luas_halaman = panjang_halaman*lebar_halaman
luas_rumah = panjang_rumah*lebar_rumah

# Lama memotong rumput
lama = (luas_halaman-luas_rumah)/2

# Hitung jam, menit, detik
waktu = []
if lama/3600>=1:
    waktu.append(lama//3600)
    lama %= 3600
else:
    waktu.append(0)
if lama<60:
    waktu.append(0)
    waktu.append(lama)
elif lama%60==0:
    waktu.append(lama//60)
    waktu.append(0)
else:
    waktu.append(lama//60)
    waktu.append(lama%60)

# Output 
if waktu[0]<1:
    if waktu[1]<1:
        print(f"Lama memotong rumput halaman adalah {waktu[2]:.0f} detik")
    elif waktu[2]<1:
        print(f"Lama memotong rumput halaman adalah {waktu[1]:.0f} menit")
    elif waktu[1]>=1 and waktu[2]>=1:
        print(f"Lama memotong rumput halaman adalah {waktu[1]:.0f} menit {waktu[2]:.0f} detik")
    else:
        print(f"Lama memotong rumput halaman adalah 0 detik")
else:
    if waktu[1]<1 and waktu[2]<1:
        print(f"Lama memotong rumput halaman adalah {waktu[0]:.0f} jam")
    elif waktu[1]<1 and waktu[2]>=1:
        print(f"Lama memotong rumput halaman adalah {waktu[0]:.0f} jam {waktu[2]:.0f} detik")
    elif waktu[1]>=1 and waktu[2]<1:
        print(f"Lama memotong rumput halaman adalah {waktu[0]:.0f} jam {waktu[1]:.0f} menit")
    else:
        print(f"Lama memotong rumput halaman adalah {waktu[0]:.0f} jam {waktu[1]:.0f} menit {waktu[2]:.0f} detik")