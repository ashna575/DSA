num = 36
i = 1

while i * i <= num:
    if i * i == num:
        print(num, "is a perfect square")
        break
    i += 1
else:
    print(num, "is not a perfect square")
