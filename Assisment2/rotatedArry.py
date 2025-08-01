def search(nums, target):
    left = 0                                     # left=0
    right = len(nums) - 1                       #  right=6    mid=3

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:              
            return mid

        # Check if left half is sorted                 
        if nums[left] <= nums[mid]:                    #   4<= 7          
            if nums[left] <= target < nums[mid]:      #  4<= 0 < 7
                right = mid - 1                           
            else:                                    #   left=4
                left = mid + 1    
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:  # target is in the right half
                left = mid + 1                        #0<2<3   left=4
            else:
                right = mid - 1

    return -1
print(search([4,5,6,0,1,2,3], 2))


      
      
      
        # if(arry[left]<=arry[mid]):
        #     if(arry[left]< target <arry[mid]):
        #         right= arry[mid]-1
        #     else:
        #         left=arry[mid]+1    
            

        # else:
        #     if(arry[right]>target>arry[mid]):
                
                
                
                
                
                
                
                
# print(rotatedsearch([4,5,6,7,0,1,2], 0))                
                