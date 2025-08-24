array=[12,99,6,8,4,66]
max=array[0]
for i in range(1,len(array)):
    if array[i] > max:
        max=array[i]
print(max)        