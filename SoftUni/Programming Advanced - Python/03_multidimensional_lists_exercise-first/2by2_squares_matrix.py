
def read_matrix():
    rows, columns = [int(x) for x in input().split()]
    current_matrix = []

    for i in range(rows):
        current_matrix.append([x for x in input().split()])

    return current_matrix


matrix = read_matrix()
sub_matrix_count = 2

matrices_found = 0

for row_index in range(len(matrix) - sub_matrix_count + 1):
    for col_index in range(len(matrix[row_index]) - sub_matrix_count + 1):
        current_matrix_found = []
        for row in range(row_index, row_index + sub_matrix_count):
            for col in range(col_index, col_index + sub_matrix_count):
                current_matrix_found.append(matrix[row][col])
        if len(set(current_matrix_found)) == 1:
            matrices_found += 1

print(matrices_found)
