def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def remainder(a, b):
    print(f"The modulo is {a%b}")

f_cache = {}
def fibonacci(n):
    if n<=1:
        return 1
    if n not in f_cache:
        f_cache[n-2] = fibonacci(n-2)
        f_cache[n-1] = fibonacci(n-1)
    f_cache[0] = 0
    return f_cache[n-2]+f_cache[n-1]

def odd_numbers(n):
    res = 0
    for i in range(len(n)):
        if n[i]%2==1:
            res+=1
    return res

if __name__ == "__main__":
    n = int(input())
    primes = sieve_of_eratosthenes(n)
    print(f"Angka {n} adalah angka prima") if n in primes else print(f"Angka {n} bukan angka prima")
    a, b = map(int, input().split())
    remainder(a, b)
    n = int(input())
    fibonacci(n)
    print("10 angka pertama bilangan fibonacci:",*f_cache.values())
    a = list(map(int, input().split()))
    print("Banyak angka ganjil:",odd_numbers(a))