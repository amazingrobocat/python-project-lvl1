"""Brain-progression game module."""

import random

RULES = 'What number is missing in the progression?'

MIN_NUMBER = 1
MAX_NUMBER = 15
MIN_STEP = 2
MAX_STEP = 5
MIN_LENGTH = 6
MAX_LENGTH = 11


def generate_progression(start, length, step):
    """Generate arithmetic progression.

    Args:
        start(int): first number in arithmetic progression
        length(int): last number in arithmetic progression
        step(int): step between numbers in arithmetic progression

    Returns:
        list of arithmetic progression
    """
    stop = start + ((length - 1) * step)
    return list(range(start, stop, step))


def get_question_and_answer():
    """Round of the Brain-progression game.

    Generate random arithmetic parameters of progression.
    Generate hidden parameter in arithmetic progression.
    Generate arithmetic progression with random hidden element.
    Calculate correct answer and question for a round of the game.

    Returns:
        - question for the user(str)
        - correct answer value(int)
    """
    first_element = random.randint(MIN_NUMBER, MAX_NUMBER)
    step_element = random.randint(MIN_STEP, MAX_STEP)
    length_element = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = generate_progression(
        first_element, length_element, step_element,
    )
    hidden_element_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    progression_hidden = ' '.join([str(element) for element in progression])
    question = str(progression_hidden)
    return question, correct_answer
