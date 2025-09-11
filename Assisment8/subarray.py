arr = [1, 2, 0, 3]
n = len(arr)

total = sum(arr)
left_sum = 0

equindex = -1

for i in range(n):
  
    if left_sum == (total - left_sum - arr[i]):
        equindex = i
        break
    left_sum += arr[i]

print("Equilibrium Index:", equindex)

        