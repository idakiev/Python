
def read_matrix():
    rows, columns = [int(x) for x in input().split()]
    current_matrix = []

    for i in range(rows):
        current_matrix.append([int(x) for x in input().split()])

    return current_matrix


matrix = read_matrix()
sub_matrix_count = 3

biggest_matrix_sum = float("-inf")
biggest_matrix = []


for row_index in range(len(matrix) - sub_matrix_count + 1):
    for col_index in range(len(matrix[row_index]) - sub_matrix_count + 1):
        current_matrix_sum = []
        for row in range(row_index, row_index + sub_matrix_count):
            for col in range(col_index, col_index + sub_matrix_count):
                current_matrix_sum.append(matrix[row][col])

        if sum(current_matrix_sum) > biggest_matrix_sum:
            biggest_matrix = current_matrix_sum
            biggest_matrix_sum = sum(current_matrix_sum)
        else:
            continue

print(f"Sum = {biggest_matrix_sum}")
print(' '.join(map(str, biggest_matrix[:3])))
print(' '.join(map(str, biggest_matrix[3:6])))
print(' '.join(map(str, biggest_matrix[6:])))
