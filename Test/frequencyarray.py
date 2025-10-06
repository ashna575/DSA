arr = [2, 3, 2, 5, 3, 2]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
