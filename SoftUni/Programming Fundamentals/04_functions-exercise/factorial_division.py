first_number = int(input())
second_number = int(input())


def factorial_division(a, b):
    result_a = 1
    result_b = 1
    for i in range(1, a + 1):
        result_a *= i
    for k in range(1, b + 1):
        result_b *= k
    return result_a / result_b


print(f"{factorial_division(first_number, second_number):.2f}")
