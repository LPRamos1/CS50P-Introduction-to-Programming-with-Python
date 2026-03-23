from fuel import convert, gauge
import pytest


def test_convert_errors():
    # Test for X > Y
    with pytest.raises(ValueError):
        convert("5/4")
    # Test for x negative
    with pytest.raises(ValueError):
        convert("-1/4")
    # Test for non-integer inputs
    with pytest.raises(ValueError):
        convert("three/four")
    # Test for Y = 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    # Test return of convert


def test_convert_success():
    assert convert("1/4") == 25
    assert convert("1/2") == 50

    # Test for gauge prints


def test_percentages():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
