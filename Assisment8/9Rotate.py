def rotate_array(arr, k):
    n = len(arr)
    k = k % n  
    reverse(arr, 0, n-1)      
    reverse(arr, 0, k-1)      
    reverse(arr, k, n-1)   
    return arr

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = [1, 2, 3, 4, 5, 6, 7]
print("Before:", arr)
print("After Rotation by 3:", rotate_array(arr, 3))
