def main():
    # 1. Choose your soda with case insensitive input handling
    while True:
        # Convert to lowercase and remove whitespace immediately
        soda_input = input("Choose your drink: ").strip().lower()
        
        # Check against a lowercase list
        valid_sodas = ["coke", "pepsi", "sprite", "dr. pepper"]
        
        if soda_input in valid_sodas:
            # Format for the final display (e.g., "coke" becomes "Coke")
            soda_name = soda_input.title()
            print(f"Excellent choice! That will be 50 cents for your {soda_name}.")
            break 
        else:
            print("Invalid choice. Please choose Coke, Pepsi, Sprite, or Dr. Pepper.")

    # 2. Payment Logic 
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert coin (25, 10, 5): "))
            if coin in [25, 10, 5]:
                amount_due -= coin
        except ValueError:
            # This prevents the program from crashing if a user types a letter instead of a number
            continue
            
    # 3. Dispense
    print(f"Dispensing {soda_name}. Enjoy!")
    if amount_due < 0:
        print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()