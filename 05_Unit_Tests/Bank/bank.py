def main():
    user_input = input("Word or phrase: ")
    result = value(user_input)
    print (f"${result}")


def value(greeting):
    """Return 0, 20 or 100 depending on the greeting content. """
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
