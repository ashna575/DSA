# rows = 5
# # Upper half
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))
# # Lower half
# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))



rows = 5
for i in range(1, rows + 1):
   print(" " * (rows - i) + "*a" * i)
row = 5
for i in range(1, row + 1):
  print(" " * (row-i) + "* " * i)
row = 5
for i in range(1, row + 1):
  print(" " * (row-i) + "*" * i)