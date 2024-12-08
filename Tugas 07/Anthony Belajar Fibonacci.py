cache = {}
def fibonacci(n):
    if n<=1:
        return n
    else:
        cache[n-1] = fibonacci(n-1)
        cache[n-2] = fibonacci(n-2)
    return cache[n-1]+cache[n-2]

n = int(input())
fibonacci(n-1)
cache = dict(sorted(cache.items(), reverse=True))
for i in cache:
    print(cache[i], end=" ")
print()
print(sum(cache.values()))