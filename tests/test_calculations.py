'''My Calculator Test'''
from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import *

from calculator.operations import *

@pytest.fixture
def setup_calculations():
    """Clear logs and add sample calculations for testing."""
    Calculations.clear_logs()

    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('4'), multiply))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    sample_calc = Calculation(Decimal('4'), Decimal('3'), add)

    Calculations.add_calculation(sample_calc)

    assert Calculations.get_last() == sample_calc, "Failed to add the calculation to the logs"

def test_get_logs(setup_calculations):
    """Test retrieving the entire calculation logs."""
    log = Calculations.get_logs()
    assert len(log) == 3, "Logs does not contain the expected number of calculations"

def test_clear_logs(setup_calculations):
    """Test clearing the entire calculation logs."""
    Calculations.clear_logs()
    assert len(Calculations.get_logs()) == 0, "Logs was not cleared"

def test_get_last(setup_calculations):
    """Test getting the latest calculation from the logs."""
    latest = Calculations.get_last()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in logs by type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"
    multiply_operations = Calculations.find_by_operation("multiply")
    assert len(multiply_operations) == 1, "Did not find the correct number of calculations with multiply operation"

