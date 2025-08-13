word = "bbabcbcab"
n = len(word)
palindrom = []

# Compare from start and end
for i in range(n // 2):
    left = word[i]
    right = word[n - 1 - i]
    
    if left == right:
        palindrom.append(left)   # add matching char from start
        palindrom.insert(0, right)  # add matching char from end at the start

print(palindrom)
    





