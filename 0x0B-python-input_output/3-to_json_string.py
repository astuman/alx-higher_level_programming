#!/usr/bin/python3
# 3-to_json_string.py
"""Defining a function that reprsents JSON"""


import json
def to_json_string(my_obj):
    """Return the JSOn representaion of a string object"""
    return json.dumps(my_obj)
