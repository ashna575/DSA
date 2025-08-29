def remove_duplicates_sorted(arr):
    if not arr:
        return []
    
    index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    return arr[:index+1]

# Example
arr = [1, 1, 2, 2, 3, 4, 4, 5]
print("Original:", arr)
print("After Removing Duplicates:", remove_duplicates_sorted(arr))
