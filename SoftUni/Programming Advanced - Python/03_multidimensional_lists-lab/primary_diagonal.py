
count_matrix = int(input())

matrix = []

for i in range(count_matrix):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = []

for row_index in range(count_matrix):
    diagonal_sum.append(matrix[row_index][row_index])

print(sum(diagonal_sum))
