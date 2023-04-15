#!/usr/bin/python3

import sys

data = " ".join(sys.argv[1:])
size = len(data)

while size > 0:
    char = data[size - 1]
    if char.islower():
        print(char.upper(), end='')
    else:
        print(char.lower(), end='')
    size -= 1
