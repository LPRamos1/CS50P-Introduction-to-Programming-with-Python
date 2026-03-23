import emoji


def main():
    x = input(f"Type phrase with emoji: ")
    print(emoji.emojize(f"{x}", language="alias"))


main()
