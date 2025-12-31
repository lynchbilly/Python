def main():
    # 1. Prompt user for greeting

    answer = input("Greeting: ").strip().lower()

    # 2. Check the greeting logic

    if answer.startswith("hello"):
        print("$0")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$100")
# End of main function
if __name__ == "__main__":
    main()