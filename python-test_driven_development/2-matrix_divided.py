#!/usr/bin/python3
""" matrix divided module """


def matrix_divided(matrix, div):
    """ function that return a new matrix with divided values """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    length = len(matrix[0])
    for idx, row in enumerate(matrix):
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for item in row:
            if type(item) != int and type(item) != float:
                raise TypeError("matrix must be a matrix (list of lists)"
                " of integers/floats")
            new_matrix[idx].append(round(item / div, 2))
    return new_matrix
