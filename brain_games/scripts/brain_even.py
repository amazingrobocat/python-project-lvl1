#!/usr/bin/env python3

"""Brain-even script."""
from brain_games.game_engine import launch_game
from brain_games.games import even


def main():
    """Start brain-even game."""
    launch_game(even)


if __name__ == '__main__':
    main()
