"""CLI module."""
import prompt


def greet():
    """Greet function."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """Welcome user function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
