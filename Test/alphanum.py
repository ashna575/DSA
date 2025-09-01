# Program to remove symbols from string and keep only alphanumeric characters

text = input("Enter a string: ")

result = ""
for ch in text:
    if ch.isalnum():   # checks if character is alphabet or number
        result += ch

print("String after removing symbols:", result)
