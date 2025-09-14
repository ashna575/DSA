def left_rotate(arr, k):
    k = k % len(arr)   
    return arr[k:] + arr[:k]

def right_rotate(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
print("Original:", arr)
print("Left :", left_rotate(arr, 2))
print("Right", right_rotate(arr, 2))
