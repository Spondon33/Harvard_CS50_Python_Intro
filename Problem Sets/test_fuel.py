from plates import is_valid


def main():
    test_strt_two_letters()
    test_max_chars()
    test_numbers()
    test_punctuation()


def test_strt_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False


def test_max_chars():
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False


def test_numbers():
    assert is_valid("SPNE2") == True
    assert is_valid("SP2NE") == False
    assert is_valid("3SPNE") == False
    assert is_valid("SN02") == False
    assert is_valid("SN20") == True


def test_punctuation():
    assert is_valid("SP.NE2") == False
    assert is_valid("SP NE2") == False
    assert is_valid("SP?NE2") == False
    assert is_valid("SP!NE2") == False
