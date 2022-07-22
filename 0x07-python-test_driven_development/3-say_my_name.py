#!/usr/bin/python3
#3-say_my_name.py
"""Defining a function"""

def say_my_name(first_name, last_name=""):
    """Print name
    Args: first_name (str) Printing the first name.
          last_name(str) printing last name
          Raises:
                TypeError: while first name or last name is string 
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {}{}".format(first_name, last_name))