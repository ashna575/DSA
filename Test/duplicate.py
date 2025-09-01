arr = [2, 3, 45, 3, 42, 2, 44, 5]

duplicate= []
for x in arr:
    if x not in duplicate:   
        duplicate.append(x)

print("Original array:", arr)
print(" removing duplicates:", duplicate)




#output Original array: [2, 3, 45, 3, 42, 2, 44, 5]
 #removing duplicates: [2, 3, 45, 42, 44, 5]