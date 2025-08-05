def subarraySum(nums, k):
    start=num[0]
   
    count = 0

    for i in nums:
        if num[i]+start==k:
         count+=1

    return count


num = [1, 2, 3]
k = 3
print(subarraySum(num, k)) 


        
#  for num in nums:
#         currentSum += num
#         if currentSum - k in SumCount:
#             count += SumCount[currentSum - k]
#         SumCount[currentSum] = SumCount.get(currentSum, 0) + 1

#     return count
    