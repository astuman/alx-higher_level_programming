#!/usr/bin/python3
# 2-append_write.py
"""Defining a function that appends a string"""
def append_write(filename="", text=""):
    """Writing a string to a file
    Args:
       filename (str):
             a string to writing on
       text (str):
             a string tfo write on the filename
       Return:
             returns the appended
             """
    with open(filename, "a", unicoding="utf-8") as f:
        return f.write(text)
