# Outdated
# Converts dates from month-day-year to year-month-day format

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()
        
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        else:
            parts = date.replace(",", "").split()
            if len(parts) != 3:
                continue
            month_name, day, year = parts
            if month_name not in months:
                continue
            month = months.index(month_name) + 1
            day = int(day)
            year = int(year)
        
        if month < 1 or month > 12 or day < 1 or day > 31:
            continue
        
        print(f"{year:04d}-{month:02d}-{day:02d}")
        break
        
    except (ValueError, IndexError):
        pass
