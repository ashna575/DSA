
num = int(input("Enter a number: "))
p = len(str(num))
sum_of_powers= 0
a = num

while a> 0:
    digit = a % 10
    sum_of_powers += digit **p
    temp //= 10


if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
