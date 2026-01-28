#!/usr/bin/env python3
def matrix_transpose(matrix):
    transposed = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed
