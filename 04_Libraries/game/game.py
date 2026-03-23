from random import randint


def main():
    n = get_level()
    rad = randint(1, n)
    while True:
        guess = get_guess()
        if guess < rad:
            print("Too small!")
        elif guess > rad:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l > 0:
                return l
            else:
                continue
        except ValueError:
            continue


def get_guess():
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                return g
            else:
                continue
        except ValueError:
            continue


main()
