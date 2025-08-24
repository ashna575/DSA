def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 2, 1]

print("arr1 sorted? ", is_sorted(arr1))  # True
print("arr2 sorted? ", is_sorted(arr2))  # False
