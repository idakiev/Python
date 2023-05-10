
number_of_electrons = int(input())

list_of_electrons = []

while number_of_electrons > 0:
    if number_of_electrons < (int(2 * (len(list_of_electrons) + 1) ** 2)):
        list_of_electrons.append(number_of_electrons)
        break
    list_of_electrons.append(int(2 * (len(list_of_electrons) + 1) ** 2))
    cells_used = list_of_electrons[-1]
    number_of_electrons -= int(cells_used)


print(list_of_electrons)
