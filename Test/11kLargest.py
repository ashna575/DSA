arr = [7, 10, 4, 3, 20, 15]
k = 3
n = len(arr)


for i in range(k):  
    index = i
    for j in range(i+1, n):
        if arr[j] < arr[index]:
            index = j
  
    arr[i], arr[index] = arr[index], arr[i]

print("3rd largest element:",arr[k-1])
