from App.commands import Command
from App.calculator.operations import multiply

class Multiply(Command):
    def execute(self):
        try:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            output= multiply(a,b)
            print(f"{a} x {b} = {output}")
        except ValueError:
            print("Invalid input")