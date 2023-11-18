"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_IF_UNDER_1000 = 0.1
BONUS_IF_OVER_1000 = 0.15


# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = sales * BONUS_IF_UNDER_1000
# else:
#     bonus = sales * BONUS_IF_OVER_1000
# print(f'Bonus is ${bonus}')

sales = float(input('Enter sales: $'))
while sales >= 0:
    if sales < 1000:
        bonus = sales * BONUS_IF_UNDER_1000
    else:
        bonus = sales * BONUS_IF_OVER_1000
    print(f'Bonus is ${bonus}')
    sales = float(input('Enter sales: $'))