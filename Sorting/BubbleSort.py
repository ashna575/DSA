      
array=[3,45,32,4,5,24,23,8,7,5,77,6,75,67] 
n=len(array)
for i in range(0,n-1):
    for j in range(0,n-1-i):
         if array[j]>array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


print(array)                  