import pytest
from stuff.calculator import Calculator


@pytest.fixture()                   # Decorator of pytest fixture
def calc():                         # Function of pytest fixture
    return Calculator(5, 2)         # Return instance of class Calculator


def test_addition(calc):            # use calc function as parameter
    sum = calc.addition()
    assert sum == 7


def test_subtraction(calc):
    sub = calc.subtract()
    assert sub == 3


def test_multiplication(calc):
    mul = calc.multiply()
    assert mul == 10


def test_division(calc):
    div = calc.division()
    assert div == 2.5
