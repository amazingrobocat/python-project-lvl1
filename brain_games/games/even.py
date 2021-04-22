"""Brain-even game module."""

import random

import prompt

start_integer = 1
stop_integer = 100
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_module():
    """Brain-even game."""
<<<<<<< HEAD
=======
    random_num = random.randint(start_integer, stop_integer)

>>>>>>> d1030c156dec2811e580d205d0c11730cf21438e
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')

<<<<<<< HEAD
    print('Hello, {name}!\n{R}'.format(name=user_name, R=rules))
=======
    print('Hello, {UN}!\n{R}'.format(UN=user_name, R=rules))
>>>>>>> d1030c156dec2811e580d205d0c11730cf21438e

    answer_count = 0
    while int(answer_count < 3):
        random_num = random.randint(start_integer, stop_integer)

<<<<<<< HEAD
        print('Question: {rand}'.format(rand=random_num))

        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if random_num % 2 == 0 else 'no'

        if user_answer == correct_answer:
=======
        print('Question: {RN}'.format(RN=random_num))

        user_answer = prompt.string('Your answer: ')

        right_answer = 'yes' if random_num % 2 == 0 else 'no'

        if user_answer == right_answer:
>>>>>>> d1030c156dec2811e580d205d0c11730cf21438e
            print('Correct!')
            answer_count += 1
        else:
            print(
<<<<<<< HEAD
                "'{user_a}' is wrong answer ;(.".format(user_a=user_answer),
                " Correct answer was '{corr_a}'.\n".format(
                    corr_a=correct_answer,
                ),
            )
            print("Let's try again, {name}!".format(name=user_name))
            break
    else:
        print('Congratulations, {name}!'.format(name=user_name))
=======
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.\n".format(
                    user_answer, right_answer,
                ),
            )
            print("Let's try again, {0}!".format(user_name))
            break
    else:
        print('Congratulations, {UN}!'.format(UN=user_name))
>>>>>>> d1030c156dec2811e580d205d0c11730cf21438e
