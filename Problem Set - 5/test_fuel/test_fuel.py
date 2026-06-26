import pytest
import fuel
from fuel import convert, gauge

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("three/four")  # Not integers
    with pytest.raises(ValueError):
        convert("5/4")          # Numerator > Denominator
    with pytest.raises(ValueError):
        convert("-1/4")         # Negative fractions
        
def test_correct_convert():
    # Test that standard fractions convert to the right integers
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("0/4") == 0

def test_correct_gauge():
    # Test the boundary values for E, F, and percentages
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_zero_division():
    # Test that dividing by zero raises a ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
