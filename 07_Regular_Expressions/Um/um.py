import re


def main():
    user_input = input("Text: ")
    print(count(user_input))


def count(s):
    """
    Counts the word 'um' as a standalone word, case-insensitively.
    """
    # \b guaranteed "um" as isolated word
    um_count = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_count)


if __name__ == "__main__":
    main()
