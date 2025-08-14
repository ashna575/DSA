fruits = ["mango", "apple", "orange"]

longest = fruits[0]   
for fruit in fruits:
    if len(fruit) > len(longest):
        longest = fruit

print("Longest string:", longest)
        