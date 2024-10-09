bu = list(map(int, input().split()))
barang = list(map(int, input().split()))
uang = list(map(int, input().split()))
barang.sort(reverse=True)
uang.sort()
hutang = 0
b = 0
u = 0
while True:
    if b == len(barang) or u == len(uang):
        print(hutang)
        break
    if uang[u] < barang[b]:
        hutang += barang[b] - uang[u]
        b += 1
        u += 1
    else:
        b += 1