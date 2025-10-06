def second_larg(arr):
   
    arr = list(set(arr))  
    arr.sort()

    if len(arr) < 2:
        return "false"
    return arr[-2]

arr = [12, 35, 1, 10, 34, 1]
print(second_larg(arr))
