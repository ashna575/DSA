array=[12,99,6,8,4,66]
min=array[0]
for i in range(1,len(array)):
    if array[i] < min:
        min=array[i]
print(min)        