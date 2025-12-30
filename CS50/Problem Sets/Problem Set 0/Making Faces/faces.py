def main():
    # 1. Get user input
   
    msg = input("Enter Hello :) or Goodbye:( or Rebel :P") 
    
    # 2. Convert the message using our helper function
    result = convert(msg)
    
    # 3. Print the final result to the terminal
    print(result)

def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    text = text.replace(":P", "😛")
    
    # Return the new string back to the main function
    return text

if __name__ == "__main__":
    main()