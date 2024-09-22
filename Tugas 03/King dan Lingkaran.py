x1, y1 = map(int, input().split()) # Titik tengah lingkaran
xs, ys = map(int, input().split()) # Titik awal melangkah
xf, yf = map(int, input().split()) # Titik akhir melangkah
jarak_1s = ((x1-xs)**2+(y1-ys)**2)
jarak_1f = ((x1-xf)**2+(y1-yf)**2)
jarak_sf = ((xs-xf)**2+(ys-yf)**2)
if jarak_1f>jarak_sf:
    print("Yes")
else:
    print("No")

