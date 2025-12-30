def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    else:
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")


def recommend(game):
    print("You might like", game)


main()
