import random


gameRunning = True


user_input=input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:")

computer = random.choice(["r","p","s"])

while (user_input != "r") and (user_input != "p") and (user_input != "s"):
    print("Invalid input, try again")
    user_input=input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:")

else:
    print("You have seclected :", user_input,"The computer has selected:",computer)