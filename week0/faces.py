# Making Faces
# Converts :) and :( to 🙂 and 🙁

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    message = input()
    print(convert(message))


main()
