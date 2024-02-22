#!/usr/bin/env python3
"""rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix in-place 90 degrees clockwise"""
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
