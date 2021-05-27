"""Brain-progression game module."""

import random

RULES = 'What number is missing in the progression?'

MIN_NUMBER = 1
MAX_NUMBER = 15
MIN_STEP = 2
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


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
    first_element = random.randint(MIN_NUMBER, MAX_NUMBER)
    step_element = random.randint(MIN_STEP, MAX_STEP)
    length_element = random.randint(MIN_LENGTH, MAX_LENGTH)
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
