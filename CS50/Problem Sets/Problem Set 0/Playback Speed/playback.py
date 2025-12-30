import sys

def main():
    # Prompt the user for input
    user_input = input("Enter some text: ")

    # Replace each space with a hyphen
    user_input = user_input.replace(" ", ".-")

    # Print the output
    print(user_input)

if __name__ == "__main__":
    main()