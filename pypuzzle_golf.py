#!/usr/bin/env python
import struct

print(''.join(chr(int(b)) for b in struct.unpack("fififhHfIdfdIiIh", open('DATA/puzzle.data', 'rb').read())))

