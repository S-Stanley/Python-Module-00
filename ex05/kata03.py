#!/usr/bin/python3

kata = "The right format"

nb = 42 - len(kata)

while nb > 0:
    print('-', end='')
    nb -= 1

print(kata, end='')