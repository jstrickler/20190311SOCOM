#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip()


t = trimmed("DATA/mary.txt")

for line in t:
    print(line)


def wacky():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'

w = wacky()

print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
# print(next(w))

w = wacky()
for thing in w:
    print(thing)

