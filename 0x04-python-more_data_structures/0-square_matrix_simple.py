#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Calculate squares of each matrix element."""
    return [list(map(lambda x: x * x, row)) for row in matrix]
