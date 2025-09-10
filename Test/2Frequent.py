from collections import Counter

def Frequent(nums, k):
   
    freq = Counter(nums)
    common = freq.most_common(k)
    
    return [num for num, count in common]



print(Frequent([1,1,1,2,2,3], 2))  

    
