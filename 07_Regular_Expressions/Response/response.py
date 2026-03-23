from validators import email

"""
Testing the "validators" library
"""


def main():
    user_email = input("What's your email address? ")
    if email(user_email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
