array=[6,3,5,2,7]
n=len(array)
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if array[i]>array[j]:
            count+=1
print(count)            