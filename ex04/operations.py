#!/usr/bin/python3

import sys


if (len(sys.argv) != 3):
    print('err')
    exit(1)

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

if not str(arg1).isnumeric() or not str(arg2).isnumeric():
    print('err')
    exit(1)

def compute_sum(arg1, arg2):
    print(f'Sum: {arg1 + arg2}')

def compute_diff(arg1, arg2):
    print(f'Diff: {arg1 - arg2}')

def compute_product(arg1, arg2):
    print(f'Product: {arg1 * arg2}')

def compute_quotien(arg1, arg2):
    if arg2 == 0:
        print('Cannot compute quotien by 0')
        return
    print(f'Quotien: {arg1 / arg2}')

def compute_remainder(arg1, arg2):
    if arg2 == 0:
        print('Cannot compute remainder by 0')
        return
    print(f'Remainder: {arg1 % arg2}')

compute_sum(arg1, arg2)
compute_diff(arg1, arg2)
compute_product(arg1, arg2)
compute_quotien(arg1, arg2)
compute_remainder(arg1, arg2)