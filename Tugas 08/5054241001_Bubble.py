def bubble(arr, reverse=False):
    n = len(arr)
    if not reverse:
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]<arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int, input().split()))
print(bubble(arr))
print(bubble(arr, reverse=True))

