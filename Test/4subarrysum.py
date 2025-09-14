def subarraysum(arr, target):
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == target:
                return arr[i:j+1]   
    return None



arr = [1, 2, 3, 7, 5]
target = 12
result = subarraysum(arr, target)
print("Subarray:", result)
