matrix_count = int(input())

matrix = []

for i in range(matrix_count):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][len(matrix) - row - 1])

diagonals_diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonals_diff)
