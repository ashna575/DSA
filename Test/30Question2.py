def No_count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

arr = [1,1,1,3,4,2,1,1]
a = No_count(arr)
n = len(arr) / 2

for key, value in a.items():
    if value > n:
        print( key)
       

