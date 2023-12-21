
rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

sum_result = []

for column_index in range(columns):
    sum_numbers = 0
    for row_index in range(rows):
        sum_numbers += matrix[row_index][column_index]
    sum_result.append(sum_numbers)

[print(x) for x in sum_result]
