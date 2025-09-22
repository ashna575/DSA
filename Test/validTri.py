def valid_tri(array):
   
    if len(array)==3:
        a=array[0]
        b=array[1]
        c=array[2]
        if a+b>c or b+c>a or c+a>b:
            return(True)
          
        else:
            return(False)    
    else:
        return(False)            

array=[12,2,3]
print(valid_tri(array))

