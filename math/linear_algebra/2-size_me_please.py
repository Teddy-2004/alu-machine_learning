#!/usr/bin/env python3

def matrix_shape(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if isinstance(matrix[0][0], list):
        num_depth = len(matrix[0][0])
        return (num_rows, num_cols, num_depth)
    return (num_rows, num_cols)
