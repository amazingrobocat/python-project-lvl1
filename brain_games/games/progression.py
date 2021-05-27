"""Brain-progression game module."""

import random

RULES = 'What number is missing in the progression?'

NUMBER_MIN = 1
NUMBER_MAX = 15
STEP_MIN = 2
STEP_MAX = 5
LENGTH_MIN = 5
LENGTH_MAX = 10


def generate_progression_parts():
    """Generate random arithmetic parameters of progression and progression itself.

    Returns:
        - arithmetic progression
        - length parameter of progression
    """
    first_element = random.randint(NUMBER_MIN, NUMBER_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    last_element = first_element + ((length - 1) * step)
    progression = list(range(first_element, last_element + 1, step))
    return progression, length


def launch_game_round():
    """Generate arithmetic progression with random hidden element.

    Returns:
        - question for the user(str)
        - correct answer value(int)
    """
    progression, length = generate_progression_parts()
    hidden_element = random.randint(0, (length - 1))
    correct_answer = progression[hidden_element]
    progression[hidden_element] = '..'
    progression_hidden = ' '.join([str(element) for element in progression])
    question = '{0}'.format(progression_hidden)
    return question, correct_answer
