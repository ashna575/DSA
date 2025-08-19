#using method
arry=[1,2,3,4,5,6,7]
size=len(arry)
arry.pop(5)

print(arry)
#slicing
arr=[2,34,5,53,45,35,33]
arr=arr[:-1]
print(arr)


#deleting particular value
color = ["red", "yellow", "orange", "blue"]
color.remove("red")   

for i in range(len(color)):
    if color[i] == "yellow":
        del color[i]
        break    
print(color)


arr=[2,34,5,53,45,35,33]
#delete from starting
arr.pop(0)        
print(arr)

del arr[2]  #index value
print(arr)


#slicing
arr=[2,34,5,53,45,35,33]
arr=arr[2:]

print(arr)