#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    totaladd = 0
    for el in range(len(sys.argv) - 1):
        totaladd += int(sys.argv[el + 1])
    print("{}".format(totaladd))
