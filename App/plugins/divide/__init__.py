from App.commands import Command
from App.calculator.operations import divide

class Divide(Command):
    def execute(self):
        try:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            output= divide(a,b)
            print(f"{a} / {b} = {output}")
        except ValueError:
            print("Invalid input")