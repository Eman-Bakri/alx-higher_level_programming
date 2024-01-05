#!/usr/bin/python3
"""
Module to find peak
"""


def find_peak(list_of_integers):
    """
    Method to calculate the hightest int in array
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
