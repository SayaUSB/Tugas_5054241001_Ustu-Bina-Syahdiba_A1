n = int(input())
segitiga = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = segitiga[i - 1][j - 1] + segitiga[i - 1][j]
    segitiga.append(row)
segitiga = segitiga[::-1]
for row in segitiga:
    print(' '.join(map(str, row)).center(2*n))