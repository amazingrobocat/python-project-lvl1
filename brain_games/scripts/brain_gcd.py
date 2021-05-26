#!/usr/bin/env python3

"""Brain-gcd script."""
from brain_games.game_engine import game_progression
from brain_games.games import gcd


def main():
    """Start brain-gcd game."""
    game_progression(gcd)


if __name__ == '__main__':
    main()
