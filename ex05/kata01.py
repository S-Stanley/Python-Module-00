#!/usr/bin/python3

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for kt in kata:
    print('{} was created by {}'.format(kt, kata[kt]))