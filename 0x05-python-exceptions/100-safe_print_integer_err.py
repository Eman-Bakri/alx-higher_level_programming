#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    int_bool = True
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        int_bool =  False
    return int_bool
