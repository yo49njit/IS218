# tests/test_add_command.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.plugins.add import Add
from App.plugins.subtract import Subtract
from App.plugins.multiply import Multiply
from App.plugins.divide import Divide
import builtins

def test_add_command(monkeypatch, capsys):
    inputs = iter(['2', '3'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    add_command = Add()
    add_command.execute()
    
    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out

def test_subtract_command(monkeypatch, capsys):
    inputs = iter(['5', '3'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    subtract_command = Subtract()
    subtract_command.execute()
    
    captured = capsys.readouterr()
    assert "5.0 - 3.0 = 2.0" in captured.out

def test_multiply_command(monkeypatch, capsys):
    inputs = iter(['6', '6'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    multiply_command = Multiply()
    multiply_command.execute()
    
    captured = capsys.readouterr()
    assert "6.0 x 6.0 = 36.0" in captured.out

def test_divide_command(monkeypatch, capsys):
    inputs = iter(['10', '2'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    divide_command = Divide()
    divide_command.execute()
    
    captured = capsys.readouterr()
    assert "10.0 / 2.0 = 5.0" in captured.out

def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(['10', '0'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    divide_command = Divide()
    divide_command.execute()

    captured = capsys.readouterr()
    assert (
    "Cannot divide by zero." in captured.out
    or "Error" in captured.out
    or "Invalid input" in captured.out
)

