import random

while True:
    userChoice = input("Please choose (rock/ paper/ scissor): ")
    computerChoice = random.choice(["rock", "paper", "scissor"])

    print("You choose " + userChoice + " and the computer chose " + computerChoice)

    if userChoice == computerChoice:
        print(f"Both players chose {computerChoice}. It's a tie!")
    if userChoice == "rock":
        if computerChoice == "scissor":
            print("Rock crushes scissor. You win!")
        else:
            print("Paper covers rock. You lose!")
    elif userChoice == "paper":
        if computerChoice == "rock":
            print("Paper covers rock. You win!")
        else:
            print("Scissor cuts paper. You lose!")
    elif userChoice == "scissor":
        if computerChoice == "paper":
            print("Scissor cuts paper! You win")
        else:
            print("Rock smashes scissor! You lose.")

    repeat = input("Play again? (y/n): ")
    if repeat.lower() != "y":
        print("Bye!")
        break
    