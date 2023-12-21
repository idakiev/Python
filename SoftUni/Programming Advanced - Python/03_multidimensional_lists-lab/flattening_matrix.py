
rows = int(input())

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

flat_matrix = []

for j in matrix:
    for number in j:
        flat_matrix.append(number)

print(flat_matrix)
