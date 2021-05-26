#!/usr/bin/env python3

"""Brain-prime script."""
from brain_games.game_engine import launch_game
from brain_games.games import prime


def main():
    """Start brain-prime game."""
    launch_game(prime)


if __name__ == '__main__':
    main()
