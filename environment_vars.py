#!/usr/bin/env python
import os

print(os.getenv('USER'))

print(os.getenv('ANIMAL', 'wombat'))


posix_cmd = "ls $USER/stuff"

print(os.path.expandvars(posix_cmd))
