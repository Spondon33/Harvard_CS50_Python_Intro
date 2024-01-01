# import:

# importing libraries
import random

coin = random.choice(["heads", "tails"])
print(coin)


# from:

# imports the choice function from the random module
from random import choice

coin = choice(["heads", "tails"])
print(coin)


# randint:
import random

number = random.randint(1, 10)
print(number)


# shuffle:
import random

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)


# statistics library:
# mean function
import statistics

print(statistics.mean([100, 90]))
