from convert0 import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000
