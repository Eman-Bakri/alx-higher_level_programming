#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdg = abs(number) % 10
if number < 0:
    lastdg = -lastdg
print("Last digit of {} is {} and is ".format(number, lastdg), end="")
if lastdg > 5:
    print("greater than 5")
elif lastdg == 0:
    print("0")
else:
    print("less than 6 and not 0")
