
count_matrix = int(input())

matrix = []

for i in range(count_matrix):
    matrix.append([x for x in input()])

special_symbol = input()
is_special_found = False

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == special_symbol:
            print(f"({row}, {column})")
            is_special_found = True
            raise SystemExit

if not is_special_found:
    print(f"{special_symbol} does not occur in the matrix")
