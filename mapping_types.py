#!/usr/bin/env python
import re

AIRPORTS = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

FOOD = ['spam', 'spam', 'spam', 'toast', 'toast',
'eggs', 'spam', 'spam', 'spam', 'spam', 'spam']


def main():
    dict_examples()
    set_examples()

def dict_examples():
    re.search("", "")
    print(AIRPORTS['EWR'])
    print(sorted(AIRPORTS))
    print(AIRPORTS.keys())
    # try:
    #     print(airports['ORF'])
    # except KeyError as err:
    #     print('NOT FOUND')
    print(AIRPORTS.get('ORF', 'NOT FOUND'))
    print(AIRPORTS.setdefault('ORF', 'Norfolk'))
    print(AIRPORTS)

def set_examples():
    """
    Some examples of sets

    :return: None
    """
    global FOOD
    FOOD = set(FOOD)
    print(FOOD)
    for i in range(1000000):
        FOOD.add('spam')
    print(FOOD)


def spam(a: int, b: str, c: float) -> list:
    """
    Does something nice

    :param a: number of things
    :param b: name of things
    :param c: percentage of things
    :return: nothing
    """

if __name__ == '__main__':
    main()
