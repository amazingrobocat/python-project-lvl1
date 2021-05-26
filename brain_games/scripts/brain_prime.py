#!/usr/bin/env python3

"""Brain-prime script."""
from brain_games.game_engine import game_progression
from brain_games.games import prime


def main():
    """Start brain-gcd game."""
    game_progression(prime)


if __name__ == '__main__':
    main()
