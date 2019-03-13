#!/usr/bin/env python


def process_log(*, file_name, cutoff_date):
    print(file_name, cutoff_date)


process_log(file_name='foo.log', cutoff_date='2019-01-01')

process_log(
    cutoff_date='2019-01-01',
    file_name='bar.log',
)

def wacky(foo, bar, *blah, spam, ham=42, **eggs):
    pass





