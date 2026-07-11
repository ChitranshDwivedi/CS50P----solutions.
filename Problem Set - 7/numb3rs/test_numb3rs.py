import numb3rs
from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("999.999.999.999") == False
    assert validate("000.001.010.100") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False
    assert validate("cat") == False
    assert validate("255.999.999.999") == False
