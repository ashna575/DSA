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




