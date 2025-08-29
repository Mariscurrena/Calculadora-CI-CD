import pytest
from io import StringIO
import sys

from main import add_numbers, rest_numbers, mult_numbers, div_numbers, main

def mock_input(mock_inputs):
    original_input = sys.stdin
    sys.stdin = StringIO('\n'.join(mock_inputs))
    return original_input

def test_addition():
    mock_input(['1', '3'])  
    result = add_numbers()
    assert result == 4 

def test_substraction():
    mock_input(['2', '10'])
    result = rest_numbers()
    assert result == -8

def test_multiplication():
    mock_input(['3', '5'])
    result = mult_numbers()
    assert result == 15

def test_division():
    mock_input(['4', '8'])
    result = div_numbers()
    assert result == 0.5 

def test_division_by_zero():
    mock_input(['4', '0'])
    try:
        div_numbers()
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    pytest.main()