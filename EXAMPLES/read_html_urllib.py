#!/usr/bin/env python

import urllib.request

u = urllib.request.urlopen("https://www.python.org")

print(u.info())  # <1>
print()

content = u.read()

# print(u.read(5000).decode())   # <2>

print(content.decode())


