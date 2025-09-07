def sort012(arr):
    low, mid, high = 0, 0, len(arr)-1
    
    while mid <= high:
        if arr[mid] == 0:   # Case 1: Swap with low
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1: # Case 2: Just move mid
            mid += 1
        else:               # Case 3: arr[mid] == 2, swap with high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example
nums = [0, 2, 1, 2, 0, 1, 0]
print("Sorted:", sort012(nums))
