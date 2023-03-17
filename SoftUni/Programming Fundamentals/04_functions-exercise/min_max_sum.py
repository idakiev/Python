numbers = input().split(" ")


def min_max_sum(number):
    min_number = min(map(int, number))
    max_number = max(map(int, number))
    sum_number = sum(map(int, number))
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_number}")


min_max_sum(numbers)
