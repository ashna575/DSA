def sum_and_average(arr):
    total = 0
    for i in arr:
        total += i
    avg = total / len(arr)
    return total, avg


arr = [5, 10, 15, 20, 25]
s, a = sum_and_average(arr)
print("Array:", arr)
print("Sum:", s, " Average:", a)
