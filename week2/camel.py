# camelCase to snake_case
# Converts camelCase variable names to snake_case

camel = input("camelCase: ")
snake = ""

for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char

print(f"snake_case: {snake}")
