from time import time
from math import sqrt

def jump(arr, key):
    mulai = time()
    n = len(arr)
    step = int(sqrt(n))  # Tentukan ukuran langkah
    prev = 0

    # Lompat hingga elemen yang dicari lebih kecil atau mencapai akhir array
    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            waktu = time()-mulai
            return -1, waktu

    # Lakukan pencarian linear pada blok yang ditemukan
    for i in range(prev, min(step, n)):
        if arr[i] == key:
            waktu = time()-mulai
            return i, waktu
    waktu = time()-mulai
    return -1, waktu

arr = list(map(int, input("Masukkan array : ").split()))
key = int(input("Masukkan angka yang dicari : "))
idx, waktu = jump(sorted(arr), key)
if idx == -1:
    print("Kamu itu menghayal seperti halnya kau bersama dia")
    print(f"Waktu kamu sadar {waktu} ms")
else:
    print(f"{key} berada di index {idx}")
    print(f"Waktu pencarian jati diri {waktu} ms")