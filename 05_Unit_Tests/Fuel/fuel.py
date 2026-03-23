def main():
    while True:
        user_input = input("Fraction: ")
        try:
            # Convert fraction string to integer percentage
            percentage = convert(user_input)
            # Get the formatted gauge output
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    """
    Convert a fraction string (X/Y) into a percentage.
    Raises ValueError for invalid fractions or ZeroDivisionError if Y is 0.
    """
    numerator, denominator = fraction.split("/")
    n = int(numerator)
    d = int(denominator)
    # Validate the fraction based on fuel gauge rules
    if d == 0:
        raise ZeroDivisionError
    if n < 0 or d < 0 or n > d:
        raise ValueError
    return round((n / d) * 100)


def gauge(percentage):
    """Return the status of the fuel tank as a string:
    'E' for <= 1%, 'F' for >= 99%, or the percentage value."""
    if percentage <= 1:
        return(f"E")
    elif percentage >= 99:
        return(f"F")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
