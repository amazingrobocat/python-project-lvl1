#!/usr/bin/env python3

"""Brain-calc script."""
from brain_games.game_engine import game_progression
from brain_games.games import calc


def main():
    """Start brain-calc game."""
    game_progression(calc)


if __name__ == '__main__':
    main()
