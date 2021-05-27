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
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{0}'.format(random_number)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer


def is_prime(random_number):
    """Check number to see if it is prime.

    Args:
        random_number(int): generated number

    Returns:
         - False if number is not prime
         - True if number is prime
    """
    if random_number < 2:
        return False

    # Перебор от 2 до random_number//2
    for num in range(2, random_number // 2):

        # Если random_number делится на любое число
        # между 2 и random_number//2, то random_number не prime
        if (random_number % num) == 0:
            return False
    return True
