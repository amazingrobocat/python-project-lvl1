"""Brain-calc game module."""
import operator
import random

INITIAL_FIRST_NUM = 0
LAST_FIRST_NUM = 20
INITIAL_SECOND_NUM = 1
LAST_SECOND_NUM = 10
RULES = 'What is the result of the expression?'


def generate_expression_parts():
    """Generate math expression with two random numbers and a random operator.

    Returns:
        - two generated numbers
        - math expression
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    first_num = random.randint(INITIAL_FIRST_NUM, LAST_FIRST_NUM)
    second_num = random.randint(INITIAL_SECOND_NUM, LAST_SECOND_NUM)
    expression = random.choice(list(operators.keys()))
    return first_num, second_num, expression, operators


def launch_game_round():
    """Ask the user a question for a round of the game.

    Ask a question to the user.
    Calculate the correct answer.

    Returns:
        - question for the user
        - correct answer value
    """
    first_num, second_num, expression, operators = generate_expression_parts()
    question = '{0} {1} {2}'.format(
        first_num, expression, second_num,
    )
    correct_answer = operators.get(expression)(first_num, second_num)

    return question, correct_answer
