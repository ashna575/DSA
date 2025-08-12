def bubbleSort(num):
    for i in range(len(num)):
      for j in range(len(num)-1):
          if num[j] >num[j+1]:
              num[j+1],num[j]=num[j],num[j+1] 
    return num    
        
        
        
        
num=[2,44,54,3,4,23,42,8]
print(bubbleSort(num))

        
        