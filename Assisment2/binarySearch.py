def binarySearch(target,arry):
    low=0
    high=len(arry)-1
    while low<=high:
      midpoint=low+high//2
      if arry[midpoint]==target:
         return midpoint
      elif arry[midpoint]>target:
        high=midpoint-1
       
      else :     
        low = midpoint+1  
       
       
arry=[2,34,5,67,7]
target=7

print(binarySearch(target,arry))            

