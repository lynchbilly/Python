# Adieu, Adieu
# Bids adieu to names using inflect library for proper grammar

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

output = p.join(names)
print(f"Adieu, adieu, to {output}")
