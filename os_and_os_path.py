#!/usr/bin/env python
import os
import sys
from datetime import datetime

print(os.getcwd())
print(os.getuid())
print(os.getpid())
os.makedirs('spam/ham/eggs/toast', exist_ok=True)
os.makedirs('barf', exist_ok=True)
os.makedirs('blech', 755, exist_ok=True)
try:
    os.remove('pastable2.py')
except:
    print("already gone")
print(os.listdir('DATA'))

for entry in os.scandir('DATA'):
    print(entry.name, entry.is_file())
    print(entry.stat())
    print('-' * 60)

print('=' * 60)

flags = [True] * 10
print(flags)

# os.path
FOLDER = 'DATA'
FILE = 'mary.txt'

# file_path = FOLDER + os.sep + FILE
file_path = os.path.join(FOLDER, FILE)

print(file_path)

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

file_size = os.path.getsize(file_path)
print("file size:", file_size)

s = os.stat(file_path)
print(s)

raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

for f in "mary.txt", "alice.txt", "mimi.txt":
    file_path = os.path.join('DATA', f)
    print(f, os.path.exists(file_path))



