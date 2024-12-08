def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
m, n = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.extend(row)

q = int(input())
queries = list(map(int, input().split()))
for target in queries:
    result = binary_search(sorted(arr), target)
    print(result, end=' ')
print()
