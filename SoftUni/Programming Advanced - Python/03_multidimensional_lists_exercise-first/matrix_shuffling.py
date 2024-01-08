
def read_matrix():
    rows, columns = [int(x) for x in input().split()]
    current_matrix = []

    for i in range(rows):
        current_matrix.append([x for x in input().split()])

    return current_matrix


matrix = read_matrix()

command = input().split()
while command[0] != "END":
    if command[0] == "swap":
        if len(command) != 5:
            print(f"Invalid input!")
        else:
            first_row = command[1]
            first_col = command[2]
            second_row = command[3]
            second_col = command[4]
            if int(first_row) < 0 or int(first_col) < 0 or int(second_row) < 0 or int(second_col) < 0:
                print(f"Invalid input!")
            elif int(first_row) > len(matrix) - 1 or int(second_row) > len(matrix) - 1\
                    or int(first_col) > len(matrix[0]) - 1 or int(second_col) > len(matrix[0]) - 1:
                print(f"Invalid input!")
            else:
                first_element = matrix[int(first_row)][int(first_col)]
                second_element = matrix[int(second_row)][int(second_col)]
                matrix[int(first_row)].insert(int(first_col), second_element)
                matrix[int(second_row)].insert(int(second_col), first_element)
                matrix[int(first_row)].pop(int(first_col) + 1)
                matrix[int(second_row)].pop(int(second_col) + 1)
                for j in range(len(matrix)):
                    print(*matrix[j])
    else:
        print(f"Invalid input!")
    command = input().split()
