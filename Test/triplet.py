def countTriplets(arr):
    arr = list(set(arr)) 
    arr.sort()
    s = set(arr)  
    triplets = set()

    n = len(arr)
    for i in range(n):
        for j in range(i+1, n): 
            a, b = arr[i], arr[j]
            c = a + b
            if c in s:
                triplets.add((a, b, c))  

    return len(triplets), triplets



arr = [1, 5, 3, 2]
count, triplets = countTriplets(arr)
print("Count:", count)
print("Triplets:", triplets)
