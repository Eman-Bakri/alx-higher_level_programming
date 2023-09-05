#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for first in range(0, 10):
    for second in range(first + 1, 10):
        if first == 8 and second == 9:
            print("{}{}".format(first, second))
        else:
            print("{}{}".format(first, second), end=", ")
