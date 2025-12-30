import random

cards = ["jack", "queen", "king"]


def main():
    print(random.choices(cards, k=2))


main()
