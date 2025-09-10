def subarray_with_sum(arr, target):
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == target:
                return arr[i:j+1], (j - i + 1)   
    return None, 0



arr = [1, 2, 3, 7, 5]
target = 12
subarr, count = subarray_with_sum(arr, target)

if subarr:
    print("Subarray:", subarr)
    print("Count of elements:", count)
else:
    print("No subarray found")
