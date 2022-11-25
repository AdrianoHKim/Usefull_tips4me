#  2. list comprehension

#  One way to do:
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i*i)

print(squares)

#  Another one in ONE line:

squares = [i*i for i in range(10) if i % 2 == 0]
print(squares)
