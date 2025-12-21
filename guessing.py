import random

number = random.randint(1, 10)
guess = 0

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess > number:
        print("Too high ❌")
    elif guess < number:
        print("Too low ❌")
    else:
        print("🎉 Congratulations! You guessed it right 🎉")