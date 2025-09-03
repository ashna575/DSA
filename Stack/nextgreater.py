def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res


print(next_greater([4, 5, 2, 25]))  # [5, 25, 25, -1]
