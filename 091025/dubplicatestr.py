
string = input("Enter a string: ")

result = ""
for i in string:
    if i not in result:
        result += i

print( result)
