# Guessing Game
# Implements a number guessing game

import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
