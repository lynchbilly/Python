# Home Federal Savings Bank
# Implements a greeting system for a bank

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
