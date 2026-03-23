from plates import is_valid


# Testing -> Start with number AND numbers in middle of the plate.
def test_two_and_middle():
    assert is_valid("1AD111") == False
    assert is_valid("AAB1CD") == False


# Testing:  2 > Lenght or Lenght > 6.
def test_lower2_greater6():
    assert is_valid("A") == False
    assert is_valid("ABCD123") == False


# Testing start with two letters.
def test_beginning_alpha():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("12") == False


# Testing special chars.
def test_periods_space_etc():
    assert is_valid("AAA.23") == False
    assert is_valid("AAA 23") == False
    assert is_valid("AAA@23") == False


# Testing first-number 0.
def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


# Testing numbers in the middle and first number 0.
def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False


# Testing Valid plates.
def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("ECTO1") == True
    assert is_valid("NRVOUS") == True
