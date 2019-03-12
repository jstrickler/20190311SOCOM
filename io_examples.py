#!/usr/bin/env python
import sys

stuff = ['spam', 22, 'eggs', 8.97]

person = "Tom Cruise"

print(stuff)
print(person)
print(repr(stuff))
print(repr(person))

a = 'spam'
b = 22
c = 'eggs'
d = 8.97

print(a, b, c, d)
print(a, b, c, d, sep='')
print(a, b, c, d, sep=':')
print(a, b, c, d, sep=' * ')


for x in a, b, c, d:
    print(x, end=" ")
print()

print("Abort! abort!", file=sys.stderr)

name = input("What is your name? ")
print("name is:", name)

import getpass
password = getpass.getpass("Password: ")
print("password is:", password)




