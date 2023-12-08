def main():
    with open('wimbledon.csv', 'r') as file:
        next(file)
        data = [line.strip().split(',') for line in file]

    champions = {}
    countries = set()
    for row in data:
        champions[row[2]] = champions.get(row[2], 0) + 1
        countries.add(row[1])

    print('Wimbledon Champions:')
    for name, count in champions.items():
        print(f'{name} {count}')

    print('\nThese', len(countries), 'countries have won Wimbledon:')
    print(', '.join(sorted(countries)))


if __name__ == '__main__':
    main()
