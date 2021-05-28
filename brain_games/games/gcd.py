"""Brain-Greatest common divisor game module."""
import random

FIRST_MIN_NUMBER = 1
FIRST_MAX_NUMBER = 45
SECOND_MIN_NUMBER = 1
SECOND_MAX_NUMBER = 15
RULES = 'Find the greatest common divisor of given numbers.'


def gcd(number_one, number_two):
    """Find greatest common divisor of two numbers.

    Args:
        number_one(int): first generated number
        number_two(int): second generated number

    Returns:
        GCD number
    """
    while number_two != 0:
        number_one, number_two = (
            number_two, number_one % number_two,
        )
    return number_one


def get_question_and_answer():
    """Round of the Brain-GCD game.

    Generate two random numbers.
    Ask the user a question for a round of the game.

    Returns:
        - question for the user
        - correct answer value
    """
    first_generated_number = random.randint(FIRST_MIN_NUMBER, FIRST_MAX_NUMBER)
    second_generated_number = random.randint(
        SECOND_MIN_NUMBER, SECOND_MAX_NUMBER,
    )
    question = '{0} {1}'.format(first_generated_number, second_generated_number)
    correct_answer = gcd(first_generated_number, second_generated_number)
    return question, correct_answer
