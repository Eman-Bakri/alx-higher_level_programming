#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    """Excute safely"""
    try:
        value = fct(*args)
        return value
    except Exception as error1:
        print("Exception: {}".format(error1), file=sys.stderr)
        return None
