#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(person[0], person[1])

first_name, last_name, product = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, product, birthdate in people:
    # first_name, last_name, product, birthdate = next(people)
    # person = next(people)
    # person = next(people)
    # ...
    print(first_name, last_name)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


for first_name, last_name, *_ in people:
    # first_name, last_name, product, birthdate = next(people)
    # person = next(people)
    # person = next(people)
    # ...
    print(first_name, last_name)
print('-' * 60)

def doit(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)

doit(1, 2, 3)

nums = [5, 10, 15]

doit(*nums)

def foo(*junk):
    pass

def config(**kwargs):
    print("kwargs:", kwargs)

config(file_name='spam.txt', animal='wombat')

info = {
    'file_name': 'eggs.txt',
    'animal': 'honey badger',
}

config(**info)
