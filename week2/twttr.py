# Just setting up my twttr
# Removes vowels from user input

text = input("Input: ")
output = ""

vowels = "aeiouAEIOU"

for char in text:
    if char not in vowels:
        output += char

print(f"Output: {output}")
