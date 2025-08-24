array=[12,99,6,8,4,61,33]
even=0
odd=0
for i in range(0,len(array)):
    if array[i] %2==0 :
      even+=1
    else:
        odd+=1       
print(even,odd)        