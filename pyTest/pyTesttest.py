from main import calc


def testSucess():
    assert calc("+", 1, 1) == 2


def testSucess2():
    assert calc("-", 1, 1) == 0


def testError():
    assert calc("", 1, 1) == "Error"


def testError2():
    assert calc("-", 1, 2) == "Value Invalid"
