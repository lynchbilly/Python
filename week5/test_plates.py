# Unit tests for plates.py

from plates import is_valid


def test_min_max_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_starts_with_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False


def test_numbers_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_special_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("PI 14") == False
