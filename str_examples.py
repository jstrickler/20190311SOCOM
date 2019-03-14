#!/usr/bin/env python
"""
Examples of string usage.
"""
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
)

ACTOR = "Tom Cruise"

print(ACTOR.lower())
print(ACTOR.split())
print(len(ACTOR))

# __builtins__.print(__builtins__.len(ACTOR))
logging.info("I am here")
print(dir(__builtins__))

X = "spam\n"

X = X.rstrip()

print(X == 'spam')

FRUITS = ["pomegranate", "cherry", "apricot", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape", "date"]

print(FRUITS[0:3])
print(FRUITS[4:9])
logging.error("UH OH!!!")


print(FRUITS[-1])

print(FRUITS[-5:])

print(FRUITS[-10:-5])
logging.warning("foobar")

logging.debug("debug message")



print(FRUITS[:3])
print(len(FRUITS))

print(FRUITS[len(FRUITS) - 1])


X = slice(3, 8)
print(FRUITS[X])

Y = slice(3, None)
print(FRUITS[Y])

X = b"abcdefghij"

print(X[::2])

X = ['Va Beach', 'Hampton', 'Portsmouth']

Y = ['Norfolk', 'Suffolk']

X.extend(Y)


print(X)


X.extend('spam')
X.extend(['spam'])

print(X)
