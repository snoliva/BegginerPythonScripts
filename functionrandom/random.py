# Simple number guessing game
# Allow the user to guess a random number between 1 and 100
# The program will give hints to the user after each guess

import random

secret_number = random.randint(1,100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")