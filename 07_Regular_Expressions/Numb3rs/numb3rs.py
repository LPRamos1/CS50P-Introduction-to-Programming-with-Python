import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validate IPv4 addresses (format: #.#.#.#).
    Ensures numbers are between 0-255 and prohibits leading zeros (e.g., 01.1.1.1).
    """
    # Regex handles format,dots and prohibits leading zeros
    if not re.search(r"^((0|[1-9]\d{0,2})\.){3}(0|[1-9]\d{0,2})$", ip):
        return False
    for p in ip.split("."):
        # Validade that each number is no larger than 255
        if int(p) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
