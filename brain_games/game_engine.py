"""Brain-even game engine."""

import prompt


def launch_game(game):
    """Launch game progression.

    Args:
        game: Provides access to functions which calculate
            values for the round of the game
    """
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')

    print('Hello, {name}!\n{R}'.format(name=user_name, R=game.RULES))

    for _ in range(3):
        question, correct_answer = game.launch_game_round()

        print('Question: {Q}'.format(Q=question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                "'{user_a}' is wrong answer ;(.".format(user_a=user_answer),
                " Correct answer was '{corr_a}'.\n".format(
                    corr_a=correct_answer,
                ),
            )
            print("Let's try again, {name}!".format(name=user_name))
            break
    else:
        print('Congratulations, {name}!'.format(name=user_name))
