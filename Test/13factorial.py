def factorial(k):
    fact = 1
    for i in range(1, k + 1):   
        fact = fact * i
    return fact

k = int(input("Enter a number = "))
print(factorial(k))
