#!/usr/bin/env python3

def cat_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        result.append(mat1[i] + mat2[i])
    return result
