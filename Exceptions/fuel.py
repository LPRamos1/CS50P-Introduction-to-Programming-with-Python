def main():

    x = get_fraction()
    if x <= 1:
        print(f"E")
    elif x >= 99:
        print(f"F")
    else:
        print(f"{x}%")


def get_fraction():
    while True:
        try:
            x = input("Type the fraction of the fuel? ")
            numerator, denominator = x.split("/")
            numerator = int(numerator)
            denominator = int(denominator)

            if denominator <= 0:
                continue
            if numerator < 0:
                continue
            if numerator > denominator:
                continue
            return round((numerator / denominator) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()
