def searchInsert(nums, target):
    left =0
    right=len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid   
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [31,4,5,7,12,15,42,68]
target = 4
print(searchInsert(nums, target))  

target = 20
print(searchInsert(nums, target)) 



