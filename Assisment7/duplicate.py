color = []
duplicate = []

n=int(input("enter the size of array:"))
for i in range(n):
    a = input("Enter your fav color: ")
    color.append(a)


for j in color:
    if color.count(j) > 1 and j not in duplicate:
        duplicate.append(j)
       

print("All Colors:", color)
print("Duplicate Colors:", duplicate)

