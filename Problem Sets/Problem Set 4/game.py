import random

while True:
    try:
        user_input = int(input("Level: "))
        if user_input > 0:
            break
    except ValueError:
        pass

n = user_input
target = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > target:
            print("Too large!")
        elif guess < target:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
