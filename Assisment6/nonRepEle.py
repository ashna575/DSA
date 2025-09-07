s = "swiss"

# Step 1: Create frequency dictionary
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: Find first character with frequency 1
result = None
for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print("First non-repeating character:", result)
