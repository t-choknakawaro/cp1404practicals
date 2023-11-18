# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """
#
# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")

import random

MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    """Get a score and classify their score, and random a score with their result"""
    score = float(input('Enter score: '))
    print(classify_score(score))
    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(f'{random_score}, is a random score and their result will be {classify_score(random_score)}.')


def classify_score(score):
    """Classify the input score in to grade"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return 'Invalid score'
    elif score >= EXCELLENT_SCORE:
        return 'Excellent'
    elif score >= PASS_SCORE:
        return 'Passable'
    else:
        return 'Bad'


main()
