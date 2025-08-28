def delete_at_index(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid Index")
        return arr
    arr.pop(index)  
    return arr

arr = [10, 20, 30, 40, 50]
print("Before:", arr)
print("After Deletion:", delete_at_index(arr, 2))
