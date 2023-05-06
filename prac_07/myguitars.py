from prac_06.guitar import Guitar
import csv

guitars = []
class_guitars = []


def main():
    with open('guitars.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header row
        for row in reader:
            guitars.append(row)
    print('These are my guitars:')
    for guitar in guitars:
        class_guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    class_guitars.sort()
    for i, guitar in enumerate(class_guitars, 1):
        vintage_string = '(vintage)' if guitar.is_vintage() else ''
        print(f'Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f} {vintage_string}')


main()
