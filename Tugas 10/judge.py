def binary_search_lower(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # Default result if no number is found

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            result = arr[mid]  # Update result
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return result

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 10

result = binary_search_lower(arr, target)
if result != -1:
    print(f"The largest number lower than {target} is: {result}")
else:
    print(f"There is no number lower than {target} in the array")