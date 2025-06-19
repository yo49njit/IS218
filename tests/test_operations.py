import pytest
from decimal import Decimal
from calculator.calculation import *
from calculator.operations import *


def test_operation(a, b, operation, expected):
    '''Function for testing for all operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.perform() == expected, "operation failed"

def test_divide_by_zero():
    '''Function for testing divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('1'), Decimal('0'), divide)
        calculation.perform()