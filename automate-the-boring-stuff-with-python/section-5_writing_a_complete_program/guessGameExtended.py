import random
import math
import sys
import time


def quitGame():
    # Message to print when CTRL+C keys are pressed
    print('\nThanks for Playing, quiting the game...')
    sys.exit()


def showMessage(message, delayTime):
    # Print Message to the Screen, and wait for given time
    print(message)
    time.sleep(delayTime)


# Greeting the Player
try:
    print('Welcome to Guess the Number Game. \nYou can Quit the game any time by pressing CTRL+C keys on your keyboard')
    playerName = input('Hello, What is your name?\n').title()
    print(
        f"Well, {playerName}, let's choose our start and end values for the game.")
except KeyboardInterrupt:
    quitGame()


# Asking Player for Guessing Range and Error Checking
while True:
    try:
        lowerEndOfGuess = int(input('Choose your start number: '))
        higherEndOfGuess = int(input('Choose your end number: '))
        if lowerEndOfGuess > higherEndOfGuess:  # Otherwise our random function will fail
            print('Starting number should be less than ending number')
            continue
        break
    except ValueError:
        print('Only Intergers are allowed as a start and end values of a Guessing Game.')
    except KeyboardInterrupt:
        quitGame()


# Haing Fun and choosing the secret number
try:
    showMessage('Wait, a moment, I m gearing up for the battle.', 2)
    showMessage(
        "Don't be stupid.I'm not stuck. I'm still thinking of what number to choose!", 3)
    showMessage("Don't dare to Quit on me", 2.5)
    secretNumber = random.randint(lowerEndOfGuess, higherEndOfGuess)
    time.sleep(2.5)
    showMessage("Shshhhhhhh! I have chosen my MAGIC NUMBER!", 1.5)
    showMessage("It's your turn", 1.5)
except KeyboardInterrupt:
    quitGame()
# print(f"Debug: Secret Number is {secretNumber}")


# Calculating maximum number of possible guesses
totalGuesses = higherEndOfGuess - lowerEndOfGuess
maxPossibleGuesses = math.ceil(math.log2(totalGuesses))
print(f"You have {maxPossibleGuesses} guesses to Win the Game.")
time.sleep(1.5)


# Game Logic
for numberOFGuesses in range(1, maxPossibleGuesses+1):
    try:
        playerGuess = int(input('Take a Guess!\n'))
        if playerGuess < secretNumber:
            print('Your Guess is too low!')
        elif playerGuess > secretNumber:
            print('Your Guess is too high!')
        else:
            break
    except ValueError:
        print('Only integers are allowed as valid game guess.')
    except KeyboardInterrupt:
        quitGame()


# Ending the Game
try:
    if playerGuess == secretNumber:
        print(f'Good job,{playerName}! You guessed my number in {
            numberOFGuesses} guesses!')
    else:
        print(f"You lose! Number of guesses are exhausted. The number I was thinking of was {
              secretNumber}.")
except NameError:
    print('Please, try again, something went wrong!')
