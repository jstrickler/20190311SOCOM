#!/usr/bin/env python

import sys
from subprocess import check_call, run, check_output, CalledProcessError, PIPE
from glob import glob
import shlex

if sys.platform == 'win32':
    CMD = 'cmd /c dir'
    FILES = r'..\DATA\t*'
else:
    CMD = 'ls -ld'
    FILES = '../DATA/t*'

cmd_words = shlex.split(CMD)
cmd_files = glob(FILES)

full_cmd = cmd_words + cmd_files

# try:
#     check_call(full_cmd)
# except CalledProcessError as err:
#     print("Command failed with return code", err.returncode)
#
# print('-' * 60)
#
# try:
#     output = check_output(full_cmd)
#     print("Output:", output.decode(), sep='\n')
# except CalledProcessError as e:
#     print("Process failed with return code", e.returncode)
#
# print('-' * 50)


try:
    proc = run(full_cmd, stdout=PIPE, stderr=PIPE)
    print(proc.returncode)
    print(proc.stdout.decode())
    print(proc.stderr.decode())
except CalledProcessError as err:
    print(err)


