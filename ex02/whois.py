#!/usr/bin/python3

import sys

if (
    len(sys.argv) > 2
    or
    len(sys.argv) <= 1
    or
    not sys.argv[1].isnumeric()
):
    print('err')
    exit(1)

nb = int(sys.argv[1])

if nb == 0:
    print("zero")
elif (nb % 2) == 0:
    print("even")
else:
    print("odd")