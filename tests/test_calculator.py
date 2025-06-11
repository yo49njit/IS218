"""
Unit tests for the calculator module.
"""

from calculator import Calculation

def test_addition():
    """Test the add() function."""
    assert Calculation.add(2, 2) == 4
def test_subtraction():
    """Test the subtract() function."""
    assert Calculation.subtract(2, 2) == 0
def test_multiply():
    """Test the multiply() function."""
    assert Calculation.multiply(2, 4) == 8
def test_divide():
    """Test the divide() function."""
    assert Calculation.divide(2, 2) == 1