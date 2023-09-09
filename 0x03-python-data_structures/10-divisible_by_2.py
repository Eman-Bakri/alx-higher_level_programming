#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean = my_list[:]
    for counter, i in enumerate(my_list):
        if i % 2 == 0:
            boolean[counter] = True
        else:
            boolean[counter] = False
    return boolean
