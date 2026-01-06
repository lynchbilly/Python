# Emojize
# Converts emoji codes to actual emoji using the emoji library

import emoji

text = input("Input: ")
output = emoji.emojize(text, language="alias")
print(f"Output: {output}")
