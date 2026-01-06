# Regular, um, Expressions
# Counts occurrences of "um" as a word

import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Pattern to match "um" as a whole word (case-insensitive)
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
