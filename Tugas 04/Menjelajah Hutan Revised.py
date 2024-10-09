perintah = list(map(int, input().split())) # Input ukuran peta dan gerakan
arr = [] # Kondisi awal peta
lokasi = [0, 0] # Koordinat awal
for i in range(perintah[0]):
    arr.append(list(map(int, input().split()))) # Input peta
gerak = input() # Input gerakan
emas = arr[0][0]
for i in gerak: # Waktunya menambang
    if i=='U':
        lokasi[0] -= 1
        if lokasi[0]<0: # Cek posisi invalid
            print("gerakanmu salah bung!")
            break
        emas += 3
        emas += arr[lokasi[0]][lokasi[1]]
    elif i=='R':
        lokasi[1] += 1
        if lokasi[1]>=perintah[1]: # Cek posisi invalid
            print("gerakanmu salah bung!")
            break
        emas += 3
        emas += arr[lokasi[0]][lokasi[1]]
    elif i=='L':
        lokasi[1] -= 1
        if lokasi[1]<0: # Cek posisi invalid
            print("gerakanmu salah bung!")
            break
        emas -= 2
        emas += arr[lokasi[0]][lokasi[1]]
    elif i=='D':
        lokasi[0] += 1
        if lokasi[0]>=perintah[0]: # Cek posisi invalid
            print("gerakanmu salah bung!")
            break
        emas -= 2
        emas += arr[lokasi[0]][lokasi[1]]
print(emas) # Output total emas