word = "bbabcbcab"
n = len(word)
palindrom = []

for i in range(n // 2):
    left = word[i]
    right = word[n - 1 - i]
    
    if left == right:
        palindrom.append(left)                                     
        palindrom.insert(0, right)                                                                        # add matching char from end at the start

print(palindrom)
    





