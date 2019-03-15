#!/usr/bin/env python
import fileinput
import argparse

arg_parser = argparse.ArgumentParser(
    description="Fake version of Unix grep"
)

arg_parser.add_argument(
    '-i', action='store_true', help='Ignore case',
    dest='ignore_case'
)

arg_parser.add_argument(
    'pattern', help="pattern to match"
)

arg_parser.add_argument(
    'files', help="files to search (STDIN if empty)",
    nargs='*'
)


arg_info, other = arg_parser.parse_known_intermixed_args()

print("namespace:", arg_info)
print("other:", other)

if arg_info.ignore_case:
    arg_info.pattern = arg_info.pattern.lower()

for line in fileinput.input(arg_info.files):
    line = line.rstrip()
    line_copy = line
    if arg_info.ignore_case:
        line_copy = line.lower()
    if arg_info.pattern in line_copy:
        print(fileinput.filename(), end=' ')
        print(line)
