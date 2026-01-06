# Math Interpreter
# Interprets and evaluates simple math expressions

expression = input("Expression: ")
x, operator, z = expression.split()

x = float(x)
z = float(z)

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z

print(f"{result:.1f}")
