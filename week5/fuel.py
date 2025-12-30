# Refueling
# Tests for fuel gauge with exception handling

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            
            return round((x / y) * 100)
            
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
