
# def guess_game():
#     print("🎮 Welcome to the 2-Player Guessing Game!")
#     n = int(input("Enter the maximum number (n): "))

#     # User A inputs the number to be guessed (hidden from User B)
#     print("\nUser A, enter the number to be guessed (1 to", n, "):")
#     while True:
#         pick = int(input("Enter your number (User B should not look!): "))
#         if 1 <= pick <= n:
#             break
#         else:
#             print("Please enter a valid number between 1 and", n)

#     print("\n" * 50)  
#     print("User B, it's your turn to guess the number!")

#     attempts = 0
#     while True:
#         guess = int(input("Your guess: "))
#         attempts += 1

#         if guess > pick:
#             print("Too high! Try a smaller number.")
#         elif guess < pick:
#             print("Too low! Try a bigger number.")
#         else:
#             print(f"🎉 Correct! You guessed it in {attempts} attempts.")
#             break

# # Run it
# guess_game()

import random

# Generate a random number between 1 and 100
picked_number = random.randint(1, 100)

# Welcome message
print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until user guesses correctly
while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < picked_number:
            print("Too low! Try a higher number. ⬆️")
        elif guess > picked_number:
            print("Too high! Try a lower number. ⬇️")
        else:
            print("🎉 Correct! You guessed the number.")
            break
    except ValueError:
        print("❌ Please enter a valid integer.")


          
           
           