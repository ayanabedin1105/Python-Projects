import random

randNum = random.randrange(1, 10)

guess = int(input("Enter a number: "))

while guess != randNum:
    if guess < randNum:
        print("Too low! Try again.")
        guess = int(input("Enter a number: "))
    elif guess > randNum:
        print("Too high! Try again.")
        guess = int(input("Enter a number: "))
    else:
        break

print("Ahha! You guessed it right!")