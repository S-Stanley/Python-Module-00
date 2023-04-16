#!/usr/bin/python3

from sys import argv

converter = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

}

if len(argv) == 1:
    exit(0)

string_to_convert = " ".join(argv[1:])

for char in string_to_convert:
    if not char.isalnum() and not char.isspace():
        print('ERROR: cannot support non alpha/num/space charactres')
        exit(1)

for x in string_to_convert:
    if x == ' ':
        print('/', end=' ')
    else:
        print(converter[x.lower()], end=' ')
print('')

