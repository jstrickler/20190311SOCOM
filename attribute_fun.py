#!/usr/bin/env python
class Dog():
    def __init__(self, breed, name):
        self._breed = breed
        self._name = name

    def bark(self):
        print("Woof! Woof")

    @property
    def breed(self):
        return self._breed

    @property
    def name(self):
        return self._name

d1 = Dog('Chug', 'Penny')
print(d1.name, d1.breed)

d2 = Dog('Sharpoodle', 'Andy')
print(d2.name, d2.breed)

a1 = 'name'
a2 = 'breed'

print(getattr(d1, a1))
print(getattr(d1, a2))

import re

x = getattr(re, 'search')

m = x('^foo', 'foobar')
print(m.group())


def wag(self):
    print("Wagging furiously")

setattr(Dog, 'wag', wag)

d1.wag()

print(hasattr(d1, 'wag'))

delattr(d1, 'breed')



