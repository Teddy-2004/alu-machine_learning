#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum_product = 0
            for k in range(len(mat2)):
                sum_product += mat1[i][k] * mat2[k][j]
            row.append(sum_product)
        result.append(row)
    return result
mat_mul = __import__('8-ridin_bareback').mat_mul