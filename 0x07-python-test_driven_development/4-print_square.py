#!/usr/bin/python3
#4-print_square.py
"""Defines a square-printing function"""
def print_square(size):
    """print a square with a '#' character
    Args: 
    size(int): The height or width of the the square
    Raise:
    TypeError: if size data tayp is not int
    ValueError: if size is less than 0 and float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("value must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
