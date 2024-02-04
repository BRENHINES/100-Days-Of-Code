import Calculator_Function as cf


def test_addition():
    assert cf.addition(1, 2) == 3


def test_substraction():
    assert cf.substraction(2, 1) == 1


def test_divide():
    assert cf.divide(1, 2) == 0.5


def test_multiply():
    assert cf.multiply(1, 1) == 1


def test_integer_divide():
    assert cf.integer_divide(3, 2) == 1


def test_power():
    assert cf.power(2, 3) == 8
