def merge_arrays(a, b):
    m, n = len(a), len(b)
    i, j = m - 1, 0

  
    while i >= 0 and j < n:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
        i -= 1
        j += 1

    
    a.sort()
    b.sort()

    return a + b
a = [2, 4, 7, 10]
b = [2, 3]
print("Merged array:", merge_arrays(a, b))
