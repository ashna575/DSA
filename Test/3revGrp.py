def rev_subarray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def reversek(arr, k):
    n = len(arr)
    left = 0
    right = k - 1

    while left < n:
        if right >= n:
            right = n - 1
        rev_subarray(arr, left, right)

        left = right + 1
        right = left + k - 1

    return arr



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print("Output:", reversek(arr, k))
