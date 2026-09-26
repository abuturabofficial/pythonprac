import random

numberOfStreaks = 0

coinFlip = ['H', 'T']

# Repeat coinFlip experiment 10000 times
for experimentNumber in range(10000):
    flipList = []
    currentStreak = 1
    previousFlip = None

    # Generate a list of 100 random coin flips
    for i in range(100):
        # Generate a list of 10000 coin flips
        flipResult = random.choice(coinFlip)
        flipList.append(flipResult)

    # Record no. of 6 streaks in 10000 experiments of 100 coins random flips
    for flip in flipList:
        if flip == previousFlip:
            currentStreak += 1
        else:
            currentStreak = 1
        if currentStreak == 6:
            numberOfStreaks += 1
            break
        previousFlip = flip


print(f"The percentage is: {round((numberOfStreaks / 10000) * 100, 2)}%")
