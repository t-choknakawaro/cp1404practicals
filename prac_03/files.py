def main():

    in_file = open('names.txt', 'r')
    name = in_file.readline()
    print('Your name is', name)
    in_file.close()

main()

print('------')

def main():
    in_file = open('numbers.txt', 'r')
    line_1 = int(in_file.readline())
    line_2 = int(in_file.readline())
    total = line_1 + line_2
    print(total)
    in_file.close()

main()

def main():
    in_file = open('numbers.txt', 'r')
    sum = 0
    for line in in_file:
        line = int(line)
        sum += line
    in_file.close()
    print(sum)

main()