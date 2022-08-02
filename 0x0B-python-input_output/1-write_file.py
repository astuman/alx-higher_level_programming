#!/usr/bin/python3
#1-write_file.py
"""Defining a function that writes a text to utf-8 and returns characters"""


def write_file(filename="", text=""):
    """writing a string to a text file and returns number of characters"""
    with open(filename, "r",encoding "utf-8") as f:
        text = f.read()
