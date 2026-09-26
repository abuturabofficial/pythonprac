import random
# Ask for Player name and greet them
playerName = input('Hello, What is your name?\n')
print(f"Well, {playerName}, I am thinking of a number between 1 and 20.")


secretNumber = random.randint(1, 20)
# print(f"Debug: Secret Number is {secretNumber}")


for numberOFGuesses in range(1, 7):  # Max number of Guesses allowed
    playerGuess = int(input('Take a Guess\n'))
    if playerGuess < secretNumber:
        print('Your Guess is too low.')
    elif playerGuess > secretNumber:
        print('Your Guess is too high')
    else:
        break


if playerGuess == secretNumber:
    print(f'Good job,{playerName}! You guessed my number in {
        numberOFGuesses} guesses!')
else:
    print(f"Nope. The number I was thinking of was {secretNumber}.")
