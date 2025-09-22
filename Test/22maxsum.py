def max_sum(array):
    s = array[0]
    i = array[0]
    for j in range(1, len(array)):
        i = max(array[j], i + array[j])
        s = max(s, i)
    return s   

array = [34, -50, 42, 14, -5, 86]
print(max_sum(array))
