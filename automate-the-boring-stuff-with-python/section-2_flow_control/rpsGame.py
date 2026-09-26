import random
import sys
# Print to the Screen
print('ROCK, PAPER, SCISSORS')
systemGuess = 0
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

# Counting Streaks
win = 0
lose = 0
tie = 0

# User Input
userGuess = input()
if userGuess == 'q':
    print('Thank you for using our Game!')
    sys.exit()
elif userGuess != 'r' and userGuess != 'p' and userGuess != 's':
    print('Illegal Guess entry, Exiting the Game')
    sys.exit()
elif userGuess == 'r':
    userGuess = 'ROCK'
elif userGuess == 'p':
    userGuess = 'PAPER'
elif userGuess == 's':
    userGuess = 'SCISSORS'

# System input
for systemGuess in range(1):
    systemGuess = random.randint(1, 3)
    # print(systemGuess)
    if systemGuess == 1:
        systemGuess = 'ROCK'
    elif systemGuess == 2:
        systemGuess = 'PAPER'
    elif systemGuess == 3:
        systemGuess = 'SCISSORS'

print(systemGuess + ' versus...')
print(userGuess)

if systemGuess == userGuess:
    print('It is a tie')
elif systemGuess == 'ROCK' and userGuess == 'PAPER':
    print('You win!')
elif systemGuess == 'ROCK' and userGuess == 'SCISSORS':
    print('Loser!')
elif systemGuess == 'SCISSORS' and userGuess == 'ROCK':
    print('You win!')
elif systemGuess == 'PAPER' and userGuess == 'ROCK':
    print('Loser!')
elif systemGuess == 'SCISSORS' and userGuess == 'PAPER':
    print('Loser!')
elif systemGuess == 'PAPER' and userGuess == 'SCISSORS':
    print('You win!')
