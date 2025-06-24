from App.commands import Command
from calculator.operations import add

class Add(Command):
    def execute(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add(a, b)
        print(f"{a} + {b} = {result}")
