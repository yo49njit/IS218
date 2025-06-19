from calculator.calculation import *
from decimal import Decimal 
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    def perform(self) -> Decimal:
        """Performs the inputted calculation and returns the result."""
        return self.operation(self.a, self.b)
