"""
Calculator module containing basic arithmetic operations.
"""
class Calculation:
    """calculation class"""
    def __init__(self, a, b, operation, result):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    @staticmethod
    def add(a, b):
        """Returns the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Returns the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Returns the multiplication of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Returns the division of a and b."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @classmethod
    def create(cls, a, b, operation_func):
        result = operation_func(a, b)
        return cls(a, b, operation_func.__name__, result)

    def get_result(self):
        """Returns results."""
        return self.operation(self.a, self.b)
        
class CalculationHistory:
    history = []

    @classmethod
    def add(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()


