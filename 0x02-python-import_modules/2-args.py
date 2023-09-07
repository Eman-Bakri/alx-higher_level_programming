#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argcount = len(sys.argv) - 1
    if argcount == 0:
        print("0 arguments.")
    elif argcount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argcount))
    for el in range(argcount):
        print("{}: {}".format(el + 1, sys.argv[el + 1]))
