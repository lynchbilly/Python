def main():
    # 1. Get user input
    # Note: Keep input empty if you are running 'check50'
    msg = input("Try :) :( :P :D <3 or ;) -> ") 
    
    # 2. Convert the message
    result = convert(msg)
    
    # 3. Print the final result
    print(result)

def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    
    # Added Options
    text = text.replace(":P", "😛")
    text = text.replace(":D", "😁")
    text = text.replace("<3", "❤️")
    text = text.replace(";)", "😉")
    text = text.replace("!!!", "❗")
    
    return text


if __name__ == "__main__":
    main()