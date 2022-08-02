#!/usr/bin/python3
#1-write_file.py
"""Defining a function that writes a text to utf-8 and returns characters"""


def write_file(filename="", text=""):
    """writing a string to a text file and returns number of characters
    Args:
       filename (str): the name of text to be write
       text (str): the text to write to the file
       Returns :
           the number of charachters written"""
    
    with open(filename, "w",encoding "utf-8") as f:
        return f.write(text)
