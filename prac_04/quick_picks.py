import random

NUMBERS_IN_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    quick_pick_numbers = int(input('Enter quick pick number: '))
    for i in range(quick_pick_numbers):
        quick_pick = []
        for t in range(LINES):
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
            while num in quick_pick:
                num = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(num)
        quick_pick.sort()
        print(' '.join('{:2}'.format(num) for num in quick_pick))

main()