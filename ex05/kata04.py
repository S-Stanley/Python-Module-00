#!/usr/bin/python3

kata = (0, 4, 132.42222, 10000, 12345.67)

def format_number(nb: int):
    if len(str(nb)) > 1:
        return (nb)
    return (f'0{nb}')

def format_scientifique_notation(input_nb: int):
    nb = float(input_nb)
    return (f"{nb:.2E}".lower())

print('module_{}, ex_{} : {}, {}, {}'.format(
    format_number(kata[0]),
    format_number(kata[1]),
    round(kata[2], 2),
    format_scientifique_notation(kata[3]),
    format_scientifique_notation(kata[4]),
))