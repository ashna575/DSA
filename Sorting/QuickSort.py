def Quicksort(arry):
    if len(arry) <=1:
        return arry
    
    pivot=arry[len(arry)//2]
    left=[]
    righ=[]
    mid=[]
    for i in arry:
        if i>pivot:
            righ.append(i)
        elif i<pivot:
            left.append(i)
        else :
            mid.append(i)
    return Quicksort(left)+mid+Quicksort(righ)




array=[43,542,52,6,42,3,5,6]        
print(Quicksort(array))        
            