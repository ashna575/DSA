def array_intersection(arr1, arr2):
    result = []
    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)
    return result

def array_union(arr1, arr2):
    result = arr1[:]
    for i in arr2:
        if i not in result:
            result.append(i)
    return result

# Example
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print("Intersection:", array_intersection(arr1, arr2))
print("Union:", array_union(arr1, arr2))
