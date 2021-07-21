# coding=utf-8

"""glenoidplanefitting tests"""

from glenoidplanefitting.ui.glenoidplanefitting_demo import run_demo
from glenoidplanefitting.algorithms import addition, multiplication

# Pytest style
def test_using_pytest_glenoidplanefitting():
    """First test"""
    #pylint:disable=invalid-name
    x = 1
    y = 2
    verbose = False
    multiply = False

    expected_answer = 3
    assert run_demo(x, y, multiply, verbose) == expected_answer

def test_addition():
    """ Test addition """
    assert addition.add_two_numbers(1, 2) == 3

def test_multiplication():
    """ Test multiplication """
    assert multiplication.multiply_two_numbers(2, 2) == 4
