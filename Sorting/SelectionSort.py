num = [62,44,3,45,63,86,9]
for i in range(len(num)):
    min = i
    for j in range(i+1,len(num)):
        if num[j] < num[min]:
            min = j
    c=num[min]
    num[min]=num[i]
    num[i]=c
            

print(num) 
          
          
            
 


   

                    
        