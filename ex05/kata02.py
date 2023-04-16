#!/usr/bin/python3

kata = (2019, 9, 25, 3, 30)

def format_number(nb):
    if len(str(nb)) > 1:
        return (nb)
    return (f'0{nb}')

print('{}/{}/{} {}:{}'.format(
    format_number(kata[1]),
    format_number(kata[2]),
    format_number(kata[0]),
    format_number(kata[3]),
    format_number(kata[4])
))