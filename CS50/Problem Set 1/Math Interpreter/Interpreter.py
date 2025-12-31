def main():
    # 1. Get the expression from the user
    expression = input("Expression: ").strip()

    # 2. Split the string into three parts: x, y, and z
    # If the user types "1 + 1", x="1", y="+", z="1"
    x_str, y, z_str = expression.split(" ")

    # 3. Convert x and z to floats so we can do math
    x = float(x_str)
    z = float(z_str)

    # 4. Perform the calculation based on the operator y
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # 5. Output the result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()