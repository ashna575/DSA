def second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

# Example
arr = [10, 20, 4, 45, 99, 99]
print("Array:", arr)
print("Second Largest:", second_largest(arr))
