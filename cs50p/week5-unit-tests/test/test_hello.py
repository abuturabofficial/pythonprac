from hello import hello


def test_defaults():
    assert hello() == "hello, World"


def test_argument():
    assert hello("David") == "hello, David"
