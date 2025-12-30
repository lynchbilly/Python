# FIGlet
# Outputs text in ASCII art using pyfiglet

import sys
import pyfiglet
import random

if len(sys.argv) == 1:
    # No arguments: random font
    font = random.choice(pyfiglet.FigletFont.getFonts())
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # Font specified
    font = sys.argv[2]
    if font not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")
figlet = pyfiglet.Figlet(font=font)
print(figlet.renderText(text))
