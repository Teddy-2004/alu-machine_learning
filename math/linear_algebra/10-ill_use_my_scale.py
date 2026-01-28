#!/usr/bin/env python3

def np_shape(matrix):
    import numpy as np
    np_matrix = np.array(matrix)
    return list(np_matrix.shape)
