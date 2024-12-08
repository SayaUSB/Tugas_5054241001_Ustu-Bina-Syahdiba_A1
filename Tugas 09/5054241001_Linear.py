from time import time

def linear(arr, key):
    mulai = time()
    for i in range(len(arr)):
        if arr[i]==key:
            waktu = time()-mulai
            return i, waktu
    waktu = time()-mulai
    return -1, waktu

arr = list(map(int, input("Masukkan elemen array: ").split()))
key = int(input("Masukkan angka yang dicari : "))
idx, waktu = linear(arr, key)
if idx == -1:
    print("Kamu itu menghayal seperti halnya kau bersama dia")
    print(f"Waktu kamu sadar {waktu} ms")
else:
    print(f"{key} berada di index {idx}")
    print(f"Waktu pencarian jati diri {waktu} ms")