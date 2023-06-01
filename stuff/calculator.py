# Write a Python module that contains a test suite for a simple calculator program.
# The program should have four basic arithmetic operations: addition, subtraction, multiplication, and division.
# You need to write test cases using pytest and utilize the @pytest.fixture decorator to set up and tear down any
# necessary resources for the tests.


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return int(self.a + self.b)

    def subtract(self):
        return int(self.a - self.b)

    def multiply(self):
        return int(self.a * self.b)

    def division(self):
        return float(self.a / self.b)
