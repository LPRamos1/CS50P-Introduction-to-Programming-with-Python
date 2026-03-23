from numb3rs import validate
import pytest


def test_lenght():
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.") == False
    assert validate("1.1.1.1.0") == False
    assert validate("") == False
    assert validate("1. 1. 1.    1") == False
    assert validate("1.1.1.1") == True


def test_higher_255():
    assert validate("256.1.1.1") == False
    assert validate("2.999.251.1") == False
    assert validate("2.3.256.99") == False
    assert validate("1.222.111.999") == False
    assert validate("301.401.510.850") == False


def test_valid_ip():
    assert validate("255.255.255.255") == True
    assert validate("100.10.253.1") == True
    assert validate("8.91.199.249") == True


def test_string():
    assert validate("cat") == False
    assert validate("test") == False
    assert validate("255.CAT.255.255") == False


def test_zero():
    # Not leading zeros
    assert validate("0.0.0.0") == True
    assert validate("192.168.0.1") == True

    # Leading zeros
    assert validate("192.168.01.1") == False
    assert validate("001.1.1.1") == False
    assert validate("1.1.1.000") == False

    # Negative


def test_negative():
    assert validate("-1.2.3.4") == False
