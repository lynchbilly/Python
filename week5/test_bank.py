# Unit tests for bank.py

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_hello_name():
    assert value("hello, Newman") == 0


def test_h_words():
    assert value("How you doing?") == 20
    assert value("hi") == 20


def test_other():
    assert value("What's happening?") == 100
    assert value("Good morning") == 100
