
rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

sum_matrix = 0
for j in matrix:
    sum_matrix += sum(j)

print(sum_matrix)
print(matrix)
