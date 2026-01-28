#!/usr/bin/env python3

def add_matrices(mat1, mat2):
    """Adds two matrices element-wise.

    Args:
        mat1 (list of list of floats): The first matrix.
        mat2 (list of list of floats): The second matrix.

    Returns:
        list of list of floats: The resulting matrix after addition.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
