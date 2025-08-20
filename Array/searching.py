def linear(arry,target):
    for i in range(len(arry)):
        if(i==target):
            return i
        
    
target=4
arry=[1,2,3,4,5,6]
print(linear(arry,target))    
            
            
            
            
def binarySearch(target,arry):
    low=0
    high=len(arry)-1
    s=sorted(arry)
    while low<high:
      midpoint=low+high//2
      if s[midpoint]==target:
         return midpoint
      elif s[midpoint]>target:
        high=midpoint-1
       
      else :     
        low = midpoint+1  
       
       
arry=[2,34,5,67,7]
target=7

print(binarySearch(target,arry))            

            