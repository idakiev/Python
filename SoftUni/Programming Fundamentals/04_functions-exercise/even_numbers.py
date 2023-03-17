numbers = input().split(" ")


def even_numbers(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


filtered = filter(even_numbers, numbers)
even_numbers_list = list(map(int, filtered))

print(even_numbers_list)
