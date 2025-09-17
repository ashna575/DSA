def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


array = [2, 4, 2, 1, 45, 4, 2, 2]
array = [2, 4, 2, 1, 45, 4, 2, 2]
array = [2, 4, 2, 1, 45, 4, 2, 2]

s = frequency(array)
print("Frequencies:", s)

for i in s:
    if s[i] > len(array) / 2: 
        print(i)

# print("Frequency dictionary:", frequency(array))
