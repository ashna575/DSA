
arry=[-4,-1,0,3,10]
m=[]
    
for i in range(0,len(arry)):
    sq=arry[i]*arry[i]
    m.append(sq)
    

print(m)
    
for i in range(0,len(m)):
  for j in range(0,len(m)-1):
      if(m[j]>m[j+1]):
       m[j],m[j+1]=m[j+1],m[j]
    
       
print(m)          
        
        
#Output   [16,1,0,9,100]
          #[0,1,9,16,100]
