
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


# sys: this module gives access to
# the values typed in the command line
# argv aka Argument Vector: this is function of the sys module
# argv is a list of all of the word typed by the user in prompt.
import sys

print("hello, my name is", sys.argv[1])


# handeling errors such as indexerror
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# using conditionals to handle errors
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


# sys.exit = will exit the program.
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


# Slices: in sys.argv[1:], [1:] will slice the first element
# of the list and start from the second element to the end
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# [1:] will start from the second element to the end
for arg in sys.argv[1:]:
    print("hello, my name is", arg)


import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# [1:] will start from the second element to the end
# -1 will start from last and omit the last element
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)


# packages
# cowsay :
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])


# APIs helps to get specific datas from any servers
# requests : requests to get specific datas from any servers
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/%20search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# json.dumps organizes those datas and make them more readable
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/%20search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))


# retrieving specific datas
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/%20search?entity=song&limit=1&term=" + sys.argv[1])

obj = response.json()
for result in obj["results"]:
    print(result["trackName"])

import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


