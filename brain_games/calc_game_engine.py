"""Brain-calc game engine."""
import prompt
from brain_games.games import calc


def game_progression():
    """Game engine function."""
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')

    print('Hello, {name}!\n{R}'.format(name=user_name, R=calc.RULES))

    game_score = 0
    while int(game_score < 3):
        question, correct_answer = calc.brain_calc_module()

        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
            game_score += 1
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
