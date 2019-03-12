#!/usr/bin/env python
import os

target1 = '.'
target2 = os.path.abspath(target1)

for curr_dir, dir_list, file_list in os.walk(target1):
    if 'git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")

