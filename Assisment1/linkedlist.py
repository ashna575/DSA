#assisment I
# # Question1 


def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    print(num_set)
    for num in num_set:
        # only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output: 4
