arry=[1,7,3,6,5,6]
def pivotIndex(arry):
 leftsum=0
 totalSum=sum(arry)
 for i in range(0,len(arry)):
    rightsum=totalSum-leftsum-arry[i]
    if (rightsum==leftsum):
        return i
    leftsum= leftsum+arry[i]
    

  
print(pivotIndex(arry))        