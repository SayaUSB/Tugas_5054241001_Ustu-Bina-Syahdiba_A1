def binary_search_lower(arr, target):
    left, right = 0, len(arr) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            count = mid + 1 
            left = mid + 1
        else:
            right = mid - 1
    return count

n, m = map(int, input().split())
arr = []
for i in range(m):
    masuk = list(map(int, input().split()))
    arr.extend(masuk)
arr.sort()
q = int(input())
questions = list(map(int, input().split()))
for i in questions:
    print(binary_search_lower(arr, i), end=' ')