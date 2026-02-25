def main():
    camel = input("Name of a variable in camel case\n")
    snake = ""
    for letter in camel:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    print("snake_case:", snake)


main()
