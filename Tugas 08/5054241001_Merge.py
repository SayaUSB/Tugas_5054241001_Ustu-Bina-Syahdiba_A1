def merge(arr):
    if len(arr)>1:  
        tengah = len(arr)//2
        kiri = arr[:tengah]
        kanan = arr[tengah:]
        merge(kiri)
        merge(kanan)

        a = b = c = 0
        while a < len(kiri) and b < len(kanan):
            if kiri[a] < kanan[b]:
                arr[c] = kiri[a]
                a += 1
            else:
                arr[c] = kanan[b]
                b += 1
            c += 1
            
        while a < len(kiri):
            arr[c] = kiri[a]
            a += 1
            c += 1

        while b < len(kanan):
            arr[c] = kanan[b]
            b += 1
            c += 1

arr = list(map(int, input().split()))
merge(arr)
print(arr)
