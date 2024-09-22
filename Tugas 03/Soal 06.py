panjang = int(input("Masukkan panjang kedua array : "))
arr1 = list(map(int, input("Masukkan array 1 : ").split()))
arr2 = list(map(int, input("Masukkan array 2 : ").split()))
cek = int(input("Masukkan berapa kali pengecekan kedua array : "))
for i in range(0, cek):
    temp1 = 0
    temp2 = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        temp1 += arr1[i]
        temp2 += arr2[i]
    if temp1==temp2:
        print("YA")
    else:
        print("TIDAK")