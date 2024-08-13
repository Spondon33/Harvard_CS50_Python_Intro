from fuel import convert, gauge
import pytest


def main():
    test_fraction()
    test_full_empty()
    test_undefined()
    test_alpha()


def test_fraction():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("2/4") == 50 and gauge(50) == "50%"
    assert convert("3/4") == 75 and gauge(75) == "75%"

def test_full_empty():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_undefined():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_alpha():
    with pytest.raises(ValueError):
        convert("a/b")


if __name__ == "__main__":
    main()
