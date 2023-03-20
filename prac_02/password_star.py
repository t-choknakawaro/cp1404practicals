MIN_LENGTH = 4

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(MIN_LENGTH):
    password = input(f'Enter password at least {MIN_LENGTH} characters: ')
    while len(password) < MIN_LENGTH:
        print('Password is too short')
        password = input(f'Enter password at least {MIN_LENGTH} characters: ')
    return password

def print_asterisks(pw):
    print('*' * len(pw))

main()
