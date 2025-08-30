text = input("Enter a string: ")
k = input("Enter the character to count: ")

count = 0
for ch in text:
    if ch == k:
        count += 1

print(count)
