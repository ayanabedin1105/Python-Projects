randNum = 7

guess = int(input("Enter a number: "))

while randNum != guess:
    if guess < randNum:
        print("Too low. Try again.")
        guess = int(input("Enter a number: "))
    elif guess > randNum:
        print("Too high. Try again.")
        guess = int(input("Enter a number: "))
    else:
        break

print("ahha!You guessed it right.")

