def occurrences(arr, x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count

arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6]
x = 5
print("Occurrences of", x, ":", occurrences(arr, x))