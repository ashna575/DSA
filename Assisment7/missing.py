def missing_number(arr, n):
  
    total = n * (n + 1) // 2

    return total - sum(arr)

nums = [1, 2, 4, 5, 6] 
n = 6
print("Missing Number:", missing_number(nums, n))
