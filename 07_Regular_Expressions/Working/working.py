import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Converts a range of time from 12-hour format to 24-hour format.

    Expects a string with two time stamps separated by ' to '.
    Hours must be between 1-12 and minutes (optional) between 00-59.
    AM/PM suffix is mandatory and must be preceded by a space.
    """
    pattern = r"^([1-9]|1[0-2])(?::([0-5]\d))?(?:\s(AM|PM)) to ([1-9]|1[0-2])(?::([0-5]\d))?(?:\s(AM|PM))$"
    if matches := re.search(pattern, s):
        # Unpack match groups into descriptive variables for clarity
        hour1, min1, suffix1 = int(matches.group(1)), matches.group(2), matches.group(3)
        hour2, min2, suffix2 = int(matches.group(4)), matches.group(5), matches.group(6)

        # Convert each timestamp to 24-hour format
        time1 = format_24h(hour1, min1, suffix1)
        time2 = format_24h(hour2, min2, suffix2)

        return f"{time1} to {time2}"
    # Raise an error if the input doesn't match the expected pattern
    raise ValueError


def format_24h(hour, minutes, suffix):
    """Converts 12-hour format to 24-hour format."""

    # Default to "00" if minutes are not provided in the input
    if minutes is None:
        minutes = "00"
    # Handle PM and AM edge cases for 24-hour conversion
    if suffix == "PM" and hour != 12:
        hour += 12
    elif suffix == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minutes}"


if __name__ == "__main__":
    main()
