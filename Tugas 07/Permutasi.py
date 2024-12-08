def permutasi(n, r):
    if r == 0:
        return 1
    else:
        return n * permutasi(n - 1, r - 1)

n = 5
r = 3
print(f"Permutasi P({n}, {r}) = {permutasi(n, r)}")