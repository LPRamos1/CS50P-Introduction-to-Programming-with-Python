from bank import value


def test_hello():
    assert value(" HeLLo ") == 0


def test_h_start():
    assert value("    hI ") == 20


def test_other():
    assert value(" Testing ") == 100
