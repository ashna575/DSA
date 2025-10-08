def sum(n):
    while n > 9: 
        s = 0
        for digit in str(n):
            s += int(digit)
        n = s
    return n

num = 9875

print(sum(num))
