# Working 9 to 5
# Converts 12-hour time format to 24-hour format

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Pattern to match time range like "9:00 AM to 5:00 PM"
    pattern = r"^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$"
    match = re.match(pattern, s)
    
    if not match:
        raise ValueError
    
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()
    
    # Convert to integers
    hour1 = int(hour1)
    minute1 = int(minute1)
    hour2 = int(hour2)
    minute2 = int(minute2)
    
    # Validate hours and minutes
    if hour1 < 1 or hour1 > 12 or hour2 < 1 or hour2 > 12:
        raise ValueError
    if minute1 < 0 or minute1 > 59 or minute2 < 0 or minute2 > 59:
        raise ValueError
    
    # Convert to 24-hour format
    if period1 == "AM":
        if hour1 == 12:
            hour1 = 0
    else:  # PM
        if hour1 != 12:
            hour1 += 12
    
    if period2 == "AM":
        if hour2 == 12:
            hour2 = 0
    else:  # PM
        if hour2 != 12:
            hour2 += 12
    
    return f"{hour1:02d}:{minute1:02d} to {hour2:02d}:{minute2:02d}"


if __name__ == "__main__":
    main()
