#!/usr/bin/env python

#  if elif else

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

target = 'x'

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("Not found")


x = 5
y = 10
try:
    result = x / y
except ZeroDivisionError as err:
    print(err)
else:
    print(result)
