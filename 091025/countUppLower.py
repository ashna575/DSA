
string = input("Enter a string: ")

upper = 0
lower = 0


for char in string:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1


print("Number of uppercase", upper)
print("Number of lowercase ", lower)
