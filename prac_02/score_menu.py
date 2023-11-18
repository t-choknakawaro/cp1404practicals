MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    """Display menu and getting choice from user."""
    score = ''
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(print_result(score))
        elif choice == 'S':
            print(show_star(score))
        else:
            print('Invalid choice')
        print(MENU)
        choice = input('>>> ').upper()
    print('Farewell')


def get_valid_score():
    """Ask user for their score."""
    score = int(input('Score: '))
    while score == '':
        print('Invalid score')
        score = int(input('Score: '))
    return score


def print_result(score):
    """Print result of the score as a grade"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return 'Invalid score'
    elif score >= EXCELLENT_SCORE:
        return 'Excellent'
    elif score >= PASS_SCORE:
        return 'Passable'
    else:
        return 'Bad'


def show_star(score):
    """Print stars as the score"""
    return '*' * score


main()
