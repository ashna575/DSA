text = input("Enter a string: ")
reverse = text.replace(" ", "").lower()

is_palindrome = True

for i in range(len(reverse) // 2):
    if reverse[i] != reverse[len(reverse) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Yes! It is a palindrome.")
else:
    print("No! It is not a palindrome.")
