##########################################
########  RPS GAME VERSION 3.0  ##########
##########################################
import random
import sys

# Print to the Screen Once
print("ROCK, PAPER, SCISSORS")
# Counting Streaks
wins = 0
losses = 0
ties = 0

# User Input

while True:
    # Print to the Screen
    systemGuess = 0
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    userGuess = input()
    if userGuess == "q":
        print("Thank you for playing our Game!")
        print(str(wins) + " Wins," + str(losses) +
              " Losses," + str(ties) + " Ties")
        sys.exit()
    elif userGuess != "r" and userGuess != "p" and userGuess != "s":
        print("Illegal Guess, Try again.")
        continue
    elif userGuess == "r":
        userGuess = "ROCK"
    elif userGuess == "p":
        userGuess = "PAPER"
    elif userGuess == "s":
        userGuess = "SCISSORS"
    # System input
    systemGuess = random.randint(1, 3)
    # print(systemGuess)
    if systemGuess == 1:
        systemGuess = "ROCK"
    elif systemGuess == 2:
        systemGuess = "PAPER"
    elif systemGuess == 3:
        systemGuess = "SCISSORS"

    print(systemGuess + " versus...")
    print(userGuess)

    if systemGuess == userGuess:
        print("It is a tie")
        ties = ties + 1
        print(str(wins) + " Wins," + str(losses) +
              " Losses," + str(ties) + " Ties")
    elif (
        (systemGuess == "ROCK" and userGuess == "PAPER")
        or (systemGuess == "SCISSORS" and userGuess == "ROCK")
        or (systemGuess == "PAPER" and userGuess == "SCISSORS")
    ):
        print("You win!")
        wins = wins + 1
        print(str(wins) + " Wins," + str(losses) +
              " Losses," + str(ties) + " Ties")
    elif (
        (systemGuess == "ROCK" and userGuess == "SCISSORS")
        or (systemGuess == "PAPER" and userGuess == "ROCK")
        or (systemGuess == "SCISSORS" and userGuess == "PAPER")
    ):
        print("Loser!")
        losses = losses + 1
        print(str(wins) + " Wins," + str(losses) +
              " Losses," + str(ties) + " Ties")
