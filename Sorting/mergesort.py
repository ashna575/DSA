def merge(arr, st, mid, end):
    temp = []
    i = st        
    j = mid + 1   
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    
    while i <= mid:
        temp.append(arr[i])
        i += 1
   
    while j <= end:
        temp.append(arr[j])
        j += 1
        
    for k in range(len(temp)):
        arr[st + k] = temp[k]


def merge_sort(arr, st, end):
    if st >= end:
        return
    mid = st + (end - st) // 2
    merge_sort(arr, st, mid)       
    merge_sort(arr, mid + 1, end) 
    merge(arr, st, mid, end)



nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums, 0, len(nums) - 1)
print("Sorted:", nums)
   