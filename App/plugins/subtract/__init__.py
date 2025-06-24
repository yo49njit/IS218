from App.commands import Command
from calculator.operations import subtract

class Subtract(Command):
    def execute(self):
        try:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            output= subtract(a,b)
            print(f"{a} - {b} = {output}")
        except ValueError:
            print("Invalid input")