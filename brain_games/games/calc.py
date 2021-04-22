"""Brain-calc game module."""
import operator
import random

INITIAL_FIRST_NUM = 0
LAST_FIRST_NUM = 20
INITIAL_SECOND_NUM = 1
LAST_SECOND_NUM = 10
RULES = 'What is the result of the expression?'


def brain_calc_module():
    """Brain-calc game.

    Generate math expression with two random numbers and a random operator.
    Ask a question to the user.
    Calculate the correct answer.

    Returns:
        Return question and correct answer.
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    random_num_one = random.randint(INITIAL_FIRST_NUM, LAST_FIRST_NUM)
    random_num_two = random.randint(INITIAL_SECOND_NUM, LAST_SECOND_NUM)
    expression = random.choice(list(operators.keys()))
    question = 'Question: {0} {1} {2}'.format(
        random_num_one, expression, random_num_two,
    )
    correct_answer = operators.get(expression)(random_num_one, random_num_two)

    return question, correct_answer
