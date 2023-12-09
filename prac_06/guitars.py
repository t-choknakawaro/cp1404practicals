from prac_06.guitar import Guitar


def main():
    """Store Guitar info inputs and display them in a list."""
    guitars = []
    print('My guitars!')
    name = input('Name: ')
    while name != '':
        year = input('Year: ')
        cost = input('Cost: $')
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, 'added.')
        name = input('Name: ')

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print('These are my guitars:')
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ''
            if guitar.is_vintage():
                vintage_string = ' (vintage)'
            print('Guitar {0}: {1.name:>20} ({1.year}), worth ${2:,.2f}{3}'.format(i, guitar, guitar.cost,
                                                                                   vintage_string))
    else:
        print('No guitars :( Quick, go and buy one!')


main()
