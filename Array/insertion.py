# arry = [1, 2, 3, 4, 5]
# arry.append(0)

# for i in range(len(arry)-1, 0, -1):
#     arry[i] = arry[i-1]

# arry[0] = 0

# print(arry)



#Another method
arry=[1,2,3,4,5]
size=len(arry)
insertingEle=[8,9]
k=len(insertingEle)

result=[0]*(size+k)

for i in range(k):
    result[i]=insertingEle[i]

for i in range(size):
    result[i+k]=arry[i]    

print(result)

#using method 
# arr=[2,4,5,6,7,7]
# arr.insert(0,33)
# arr.insert(1,32)

# print(arr)


# nums=[1,2,3,4,65]
# size=len(nums)
# num=44
# index=3
# result=[0]*(size+1)

# print(nums)
# for i in range(size-(index-1)):
#     result[i]=nums[i]
    

# result[index]=num

# for i in range(index,size):
#     result[i+1]=nums[i]
# print(result)    
