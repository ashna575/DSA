def find_duplicates(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


arr = [4, 2, 4, 5, 2, 3, 1]
print("Array:", arr)
print("Duplicates:", find_duplicates(arr))
