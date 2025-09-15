# Spiral Number Square Pattern

n = int(input("Enter size: "))

# initialize empty matrix
matrix = [[0]*n for _ in range(n)]

num = 1
top, left = 0, 0
bottom, right = n-1, n-1

while top <= bottom and left <= right:
    # top row
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1

    # right column
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # bottom row
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    # left column
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    for val in row:
        print(f"{val:3}", end=" ")
    print()
