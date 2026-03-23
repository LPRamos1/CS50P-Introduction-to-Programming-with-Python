def main():
    user_input = input(f"Type a word: ")
    # Get the word without vowels and print it
    twttr = shorten(user_input)
    print(twttr)


def shorten(word):
    """Remove all vowels (uppercase and lowercase) from a given string.
    Returns the string with only consonants and other characters."""
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for w in word:
        if w not in vowels:
            no_vowels += w
    return no_vowels


if __name__ == "__main__":
    main()
