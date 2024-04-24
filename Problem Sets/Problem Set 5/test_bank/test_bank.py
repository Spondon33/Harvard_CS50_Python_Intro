from bank import value


def main():
    test_hello()
    test_includes_h()
    test_others()


def test_hello():
    assert value('Hello') == 0
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('Hello, Newman') == 0


def test_includes_h():
    assert value('Hey') == 20
    assert value('HEY') == 20
    assert value('hey') == 20
    assert value('Hi') == 20


def test_others():
    assert value("What's up?") == 100
    assert value("What's happening?") == 100
