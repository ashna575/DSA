arr = [0, 1, 0, 1, 1, 1, 1]
count = 0
maxNo = 0

for i in arr:
    if i == 1 or 0:
        count += 1
        maxNo = max(maxNo, count)
    else:
        count = 0

print(maxNo)
    