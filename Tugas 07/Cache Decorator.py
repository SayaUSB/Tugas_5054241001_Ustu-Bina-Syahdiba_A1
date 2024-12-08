def memo(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@memo
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(100))