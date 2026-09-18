import random

# # Coin flip using random.choice(seq)
# coin = random.choice(["head", "tail"])
# print(coin)


# # Choose a random number between given range using random.randint(a, b)
# num = random.randint(1, 100)
# print(num)


# Shuffling the items using random.shuffle(x)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
