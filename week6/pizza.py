# Pizza Py
# Formats a pizza menu from a CSV file using tabulate

import sys
import csv
from tabulate import tabulate


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]
    
    # Check if file is a CSV file
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    # Try to open and read the CSV file
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            table = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    # Print the table using tabulate
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


if __name__ == "__main__":
    main()
