"""
A parametrized test function
we don't need to write separate test cases of same type, These tests violate the DRY principle - "Don't Repeat Yourself"
@pytest.mark.parametrize
"""
# def test_multiply_two_positive_ints():
#  assert 2 * 3 == 6
#
# def test_multiply_identity():
#   assert 1 * 99 == 99
#
# def test_multiply_zero():
#   assert 0 * 100 == 0

import pytest

products = [
  (2, 3, 6),                    # positive integers
  (1, 99, 99),                  # identity
  (0, 99, 0),                   # zero
  (3, -4, -12),                 # positive by negative
  (-5, -5, 25),     	        # negative by negative
  (2.5, 6.7, 16.75)             # floats
]


@pytest.mark.parametrize('num1, num2, product', products)
def test_multiplication(num1, num2, product):
    assert num1 * num2 == product

#   -----------------------------------IMPORTANT---------------------------------------------------------------
#   We also need to pass two arguments to the decorator.
#   The first argument is a string containing a comma-separated list of variable names.
#   These names must match the parameter names for the test case function, a, b, and product.
#   The second argument is the list of parametrized values.
#   Note that the number of variable names and the length of each tuple in the list is three. These must match.
#   And just like that, we have parametrized one test case function to cover multiple sets of inputs.
#   ------------------------------------------------------------------------------------------------------------
