#!/usr/bin/python3

def magic_calculation(a, b):
    myresult = 0
    for el in range(1, 3):
        try:
            if el > a:
                raise Exception('Too far')
            else:
                myresult += a ** b / el
        except:
            myresult = b + a
            break
    return myresult
