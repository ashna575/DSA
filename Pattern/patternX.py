rows = 7  # Must be odd for symmetrical X
for i in range(rows):
    for j in range(rows):
        if j == i or j == rows - 1 - i or j > min(i, rows - 1 - i) and j < max(i, rows - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    