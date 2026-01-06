# Lines of Code
# Counts the lines of code in a Python file (excluding comments and blank lines)

import sys


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]
    
    # Check if file is a Python file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    
    # Try to open and read the file
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    # Count lines of code
    count = 0
    for line in lines:
        stripped = line.strip()
        # Skip blank lines and comments
        if stripped and not stripped.startswith("#"):
            count += 1
    
    print(count)


if __name__ == "__main__":
    main()
