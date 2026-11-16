matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print the matrix
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# sum of all elements
total = 0
for row in matrix:
    for value in row:
        total = total + value

print("Sum =", total)
