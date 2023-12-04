
def main():
    """get an email from the user and return it with their name."""
    email_to_name = {}
    email = input('Email: ')
    while email != '':
        name = get_name_from_email(email)
        check = input(f'Is your name {name}? (Y/n) ').upper()
        if check != 'Y' and check != '':
            name = input('Name: ')
        email_to_name[email] = name
        email = input('Email: ')

    for email, name in email_to_name.items():
        print(f'{name} ({email})')


def get_name_from_email(email):
    """split user email."""
    name = email.split('@')[0].replace('.', ' ').title()
    return name


main()
