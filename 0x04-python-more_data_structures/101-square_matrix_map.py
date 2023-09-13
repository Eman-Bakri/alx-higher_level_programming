#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda el: list(map(lambda el2: el2**2, el)), matrix)))
