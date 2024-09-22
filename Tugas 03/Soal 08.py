panjang, target, tinggi = map(int, input("Masukkan panjang array, target, dan tinggi tower : ").split())
arr = list(map(int, input("Masukkan elemen array : ").split()))
hasil = 0
for _ in range(0, tinggi):
    a, b = map(int, input().split())
    temp = 0
    for i in range(a-1, b-1):
        temp += arr[i]
    hasil += temp
if target>=hasil:
    print(f"EZ banget, energiku sisa {hasil-target}!")
else:
    print(f"NT, kurang {hasil-target} energi sih.")