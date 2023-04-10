number = int(input())


def perfect_number(number_to_check):
    current_sum = 0
    for i in range(1, number_to_check):
        if number_to_check % i == 0:
            current_sum += i
        else:
            continue
    if current_sum == number_to_check:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(number)
