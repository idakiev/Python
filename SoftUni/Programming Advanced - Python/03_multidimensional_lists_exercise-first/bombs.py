
def read_matrix():
    rows = int(input())
    current_matrix = []

    for i in range(rows):
        current_matrix.append([int(x) for x in input().split()])

    return current_matrix


matrix = read_matrix()

bombs = [[int(y) for y in x.split(",")] for x in input().split()]

while bombs:
    current_bomb_row = bombs[0][0]
    current_bomb_col = bombs[0][1]
    bomb_value = matrix[current_bomb_row][current_bomb_col]
    if current_bomb_row != 0:
        for row in range(current_bomb_row - 1, current_bomb_row + 2):
            if current_bomb_col != 0:
                for col in range(current_bomb_col - 1, current_bomb_col + 2):
                    if matrix[row][col] > 0:
                        matrix[row][col] = matrix[row][col] - bomb_value
                    else:
                        continue
            else:
                for col in range(0, current_bomb_col + 2):
                    if matrix[row][col] > 0:
                        matrix[row][col] = matrix[row][col] - bomb_value
                    else:
                        continue
    else:
        for row in range(0, current_bomb_row + 2):
            if current_bomb_col != 0:
                for col in range(current_bomb_col - 1, current_bomb_col + 2):
                    if matrix[row][col] > 0:
                        matrix[row][col] = matrix[row][col] - bomb_value
                    else:
                        continue
            else:
                for col in range(0, current_bomb_col + 2):
                    if matrix[row][col] > 0:
                        matrix[row][col] = matrix[row][col] - bomb_value
                    else:
                        continue

    bombs.pop(0)

print(matrix)
