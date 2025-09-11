arr = [1, 2, 3, 5]
n = len(arr) + 1   

sum = n * (n + 1) // 2
i= 0

for num in arr:
    i += num

missingNo = sum - i
print("Missing number:", missingNo)
