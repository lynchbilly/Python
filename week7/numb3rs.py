# NUMB3RS
# Validates IPv4 addresses using regular expressions

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Pattern for IPv4 address
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, ip)
    
    if match:
        # Check if each octet is between 0 and 255
        for i in range(1, 5):
            octet = int(match.group(i))
            if octet < 0 or octet > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
