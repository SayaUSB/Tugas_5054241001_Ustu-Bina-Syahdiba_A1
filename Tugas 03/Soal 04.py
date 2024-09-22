import math as m    # Menggunakan library math untuk fungsi akar

arr = []    # Berisi angka prima

def prima(x):   # Fungsi mencari angka prima
    if x<=1:
        return False
    elif x==2 or x==3:
        return True
    for i in range(2, m.floor(m.sqrt(x))+1):
        if x%i==0:
            return False
    return True

perulangan = int(input("Masukkan banyak perulangan : "))
i = 2 # Angka pertama bilangan prima
for _ in range(0, perulangan):
    a, b = map(int, input("Mencari dari prima urutan ke a sampai b : ").split())
    while len(arr)<b: # Pengecekan bilangan prima
        if prima(i): 
            arr.append(i)
        i += 1
    for j in range(a-1, b): # Output urutan angka prima yang diminta
        print(arr[j], end=" ") 
    print("\n")