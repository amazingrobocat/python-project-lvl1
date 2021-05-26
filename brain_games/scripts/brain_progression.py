#!/usr/bin/env python3

"""Brain-progression script."""
from brain_games.game_engine import game_progression
from brain_games.games import progression


def main():
    """Start brain-gcd game."""
    game_progression(progression)


if __name__ == '__main__':
    main()
