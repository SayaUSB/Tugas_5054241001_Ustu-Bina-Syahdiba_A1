banyak = int(input())
for _ in range(banyak):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    q = int(input())
    if q==1:
        max_sum = float("-inf")
        for i in range(n):
            current_sum = 0
            for j in range(i, min(i + k, n)):
                current_sum += arr[j]
                max_sum = max(max_sum, current_sum)
        print(max_sum)
    elif q==2:
        min_sum = float("inf")
        for i in range(n):
            current_sum = 0
            for j in range(i, min(i + k, n)):
                current_sum += arr[j]
                min_sum = min(min_sum, current_sum)
        print(min_sum)