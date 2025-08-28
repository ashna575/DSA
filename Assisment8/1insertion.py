def insert_at_position(arr, posi, value):
    n = len(arr)
    if posi < 0 or posi > n:
        print("Invalid Position")
        return arr
    
    arr += [0]
    
  
    for i in range(n, posi, -1):
        arr[i] = arr[i-1]
    
   
    arr[posi] = value
    return arr


arr = [10, 20, 30, 40]
print("Before:", arr)
print("After Insertion:", insert_at_position(arr, 2, 25))
