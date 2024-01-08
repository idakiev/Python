
rows, columns = [int(x) for x in input().split()]

start_char = ord("a")

for row in range(start_char, start_char + rows):
    for col in range(start_char, start_char + columns):
        print(f"{chr(row)}{chr(row + col - start_char)}{chr(row)}", end=" ")

    print()
