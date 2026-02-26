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
    "December",
]


def main():
    while True:
        try:
            date = input(f"What date (MM/DD/YEAR) or Month Day, Year? ")
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
            else:
                month_str, rest = date.split(" ", 1)
                day, year = rest.split(",")
                if month_str not in months:
                    continue
                month = months.index(month_str) + 1
                day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year.strip()}-{month:02}-{day:02}")
                break
        except ValueError:
            continue


main()
