#!/usr/bin/env python3

"""Brain-even script."""
from brain_games.game_engine import game_progression
from brain_games.games import even


def main():
    """Start brain-even game."""
    game_progression(even)


if __name__ == '__main__':
    main()
