import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# what did you see on line 1
# 10
# what was the smallest number you could have seen, what was the largest
# smallest: 5 and largest: 19

# what did you see on line 2
# 5
# what was the smallest number you could have seen, what was the largest
# smallest: 3 and largest: 9

# what did you see on line 3
# 5.002255929987108
# what was the smallest number you could have seen, what was the largest
# smallest: 2.5 and largest: 5.49

print('--------')

def main():
    print(random.randint(1, 100))

main()