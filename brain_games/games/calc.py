"""Brain-calc game module."""
import operator
import random

INITIAL_FIRST_NUM = 0
LAST_FIRST_NUM = 20
INITIAL_SECOND_NUM = 1
LAST_SECOND_NUM = 10
RULES = 'What is the result of the expression?'


def launch_game_round():
    """Brain-calc game.

    Generate math expression with two random numbers and a random operator.
    Ask the user a question for a round of the game.
    Calculate the correct answer.

    Returns:
        - question for the user
        - correct answer value
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    first_num = random.randint(INITIAL_FIRST_NUM, LAST_FIRST_NUM)
    second_num = random.randint(INITIAL_SECOND_NUM, LAST_SECOND_NUM)
    expression = random.choice(list(operators.keys()))
    question = '{0} {1} {2}'.format(
        first_num, expression, second_num,
    )
    correct_answer = operators.get(expression)(first_num, second_num)

    return question, correct_answer
