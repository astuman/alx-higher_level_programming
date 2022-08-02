#!/usr/bin/python3
#1-write_file.py
"""Defining a file-writing function"""


def write_file(filename="", text=""):
    """writing a string to a UTF-8 text file
    Args:
       filename (str): the name of text to be write
       text (str): the text to write to the file
       Returns :
           the number of charachters written
           """
    
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
