numbers_to_check = input().split(", ")

numbers_list = list(map(int, numbers_to_check))

numbers_list_index = map(lambda x: x if numbers_list[x] % 2 == 0 else "no", range(len(numbers_list)))

even_numbers_index = list(filter(lambda y: y != "no", numbers_list_index))
print(even_numbers_index)
