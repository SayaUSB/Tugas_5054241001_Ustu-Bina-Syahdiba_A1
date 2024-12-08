from time import time

def interpolation(arr, key):
    mulai = time()
    low = 0
    high = len(arr)-1
    while low <= high and key >= arr[low] and key <= arr[high]:
        # Cegah pembagian nol
        if arr[low] == arr[high]:
            if arr[low] == key:
                waktu = time()-mulai
                return low, waktu
            waktu = time()-mulai
            return -1, waktu
            
        # Hitung posisi estimasi
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # Periksa apakah elemen ditemukan
        if arr[pos] == key:
            waktu = time()-mulai
            return pos
        elif arr[pos] < key:
            low = pos + 1  # Fokus pada bagian kanan
        else:
            high = pos - 1  # Fokus pada bagian kiri
    waktu = time()-mulai
    return -1, waktu  # Elemen tidak ditemukan

arr = list(map(int, input("Masukkan array : ").split()))
key = int(input("Masukkan angka yang dicari : "))
idx, waktu = interpolation(sorted(arr), key)
if idx == -1:
    print("Kamu itu menghayal seperti halnya kau bersama dia")
    print(f"Waktu kamu sadar {waktu} ms")
else:
    print(f"{key} berada di index {idx}")
    print(f"Waktu pencarian jati diri {waktu} ms")