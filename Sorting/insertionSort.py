num = [62,44,3,45,63,86,9]

for i in range(1,len(num)):
    key=num[i]
    j=i-1
    while j>=0 and num[j]>key:
        num[j+1]=num[j]
        j-=1
        num[j+1]=key
        
print(num)        



    
       