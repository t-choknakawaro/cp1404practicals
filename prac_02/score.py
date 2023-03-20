
def main():
    score = float(input('Enter your score: '))
    print(score_status(score))

def score_status(score):
    if score < 0 or score > 100:
        return 'Invalid score'
    elif score >= 90:
        return 'Excellent'
    elif score >= 50:
        return 'Pass'
    else:
        return 'Bad'

main()
