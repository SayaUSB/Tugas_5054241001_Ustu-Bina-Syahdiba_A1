ukuran_matriks1 = list(map(int, input().split()))
ukuran_matriks2 = list(map(int, input().split()))
if ukuran_matriks1[1]!=ukuran_matriks2[0]:
    print("Matriks tidak dapat dijumlahkan")
else:
    matriks1 = []
    matriks2 = []
    matriks3 = [[0 for _ in range(ukuran_matriks2[1])] for _ in range(ukuran_matriks1[0])]
    for i in range(ukuran_matriks1[0]):
        temp = list(map(int, input().split()))
        matriks1.append(temp)
    for i in range(ukuran_matriks2[0]):
        temp = list(map(int, input().split()))
        matriks2.append(temp)
    for i in range(ukuran_matriks1[0]):
            for j in range(ukuran_matriks2[1]):
                for k in range(ukuran_matriks1[1]):
                    matriks3[i][j] += matriks1[i][k] * matriks2[k][j]
    print(matriks3)
