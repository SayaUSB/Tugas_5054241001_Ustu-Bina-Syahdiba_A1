kiri = [0]
kanan = [0]
merge = [0]

def merges(arr, left, mid, right):
    merge[0] += 1 
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
        kiri[0] += 1
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        kanan[0] += 1

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merges(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    banyak = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, banyak - 1)
    print(*kiri)
    print(*kanan)
    print(*merge)

