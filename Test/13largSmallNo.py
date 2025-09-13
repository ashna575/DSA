array = [22, 34, 53, 2, 44, 3, 42, 72]
larg = array[0]
small = array[0]
for i in array:
    if i < small:
        small = i
    if i > larg:
        larg = i    

print("Smallest No:", small)
print("Largest No:", larg)
