from random import randint

secretNumber = randint(1, 20)
# print(secretNumber)  # Debuging purposes only
print("I am thinking of a number between 1 and 20.")
# guess = ''
numberOfGuesses = 0
while True:
    guess = int(input("Take a Guess: "))
    numberOfGuesses = numberOfGuesses + 1
    if guess < secretNumber:
        print("Your Guess is too low.")
    elif guess > secretNumber:
        print("Your Guess is too high")
    else:
        break

print("Good job! You guessed my number in " +
      str(numberOfGuesses) + " guesses!")
