months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) < 1 or int(month) > 12:
                raise ValueError
            if int(day) < 1 or int(day) > 31:
                raise ValueError
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            month_day, year = [part.strip() for part in date.split(",")]
            month, day = month_day.split(" ")
            month = months.index(month.title()) + 1
            if month < 1 or month > 12:
                raise ValueError
            if int(day) < 1 or int(day) > 31:
                raise ValueError
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except ValueError:
        pass
