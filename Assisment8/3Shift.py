def shift_array(arr, k, direction="right"):
    n = len(arr)
    k = k % n  
    
    if direction == "right":
        return arr[-k:] + arr[:-k]
    elif direction == "left":
        return arr[k:] + arr[:k]
    else:
        print("Invalid direction (use 'right' or 'left')")
        return arr


arr = [1, 2, 3, 4, 5]
print("Right Shift by 2:", shift_array(arr, 2, "right"))
print("Left Shift by 2:", shift_array(arr, 2, "left"))
