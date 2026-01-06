# Unit tests for fuel.py

import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_empty():
    assert convert("0/100") == 0
    assert convert("99/100") == 99


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
