"""Brain-even game module."""

import random

import prompt

start_integer = 1
stop_integer = 100
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_module():
    """Brain-even game."""
    random_num = random.randint(start_integer, stop_integer)

    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')

    print('Hello, {0}!\n{1}'.format(user_name, rules))

    answer_count = 0
    while int(answer_count < 3):
        random_num = random.randint(start_integer, stop_integer)

        print('Question: {0}'.format(random_num))

        user_answer = prompt.string('Your answer: ')

        right_answer = 'yes' if random_num % 2 == 0 else 'no'

        if user_answer == right_answer:
            print('Correct!')
            answer_count += 1
        else:
            print("'{UA}' is wrong answer ;(. Correct answer was '{RA}'.".format(UA=user_answer, RA=right_answer))
            print("Let's try again, {UN}!".format(UN=user_name))
            break
    else:
        print('Congratulations, {UN}!'.format(UN=user_name))
