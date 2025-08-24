def second_largest_sort(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    arr = list(set(arr))  
    arr.sort()

    if len(arr) < 2:
        return "No second largest element"
    return arr[-2]

# Example
arr = [12, 35, 1, 10, 34, 1]
print("Second largest:", second_largest_sort(arr))
