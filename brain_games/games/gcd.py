"""Brain-Greatest common divisor game module."""
import random

INITIAL_FIRST_NUM = 1
LAST_FIRST_NUM = 50
INITIAL_SECOND_NUM = 1
LAST_SECOND_NUM = 20
RULES = 'Find the greatest common divisor of given numbers.'


def generate_random_numbers():
    """Generate two random numbers.

    Returns:
        two generated numbers.
    """
    first_number = random.randint(INITIAL_FIRST_NUM, LAST_FIRST_NUM)
    second_number = random.randint(INITIAL_SECOND_NUM, LAST_SECOND_NUM)
    return first_number, second_number


def gcd(first_number, second_number):
    """Find greatest common divisor of two numbers.

    Args:
        first_number(int): first generated number.
        second_number(int): second generated number.

    Returns:
        GCD number.
    """
    while second_number != 0:
        first_number, second_number = (
            second_number, first_number % second_number,
        )
    return first_number


def launch_game_round():
    """Ask the user a question for a round of the game.

    Returns:
        - question for the user
        - correct answer value
    """
    first_number, second_number = generate_random_numbers()
    question = '{0} {1}'.format(first_number, second_number)
    correct_answer = gcd(first_number, second_number)
    return question, correct_answer
