from decimal import Decimal
from typing import Callable, List

from calculator.calculation import *

class Calculations:
    logs: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the logs list."""
        cls.logs.append(calculation)

    @classmethod
    def get_logs(cls) -> List[Calculation]:
        """Retrieve the entire logs of calculations."""
        return cls.logs

    @classmethod
    def clear_logs(cls):
        """Clear the log of calculations."""
        cls.logs.clear()

    @classmethod
    def get_last(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.logs:
            return cls.logs[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.logs if calc.operation.__name__ == operation_name]