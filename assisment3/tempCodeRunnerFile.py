def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n):
    low = 1
    high = n
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        result = guess(mid)
        steps += 1

        print(f"Step {steps}: Guess = {mid}, ", end="")
        
        if result == 0:
            print("Correct!")
            return mid
        elif result == -1:
            print("Too high")
            high = mid - 1
        else:
            print("Too low")
            low = mid + 1

# # Example usage
pick = 7  # You can change this for testing
n = 100
print(f"\n The number to guess is: {pick}")
result = guessNumber(n)
print(f"✅ Found number {result} using binary search.")

  