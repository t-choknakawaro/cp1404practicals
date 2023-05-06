MENU = '(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars (this should print as many stars as the score)\n(Q)uit'
MAX_SCORE = 100
MIN_SCORE = 0
PASS_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    score = ''
    print(MENU)
    choice = input('').upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_number('Score: ', 0, 100)
        elif choice == 'P':
            if score == '':
                print('Please choose (G) to enter valid score first.')
            else:
                print_grade(score)
        elif choice == 'S':
            if score == '':
                print('Please choose (G) to enter valid score first.')
            else:
                get_stars(score)
                print()
        else:
            print('Invalid choice')
        print(MENU)
        choice = input('>>>').upper()
    print("Farewell")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print('Invalid input')
        number = float(input(prompt))
    return number


def get_grade(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return 'Invalid score'
    elif MIN_SCORE <= score < PASS_SCORE:
        return 'Bad'
    elif PASS_SCORE <= score < EXCELLENT_SCORE:
        return 'Passable'
    elif EXCELLENT_SCORE <= score <= MAX_SCORE:
        return 'Excellent'


def print_grade(score):
    print('Your grade is ', get_grade(score))


def get_stars(score):
    score = int(score)
    for i in range(score):
        print('*', end='')


main()
