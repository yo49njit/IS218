"""
Calculator module containing basic arithmetic operations.
"""
from calculator.calculations import *
from calculator.operations import *
from calculator.calculation import * 
from decimal import Decimal  
from typing import Callable 

class Calculator:
    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, divide)