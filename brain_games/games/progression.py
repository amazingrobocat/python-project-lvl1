"""Brain-progression game module."""

import random

RULES = 'What number is missing in the progression?'

NUMBER_MIN = 1
NUMBER_MAX = 15
STEP_MIN = 2
STEP_MAX = 5
LENGTH_MIN = 5
LENGTH_MAX = 10


def generate_progression(start, last, step):
    """Generate arithmetic progression.

    Args:
        start(int): first number in arithmetic progression
        last(int): last number in arithmetic progression
        step(int): step between numbers in arithmetic progression

    Returns:
        list of arithmetic progression
    """
    return list(range(start, last, step))


def launch_game_round():
    """Round of the Brain-progression game.

    Generate random arithmetic parameters of progression.
    Generate hidden parameter in arithmetic progression.
    Generate arithmetic progression with random hidden element.
    Calculate correct answer and question for a round of the game.

    Returns:
        question for the user(str)
        correct answer value(int)
    """
    first_element = random.randint(NUMBER_MIN, NUMBER_MAX)
    step_element = random.randint(STEP_MIN, STEP_MAX)
    length_element = random.randint(LENGTH_MIN, LENGTH_MAX)
    last_element = first_element + ((length_element - 1) * step_element)
    progression = generate_progression(
        first_element, last_element + 1, step_element,
    )
    hidden_element = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_element]
    progression[hidden_element] = '..'
    progression_hidden = ' '.join([str(element) for element in progression])
    question = '{0}'.format(progression_hidden)
    return question, correct_answer
