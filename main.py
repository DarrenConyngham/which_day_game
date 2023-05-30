import random
from datetime import datetime, timedelta


def get_random_date():
    """
    This function will return a random datetime between two datetime objects.
    """
    start_date = datetime.strptime('1900-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2099-12-31', '%Y-%m-%d')
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return datetime.strftime(start_date + timedelta(seconds=random_second), '%Y-%m-%d'), datetime.strftime(start_date + timedelta(seconds=random_second), '%d %B %Y')


def calculate_day_of_week(date):
    """
    This function will return the day of the week for a given date.
    """
    date = datetime.strptime(date, '%Y-%m-%d')
    return datetime.strftime(date, '%A')


def evaluate_answer(answer, correct_answer):
    """
    This function will evaluate the answer provided by the user.
    """
    if answer.lower().strip() == correct_answer.lower().strip():
        return True
    else:
        return False


def play_game():
    """
    This function will start the game.
    """
    start_game_input = input('Press x to start the game: ')
    if start_game_input.lower().strip() == 'x':
        date_to_guess, formatted_date_to_guess = get_random_date()
        correct_answer = calculate_day_of_week(date_to_guess)
        print(f"What day of the week does {formatted_date_to_guess} fall on?")
        guess = input('Enter your answer: ')
        while not evaluate_answer(guess, correct_answer):
            print('Incorrect! Try again.')
            guess = input('Enter your answer: ')
        print('Correct!')


if __name__ == '__main__':
    play_game()
