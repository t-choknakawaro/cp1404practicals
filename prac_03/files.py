
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file_name = open('name.txt', 'r')
name = in_file_name.readline()
print('Your name is', name)
in_file_name.close()

print('-' * 20)

# Write code that opens "numbers.txt", reads only the first two numbers and adds
# them together then prints the result, which should be... 59.
in_file_numbers = open('numbers.txt', 'r')
line_1 = int(in_file_numbers.readline())
line_2 = int(in_file_numbers.readline())
print(line_1 + line_2)
in_file_numbers.close()

print('-' * 20)

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a
# file with any number of numbers.
in_file_sum = open('numbers.txt', 'r')
total = 0
for line in in_file_sum:
    number = int(line)
    total += number
print(total)
in_file_sum.close()
