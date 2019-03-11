#!/usr/bin/env python

actor = "Tom Cruise"

print(actor.lower())
print(actor.split())
print(len(actor))

__builtins__.print(__builtins__.len(actor))

print(dir(__builtins__))

x = "spam\n"

x = x.rstrip()

print(x == 'spam')

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0:3])
print(fruits[4:9])

print(fruits[-1])

print(fruits[-5:])

print(fruits[-10:-5])


print(fruits[:3])
print(len(fruits))

print(fruits[len(fruits) - 1])


x = slice(3, 8)
print(fruits[x])

y = slice(3, None)
print(fruits[y])

x = b"abcdefghij"

print(x[::2])

x = ['Va Beach', 'Hampton', 'Portsmouth']

y = ['Norfolk', 'Suffolk']

x.extend(y)


print(x)


x.extend('spam')
x.extend(['spam'])

print(x)
















