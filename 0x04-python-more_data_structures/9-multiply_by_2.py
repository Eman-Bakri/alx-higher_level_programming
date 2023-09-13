#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dct = a_dictionary.copy()
    keys = list(new_dct.keys())

    for i in keys:
        new_dct[i] *= 2

    return (new_dct)
