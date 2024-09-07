# Input koordinat
koordinat = tuple(map(float, input("Masukkan koordinat X dan Y : ").split()))

# kategorisasi kuadran
if koordinat[0]>0 and koordinat[1]>0:
    kuadran = "kuadran 1"
elif koordinat[0]<0 and koordinat[1]>0:
    kuadran = "kuadran 2"
elif koordinat[0]<0 and koordinat[1]<0:
    kuadran = "kuadran 3"
elif koordinat[0]>0 and koordinat[1]<0:
    kuadran = "kuadran 4"
elif koordinat[0]==0 and koordinat[1]>0:
    kuadran = "terletak di sumbu y positif"
elif koordinat[0]==0 and koordinat[1]<0:
    kuadran = "terletak di sumbu y negatif"
elif koordinat[0]>0 and koordinat[1]==0:
    kuadran = "terletak di sumbu x positif"
elif koordinat[0]<0 and koordinat[1]==0:
    kuadran = "terletak di sumbu x negatif"
else:
    kuadran = "terletak di titik tengah"

# Output kategorisasi kuadran
print(f"Koordinat {koordinat} termasuk {kuadran}")