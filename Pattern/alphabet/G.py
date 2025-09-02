def print_g_pattern(n):
    for i in range(n):
        for j in range(n):
            # Top row
            if i == 0 and j > 0:
                print("*", end=" ")
            # Left column
            elif j == 0 and i > 0 and i < n - 1:
                print("*", end=" ")
            # Bottom row
            elif i == n - 1 and j > 0:
                print("*", end=" ")
            # Middle horizontal line (for G's inside bar)
            elif i == n // 2 and j >= n // 2:
                print("*", end=" ")
            # Right side vertical (for lower half)
            elif j == n - 1 and i >= n // 2 and i < n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Example: size 7
print_g_pattern(7)
