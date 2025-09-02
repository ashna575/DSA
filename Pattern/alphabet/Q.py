def print_q_pattern(n):
    for i in range(n):
        for j in range(n):
            # Top row
            if (i == 0 and j > 0 and j < n - 1):
                print("*", end=" ")
            # Bottom row
            elif (i == n - 2 and j > 0 and j < n - 1):
                print("*", end=" ")
            # Left column
            elif (j == 0 and i > 0 and i < n - 2):
                print("*", end=" ")
            # Right column
            elif (j == n - 1 and i > 0 and i < n - 2):
                print("*", end=" ")
            # Diagonal tail of Q
            elif (i == j and i >= n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Example: size 7
print_q_pattern(7)
