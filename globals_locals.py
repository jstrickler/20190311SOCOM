#!/usr/bin/env python

x = 5
person = 'Ferd Berfel'

def spam():
    alien = 'Mork'
    print(locals())

g = globals()
print(g)

for var_name in 'person', 'x', 'spam':
    print(g[var_name])

g['spam']()


g['city'] = 'Virginia Beach'

print(city)

g['double'] = lambda x: x * 2

print(double(4))
