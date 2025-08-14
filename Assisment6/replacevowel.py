word = "mango"
vowels = "aeiou"

result = ""
for i in word:
    if i in vowels:
        result += "0"
    else:
        result += i

print(result) 
  