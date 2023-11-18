MIN_LENGTH = 3


def main():
    """Get password from user and print the output as the asterisks."""
    password = get_password()
    print_asterisk(password)


def get_password():
    """Get the password from the user with minimum characters of 3."""
    password = input(f'Enter password at least {MIN_LENGTH} characters: ')
    while len(password) < MIN_LENGTH:
        password = input(f'Enter password at least {MIN_LENGTH} characters: ')
    return password


def print_asterisk(password):
    """Print asterisks as the length of password"""
    print('*' * len(password))


main()
