def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Return True if plate meets Harvard's vanity plate requirements.
    Rules: 2-6 chars, starts with 2 letters, numbers at the end (first non-zero)"""
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False

    number_started = False
    # Numbers must be at the end and the first one cannot be '0'
    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                if char == "0":
                    return False
        else:
            if number_started:
                # If find a letter after a number has already started
                return False

    return True


if __name__ == "__main__":
    main()
