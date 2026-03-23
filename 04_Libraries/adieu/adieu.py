names = []


def main():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    if len(names) == 2:
        print(f"Adieu, adieu, to {' and '.join(names)}")
    if len(names) >= 3:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")


main()
