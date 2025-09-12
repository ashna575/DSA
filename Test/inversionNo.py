array=[6,3,5,2,7]
n=len(array)
a=[]
for i in range(0,n):
    for j in range(i+1,n):
        if array[i]>array[j]:
          a.append([array[i],array[j]])  
print(a)   