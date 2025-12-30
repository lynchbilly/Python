# Seasons of Love
# Calculates a person's age in minutes

from datetime import date
import inflect
import sys


def main():
    # Get date of birth from user
    dob = input("Date of Birth: ")
    
    try:
        # Parse the date
        year, month, day = dob.split("-")
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    
    # Calculate age in minutes
    today = date.today()
    age_in_days = (today - birth_date).days
    age_in_minutes = age_in_days * 24 * 60
    
    # Convert to words
    p = inflect.engine()
    words = p.number_to_words(age_in_minutes, andword="")
    
    # Capitalize first letter and print
    print(f"{words.capitalize()} minutes")


if __name__ == "__main__":
    main()
