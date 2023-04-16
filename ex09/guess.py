#!/usr/bin/python3

from random import randint

to_guess = randint(0, 99)

print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret number.')
print('Type \'exit\' to end the game.')
print('Good luck!')

attempts = 0

while True:
    user_input = input('Type your guess: ')
    if user_input == 'exit':
        exit(0)
    elif not user_input.isnumeric():
        print('Your guess is not numeric, please retry')
    elif int(user_input) < 0 or int(user_input) > 99:
        print('Your guess should be between 0 and 99')
    elif int(user_input) > to_guess:
        print('Your guess is too hight')
        attempts += 1
    elif int (user_input) < to_guess:
        print('Your guess is too low')
        attempts += 1
    else:
        if to_guess == 42:
            print('The answer to the ultimate question of life, the universe and everything is 42.')
        else:
            print(f'You did guess the right number in {attempts} attemps!')
        if attempts == 1:
            print('Congratulations! You got it on your first try!')
        exit(0)