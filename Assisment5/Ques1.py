def countSubarrays(nums, k):
    count = 0
    n = len(nums)

    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total == k:
                count += 1

    return count

nums = [1, 2, 3]
k = 3
print(countSubarrays(nums, k))  



        

    