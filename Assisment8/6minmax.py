def find_min_max(arr):
    maximum = arr[0]
    minimum = arr[0]
    
    for i in arr:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return minimum, maximum


arr = [5, 10, 3, 25, 8, 15]
mn, mx = find_min_max(arr)
print("Array:", arr)
print("Minimum:", mn, " Maximum:", mx)
