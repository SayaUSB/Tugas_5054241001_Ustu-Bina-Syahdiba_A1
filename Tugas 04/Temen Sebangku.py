sigma = list(map(int, input().split()))
arr = [[0 for _ in range(sigma[1])]for _ in range(sigma[2])] # Inisialisasi array 2d
for i in range(sigma[0]):
    masuk = list(map(int, input().split()))
    arr[masuk[1]-1][masuk[2]-1] = masuk[0] # Memasukkan nomor dan koordinat siswa ke array 2d
for i in range(sigma[1]):
    for j in range(sigma[2]):
        if arr[i][j] != 0:
            for a in range(i-1, i+2): # Cek apakah ada siswa di sekitar
                for b in range(j-1, j+2):
                    if i==a and j==b or a<0 or b<0 or a>=sigma[1] or b>=sigma[2]:
                        continue
                    if arr[a][b]>0:
                        print(f"Yang duduk di sekitar siswa {arr[i][j]} ada siswa {arr[a][b]}")
            