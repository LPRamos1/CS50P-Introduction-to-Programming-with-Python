from jar import Jar
import pytest


def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(7)
