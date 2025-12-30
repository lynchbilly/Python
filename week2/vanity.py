# Vanity Plates
# Validates vanity license plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check first two characters are letters
    if not s[0:2].isalpha():
        return False
    
    # Check for invalid characters (only letters and numbers allowed)
    if not s.isalnum():
        return False
    
    # Check number placement
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            # First number cannot be '0'
            if not number_started and char == '0':
                return False
            number_started = True
        elif number_started:
            # No letters after numbers
            return False
    
    return True


main()
