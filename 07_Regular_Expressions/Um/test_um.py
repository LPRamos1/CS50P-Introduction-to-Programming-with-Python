import pytest
from um import count


def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("um...") == 1


def test_case_insensitivity():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_substrings():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("hum") == 0
    assert count("column") == 0


def test_multiple_um():
    assert count("um, thanks, um...") == 2
    assert count("um, hello, um, world, um") == 3
    assert count("Um? Mum? Is this um... yummy?") == 2


def test_sentence_with_other_words():
    assert count("Test with no u-m.") == 0
    assert count("The word is um.") == 1
