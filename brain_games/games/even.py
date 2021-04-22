"""Brain-even game module."""

import random

import prompt

start_integer = 1
stop_integer = 100
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_module():
    """Brain-even game."""
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')

    print('Hello, {name}!\n{R}'.format(name=user_name, R=rules))

    answer_count = 0
    while int(answer_count < 3):
        random_num = random.randint(start_integer, stop_integer)

        print('Question: {rand}'.format(rand=random_num))

        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if random_num % 2 == 0 else 'no'

        if user_answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print(
                "'{user_a}' is wrong answer ;(.".format(user_a=user_answer),
                " Correct answer was '{corr_a}'.\n".format(
                    corr_a=correct_answer,
                ),
            )
            print("Let's try again, {name}!".format(name=user_name))
            break
    else:
        print('Congratulations, {name}!'.format(name=user_name))
