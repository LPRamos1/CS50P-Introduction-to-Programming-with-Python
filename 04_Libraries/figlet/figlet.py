import sys
import random
from pyfiglet import Figlet


def main():
    f = Figlet()

    # Random font
    if len(sys.argv) == 1:
        font = random.choice(f.getFonts())
    # -f or --font
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in f.getFonts():
            sys.exit("Invalid Font")
    else:
        sys.exit("Not in the correct format.")

    f.setFont(font=font)
    text = input("Type something: ")
    print(f.renderText(text))


main()
