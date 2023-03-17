first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a: int, b: int):
    return a + b


def subtract(a: int, b: int, d: int):
    return sum_numbers(a, b) - d


def add_and_subtract(a: int, b: int, d: int):
    return subtract(a, b, d)


print(add_and_subtract(first_number, second_number, third_number))
