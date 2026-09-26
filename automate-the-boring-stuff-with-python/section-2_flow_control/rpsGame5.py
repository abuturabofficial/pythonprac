##########################################
########  RPS GAME VERSION 5.0  ##########
##########################################

import random
import sys

# Print to the Screen Once
print("ROCK, PAPER, SCISSORS")

# Counting Streaks
wins = 0
losses = 0
ties = 0

while True:
    # Print to the Screen
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

    # User Input
    userMove = input()
    if userMove == "q":
        print(f"Thank you for playing our Game!\n {
              wins} Wins, {losses} losses, {ties} Ties")
        sys.exit()
    elif userMove != "r" and userMove != "p" and userMove != "s":
        print("Illegal Guess, Try again.")
        continue
    elif userMove == "r":
        userMove = "ROCK"
    elif userMove == "p":
        userMove = "PAPER"
    elif userMove == "s":
        userMove = "SCISSORS"

    # System input
    systemMove = random.randint(1, 3)
    if systemMove == 1:
        systemMove = "ROCK"
    elif systemMove == 2:
        systemMove = "PAPER"
    elif systemMove == 3:
        systemMove = "SCISSORS"

    # Showing the Played Moves
    print(f"{systemMove} vs. {userMove}")

    # Game Logic
    if systemMove == userMove:
        print("It is a tie")
        ties = ties + 1
    elif (
        (systemMove == "ROCK" and userMove == "PAPER")
        or (systemMove == "SCISSORS" and userMove == "ROCK")
        or (systemMove == "PAPER" and userMove == "SCISSORS")
    ):
        print("You win!")
        wins = wins + 1
    elif (
        (systemMove == "ROCK" and userMove == "SCISSORS")
        or (systemMove == "PAPER" and userMove == "ROCK")
        or (systemMove == "SCISSORS" and userMove == "PAPER")
    ):
        print("Loser!")
        losses = losses + 1
