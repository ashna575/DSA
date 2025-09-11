# given two array a and b of size n and m ,merge them in sorted order  .
# Modify a[] array such that it cointain n element and b[] cointain m element

a = [2, 4, 7, 10]
b = [2, 3]

n = len(a)
m = len(b)

i = n - 1  
j = 0

while i >= 0 and j < m:
    if a[i] > b[j]:
        a[i], b[j] = b[j], a[i]
    i -= 1
    j += 1


a.sort()
b.sort()

print(a)   
print(b)   
