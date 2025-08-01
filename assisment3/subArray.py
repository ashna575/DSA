def max_candies(jars):
    max_candies = jars[0]
    current_candies = jars[0]

    for i in range(1, len(jars)):
        current_candies = max(jars[i], current_candies + jars[i])
        max_candies = max(max_candies, current_candies)

    return max_candies




nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_candies(nums))
