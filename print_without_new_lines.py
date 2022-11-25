#  4. Print without new lines

data = [0, 1, 2, 3, 4, 5]


# common way:
for i in data:
    print(i, end=" ")


# without new lines:
print('\nWithout new lines: ')
print(*data)
