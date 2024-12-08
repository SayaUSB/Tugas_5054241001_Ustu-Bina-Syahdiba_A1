from time import time

def binary(arr, key):
    mulai = time()
    kiri, kanan = 0, len(arr)-1
    while kiri<=kanan:
        tengah = kiri + (kanan-kiri)//2
        if arr[tengah]==key:
            waktu = time() - mulai
            return tengah, waktu
        elif arr[tengah]<key:
            kiri = tengah + 1
        elif arr[tengah]>key:
            kanan = tengah - 1
    waktu = time() - mulai
    return -1, waktu

arr = list(map(int, input("Masukkan array : ").split()))
key = int(input("Masukkan angka yang dicari : "))
idx, waktu = binary(sorted(arr), key)
if idx == -1:
    print("Kamu itu menghayal seperti halnya kau bersama dia")
    print(f"Waktu kamu sadar {waktu} ms")
else:
    print(f"{key} berada di index {idx}")
    print(f"Waktu pencarian jati diri {waktu} ms")