import sys
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7
memo = {}

def pancong_variasi(N):
    # Basis kasus
    if N == 0:
        return 1
    if N < 0:
        return 0
    if N in memo:
        return memo[N]
    memo[N] = (pancong_variasi(N - 2) + pancong_variasi(N - 3) + pancong_variasi(N - 4)) % MOD
    return memo[N]
N = int(input().strip())
print(pancong_variasi(N))

