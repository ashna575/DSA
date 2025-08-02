def find_K_largestNo(arry,k):
    a=[]
    for i in range(0,len(arry)):
       a.append(arry[i])
       
       if len(a) >k:
           a.remove(min(a))
       
    return min(a)
   
arry=[3,2,1,5,6,4]  
target=2
print(find_K_largestNo(arry,target))