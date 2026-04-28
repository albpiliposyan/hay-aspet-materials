
import random

secret = random.randint(1, 100)


guess = int(input("Guess the number between 1 and 100: "))

while guess != secret:
    if guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < 0 or 100 < guess:
        print("Please enter a number between 1 and 100.")

print("Congratulations! You guessed the number.")
