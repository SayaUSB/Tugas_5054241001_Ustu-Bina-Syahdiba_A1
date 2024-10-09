banyak, uang = map(int, input().split()) # Memasukkan banyak buah dan uang
harga = list(map(int, input().split())) # Memasukkan harga
harga.sort() # Sorting harga
output = 0
for i in range(len(harga)): # Cek kemungkinan buah yang dibeli
    if uang >= harga[i]:
        output += 1
    else:
        break
print(output) # Output kemungkinan buah yang dibeli