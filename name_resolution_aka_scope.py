#!/usr/bin/env python
import sys

# def print(*args, **kwargs):
#     sys.stdout.write("HA HA HA\n")

# x = 100

def spam():
    global x
    x = 42
    print("spam() x is:", x)

    def ham():
        # x is nonlocal scope
        print("ham() x is", x)

    return ham


f = spam()
print("main x is:", x)
f()



