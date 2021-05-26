#!/usr/bin/env python3

"""Brain-calc script."""
from brain_games.game_engine import launch_game
from brain_games.games import calc


def main():
    """Start brain-calc game."""
    launch_game(calc)


if __name__ == '__main__':
    main()
