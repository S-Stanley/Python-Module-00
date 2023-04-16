#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print('ERROR: wrong number of arguments')
    exit(1)

if not sys.argv[2].isnumeric():
    print('ERROR: 2nd argument should be integer')
    exit(1)

words = sys.argv[1].split(' ')
nb = int(sys.argv[2])

def count_ponctuation(word: str):
    count = 0
    for ch in word:
        if (
            ch == '.'
            or
            ch == '!'
            or
            ch == '?'
        ):
            count += 1
    return (count)

for word in words:
    if (len(word) - nb - count_ponctuation(word)) > 0:
        print(word)
