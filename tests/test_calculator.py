''' 
    Tests for calculator functions 
'''

from calculator import add, subtract

def test_add():
    ''' Test if the addition function works '''
    assert add(5, 3) == 8

def test_subtract():
    ''' Test if the subtraction function works '''
    assert subtract(5, 3) == 2
