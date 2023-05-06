for i in range(1, 21, 2):
    print(i, end=' ')
print()

print('----------')

# a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

print('----------')

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print('----------')

# c
n = int(input('Number of stars: '))
for i in range(n):
    print('*', end='')
print()

print('----------')

# d
for i in range(1, n + 1):
    print('*' * i)
print()