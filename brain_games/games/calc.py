"""Brain-calc game module."""
import operator
import random

FIRST_MIN_NUMBER = 0
FIRST_MAX_NUMBER = 20
SECOND_MIN_NUMBER = 1
SECOND_MAX_NUMBER = 10
RULES = 'What is the result of the expression?'


def launch_game_round():
    """Brain-calc game.

    Generate math expression with two random numbers and a random operator.
    Ask the user a question for a round of the game.
    Calculate the correct answer.

    Returns:
        question for the user
        correct answer value
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    first_num = random.randint(FIRST_MIN_NUMBER, FIRST_MAX_NUMBER)
    second_num = random.randint(SECOND_MIN_NUMBER, SECOND_MAX_NUMBER)
    random_operator = random.choice(list(operators.keys()))
    question = '{0} {1} {2}'.format(
        first_num, random_operator, second_num,
    )
    correct_answer = operators.get(random_operator)(first_num, second_num)

    return question, correct_answer
