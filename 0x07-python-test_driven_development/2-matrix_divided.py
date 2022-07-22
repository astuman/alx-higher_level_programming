#!/usr/bin/python3
#2-matrix_devided.py
""""Defining matrix_divided"""
def matrix_divided(matrix, div):
    if matrix is float:
        matrix = int(matrix)
    if div is not int or div is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is not int or matrix is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
