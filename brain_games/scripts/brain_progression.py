#!/usr/bin/env python3

"""Brain-progression script."""
from brain_games.game_engine import launch_game
from brain_games.games import progression


def main():
    """Start brain-progression game."""
    launch_game(progression)


if __name__ == '__main__':
    main()
