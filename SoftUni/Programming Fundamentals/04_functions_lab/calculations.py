command = input()
first_number = int(input())
second_number = int(input())


def multiply_numbers():
    return first_number * second_number


def divide_numbers():
    return int(first_number / second_number)


def add_numbers():
    return first_number + second_number


def subtract_numbers():
    return first_number - second_number


if command == "multiply":
    print(multiply_numbers())
elif command == "divide":
    print(divide_numbers())
elif command == "add":
    print(add_numbers())
elif command == "subtract":
    print(subtract_numbers())
