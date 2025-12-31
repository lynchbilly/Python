def main():
    # 1. Get user input and "clean" it
    # .strip() removes accidental spaces, .lower() ignores capitalization
    answer = input("What is the answer to life, the universe and everything? ").strip().lower()

    # 2. Check the answer against Strings
    # Note how we use quotes around "42" to match the input type
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

# This line tells Python to execute the main function
if __name__ == "__main__":
    main()