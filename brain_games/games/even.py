"""Brain-even game module."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """Generate a game round.

    Generate random number that may or may not be even.
    Ask the user a question for a round of the game.
    Calculate the correct answer.

    Returns:
        - question for the user
        - correct answer value
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{0}'.format(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
