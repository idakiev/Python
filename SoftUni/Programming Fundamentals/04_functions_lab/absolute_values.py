list_of_strings = input().split(" ")
list_as_numbers = list(map(float, list_of_strings))

absolute_numbers = []

for i in range(len(list_as_numbers)):
    absolute_numbers.append(abs(list_as_numbers[i]))

print(absolute_numbers)
