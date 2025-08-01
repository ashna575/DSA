def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    
    # If total length is odd
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        # If total length is even
        mid1 = merged[n // 2]
        mid2 = merged[n // 2 - 1]
        return (mid1 + mid2) / 2
    
    
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
