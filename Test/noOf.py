# Program to count all characters in a string

text = input("Enter a string: ")

char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character frequencies:")
for key, value in char_count.items():
    print(f"'{key}' : {value}")
