banyak = int(input())
angka = list(map(int, input().split()))
flag = 0
for i in range(len(angka)-1):
    if flag==1:
        break
    for j in range(i+1, len(angka)):
        if angka[i]^angka[j] == 0:
            hasil = 0
            flag = 1
            break
        if i==0 and j==1:
            hasil = angka[i]^angka[j]
        else:
            hasil *= angka[i]^angka[j]
print(hasil)