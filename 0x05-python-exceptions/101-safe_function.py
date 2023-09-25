#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception as error1:
        print("Exception: {}".format(error1), file=sys.stderr)
        return None
