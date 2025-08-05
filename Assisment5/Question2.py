def consecutive(arry):
     s=sorted(arry)
     count=1
     for i in range(1,len(s)):
       
       if  s[i]-s[i-1]==1:
            count+=1       
         
           
     return count
         

arry=[100,4,200,1,2,3]   
print(consecutive(arry)) 