def urutan(x):
    angka = int(x)
    temp = 0
    while True:
        for i in range(len(x)):
            temp += int(x[i])
        if temp<10:
            return temp, angka
        x = str(temp)
        temp = 0

masuk = list(map(str, input().split()))
masuk.sort(key=urutan)
print(' '.join(masuk))
