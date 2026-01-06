# Testing my twttr
# Tests for the twttr function that removes vowels

def shorten(word):
    result = ""
    vowels = "aeiouAEIOU"
    for char in word:
        if char not in vowels:
            result += char
    return result


def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


if __name__ == "__main__":
    main()
