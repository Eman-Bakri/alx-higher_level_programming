#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    int_bool = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        int_bool =  False
    return int_bool
