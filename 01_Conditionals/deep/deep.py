x = input("What is the great question of life ?").strip().lower()


def main():
    if x in ("42", "forty-two", "forty two"):
        print("Yes")
    else:
        print("No")


main()
