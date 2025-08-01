num1=[1,2,2,3,1]
num2=[2,2,3,4,3]
newArry=[]

for i in num1 :
    if i  in num2    and i not in newArry:     
      newArry.append(i)
  
           
print(newArry)        