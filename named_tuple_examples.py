#!/usr/bin/env python

from collections import namedtuple

Person = namedtuple("Person", "first_name last_name age")

p1 = Person("Bob", "Smith", 42)
p2 = Person("Mary", "Reece", 85)

for pres in p1, p2:
    print(pres.last_name)

President = namedtuple("President", "term last_name first_name birth_date death_date birth_place birth_state term_start term_end party")

presidents = []
with open('DATA/presidents.txt') as pres_in:
    for line in pres_in:
        p = President(*line.rstrip().split(':'))
        presidents.append(p)

for pres in presidents:
    print(f"{pres.first_name:20.20} {pres.last_name:15} {pres.party}")

x, y, z = 'foo', 'bar', 'blah'
spam = f"""
    first part {x}
    second part {y} 
    third part {z}
"""


print(spam.strip().replace('\n', ' '))

import re

x = re.sub('\s+', ' ', spam.strip())
print(x)



s = "abcabaaabbaabPython is awesomebbaaaabbaa"

print(s.strip('abc'))

print("H" "e" "l" "l" "o")





