#!/usr/bin/env python

x = 5

y = x

stuff = ['a', 'b', 'c']
print(stuff)
things = stuff
things.append('wombat')

print("stuff:", stuff)
print("things:", things)
print(x is y)
y = 10

print(x is y)
print(things is stuff)

print(id(x) == id(y))

a = 22
b = 22

print(id(a), id(b), a is b)

x = [1, 2, 3]
y = [1, 2, 3]
print(id(x), id(y), x == y, x is y)



# numbers
#  int float bool complex

# string-like
# str bytes

# array-like
#  list tuple

# mapping types
#  dict set frozenset



