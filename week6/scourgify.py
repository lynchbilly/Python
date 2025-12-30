# Scourgify
# Reorganizes student data from one CSV to another

import sys
import csv


def main():
    # Check command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if files are CSV files
    if not input_file.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    # Try to open and read the input CSV file
    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            students = []
            
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    
    # Write to the output CSV file
    with open(output_file, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()
