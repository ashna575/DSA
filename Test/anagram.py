
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

list1 = list(str1)

is_anagram = True
for i in str2:
        if i in list1:
            list1.remove(i)
        else:
            is_anagram = False
            break
if is_anagram and not list1:
        print(" it is a anagram.")
else:
        print("it is not a anagrams.")

