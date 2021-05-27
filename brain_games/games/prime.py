"""Brain-prime game module."""

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 2
MAX_NUMBER = 200


def launch_game_round():
    """Generate random number that may or may not be prime.

    Returns:
        - question for the user
        - correct answer value
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def is_prime(any_number):
    """Check number to see if it is prime.

    Args:
        any_number(int): generated number

    Returns:
         - False if number is not prime
         - True if number is prime
    """
    if any_number < 2:
        return False
    for divider in range(2, any_number // 2):
        if (any_number % divider) == 0:
            return False
    return True
