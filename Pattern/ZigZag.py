
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(i*m + j + 1, end="\t")
        else:
            print(i*m + (m-j), end="\t")
    print()
