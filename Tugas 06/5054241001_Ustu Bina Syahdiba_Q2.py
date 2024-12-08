n, m = map(int, input().split())
peta = []
for _ in range(n):
    peta.append(list(map(int, input().split())))
hasil = 0
for i in range(n):
    for j in range(m):
        if peta[i][j]==1:
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if a<0 or b<0 or a>=n or b>=m or peta[a][b]==1:
                        continue
                    elif peta[a][b]==0:
                        hasil += 1
print(hasil)