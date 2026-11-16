matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []
for col in range(3):
    new_row = []
    for row in range(2):
        new_row.append(matrix[row][col])
    transpose.append(new_row)

print(transpose)
