import re

def camel_to_snake(name):
    # Insert an underscore before any uppercase letter that is followed by a lowercase letter,
    # or before an uppercase letter that follows a lowercase letter.
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    # Convert the entire string to lowercase
    return s.lower()

# Example usage with user input:
user_input = input("Enter a string in camel case: ")
snake_case_output = camel_to_snake(user_input)

print(f"Original input: {user_input}")
print(f"Snake case output: {snake_case_output}")
