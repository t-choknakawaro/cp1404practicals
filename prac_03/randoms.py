import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1?
# Answer: 20

# What was the smallest number you could have seen, what was the largest?
# Answer: smallest is 5, largest is 20


# What did you see on line 2?
# Answer: 9

# What was the smallest number you could have seen, what was the largest? Could line 2 have produced a 4?
# Answer: smallest is 5, largest is 9, and no line 2 cannot produce a 4


# What did you see on line 3?
# Answer: 4.76694544947256

# What was the smallest number you could have seen, what was the largest?
# Answer: smallest is 2.5, largest is 4.9

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
def main():
    print(random.randint(1, 101))


main()
