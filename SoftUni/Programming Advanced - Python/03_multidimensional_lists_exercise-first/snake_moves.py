from collections import deque

rows, cols = [int(x) for x in input().split()]

snake_string = list(input())
copy_snake = deque(snake_string)

for row in range(1, rows + 1):
    while len(copy_snake) < cols:
        copy_snake.extend(snake_string)

    if row % 2 != 0:
        for i in range(cols):
            print(copy_snake.popleft(), end="")
        print()
    else:
        current_string = []
        for j in range(cols):
            current_string.append(copy_snake.popleft())
        print(''.join(reversed(current_string)))
