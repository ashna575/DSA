arry=[0,1,0,3,12]
zero=[]
num=[]
for i in range(0,len(arry)):
    if(arry[i]==0):
       zero.append(arry[i])
    else:
       num.append(arry[i])
newArray= num+zero      
print(arry)       
print(zero)
print(newArray)