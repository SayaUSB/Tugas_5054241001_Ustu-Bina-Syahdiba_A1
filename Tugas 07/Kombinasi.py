def kombinasi(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return kombinasi(n - 1, k - 1) + kombinasi(n - 1, k)
        
def susunan_ubin(n, m):
    hasil = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            hasil.append((i, j))
    return hasil

n = 3
m = 2
susunan = susunan_ubin(n, m)
print(f"Susunan ubin {n} x {m} adalah:", *susunan)
print(f"Jumlah susunan: {len(susunan)}")