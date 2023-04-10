first_number = int(input())
second_number = int(input())
third_number = int(input())


def min_of_three_numbers(a: int, b: int, c: int):
    list_numbers = [a, b, c]
    return min(list_numbers)


print(min_of_three_numbers(first_number, second_number, third_number))
