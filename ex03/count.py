#!/usr/bin/python3

import sys

def count_char(txt: str):
    print(f'The text contain {len(txt)} charactere(s)')

def count_upper(txt: str):
    count = 0
    for i in txt:
        if i.isupper():
            count += 1
    print(f'- {count} upper letter(s)')

def count_lower(txt: str):
    count = 0
    for i in txt:
        if i.islower():
            count += 1
    print(f'- {count} lower letter(s)')

def count_ponctuation(txt: str):
    count = 0
    for i in txt:
        if (
            i == '?'
            or
            i == '!'
            or
            i == '.'
        ):
            count += 1
    print(f'- {count} ponctuation mark(s)')

def count_space(txt: str):
    count = 0
    for i in txt:
        if i.isspace():
            count += 1
    print(f'- {count} spaces(s)')

def get_string(user_input: str):
    if not user_input:
        txt = input('Please, provide a string\n')
    elif user_input is None:
        txt = input('Please, provide a string\n')
    else:
        txt = user_input
    return (txt)

def text_analyzer(user_input: str = ""):
    txt = get_string(user_input)
    count_char(txt)
    count_upper(txt)
    count_lower(txt)
    count_ponctuation(txt)
    count_space(txt)

if __name__ == '__main__':
    text_analyzer(" ".join(sys.argv[1:]))