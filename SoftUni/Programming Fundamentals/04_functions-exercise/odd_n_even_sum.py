number_input = input()


def odd_even_sum(numbers):
    even_numbers = []
    odd_numbers = []
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])
    sum_even_numbers = sum(map(int, even_numbers))
    sum_odd_numbers = sum(map(int, odd_numbers))
    print(f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}")


odd_even_sum(number_input)
