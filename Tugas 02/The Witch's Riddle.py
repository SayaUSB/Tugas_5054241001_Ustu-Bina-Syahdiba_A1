tujuh = list(map(int, input().split()))
gerak = int(input())
sebanyak = int(input())
index = list(map(int, input().split()))
for i in range(0, sebanyak):
    panjang = len(tujuh)-gerak
    tujuh.extend(tujuh[:-gerak])
    tujuh = tujuh[panjang:]
for i in index:
    print(tujuh[i], end=" ")