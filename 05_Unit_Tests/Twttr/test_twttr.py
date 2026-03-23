from twttr import shorten


def test_education():
    assert shorten("education") == "dctn"


def test_euphoria():
    assert shorten("euphoria") == "phr"


def test_FaCeTiously():
    assert shorten("FaCeTiously") == "FCTsly"


def test_Twitter():
    assert shorten("Twitter") == "Twttr"


def test_tWiTTer():
    assert shorten("tWiTTer") == "tWTTr"


def test_TWiTTeR():
    assert shorten("TWiTTeR") == "TWTTR"


if __name__ == "__main__":
    main()
