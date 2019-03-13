#!/usr/bin/env python
class Dog():
    def __init__(self, breed, name):
        self._breed = breed
        self._name = name

    def bark(self):
        print("Woof! Woof")

    def __add__(self, other):
        x = Dog(type(self).__name__ + type(other).__name__, "None")
        return x

    @property
    def breed(self):
        return self._breed

class Chug(Dog):
    def bark(self):
        super().bark()
        print("Erk! Erk!")


d = Chug('Chug', 'Penny')

d.bark()


class Doodle(Dog):
    pass

d2 = Doodle("Doodle", "Bob")

d3 = d + d2

print(d3.breed)

