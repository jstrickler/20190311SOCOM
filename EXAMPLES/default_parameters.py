#!/usr/bin/env python

def spam(greeting, whom='world'):  # <1>
    print("{}, {}".format(greeting, whom))


spam("Hello")  # <2>
spam("Hello", "Mom")  # <3>
print()

def ham(*, file_name, file_format='txt'):  # <4>
    print("Processing {} as {}".format(file_name, file_format))

ham(file_name='eggs')  # <5>
ham(file_name='toast', file_format='csv')
