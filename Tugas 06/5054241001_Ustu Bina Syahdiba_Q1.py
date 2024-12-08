banyak = int(input())
for _ in range(banyak):
    m = int(input())
    angka = list(map(int, input().split()))
    if len(angka)==1:
        print(-1)
        continue
    dicti = {}
    for i in angka:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    modus = max(dicti.values())
    arr_modus = []
    for i in dicti:
        if dicti[i]==modus:
            arr_modus.append(i)
    if len(arr_modus)>1:
        print("*".join(map(str,arr_modus)), end=" = ")
        hasil = 1
        for i in arr_modus:
            hasil *= i
        print(hasil)
    else:
        print(f"{dicti[arr_modus[0]]}*{arr_modus[0]} = {dicti[arr_modus[0]]*arr_modus[0]}")