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


array=[43,542,52,6,42,3,5,]        
print(Quicksort(array))        
            
            
            
def partition(arr, low, high):
    pivot = arr[high]   
    i = low - 1       

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)   
        quicksort(arr, pi + 1, high)  



arr = [10, 7, 8, 9, 1, 5]

quicksort(arr, 0, len(arr) - 1)
print( arr)
