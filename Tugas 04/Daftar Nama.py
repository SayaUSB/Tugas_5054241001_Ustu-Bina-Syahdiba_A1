from collections import OrderedDict # Library mengurutkan dictionary dari key

sigma = list(map(int, input().split())) # Input banyak siswa dan ukuran peta
pcc = {} # Dictionary untuk menyimpan lokasi siswa
for i in range(sigma[0]):
    temp = list(map(int, input().split())) # Input lokasi siswa
    if temp[1] in pcc: # Menambahkan siswa
        pcc[temp[1]] += 1 
    else:
        pcc[temp[1]] = 1
pcc = OrderedDict(sorted(pcc.items())) # Mengurutkan dictionary dari key
for i in pcc: # Output lokasi siswa
    print(pcc[i])
