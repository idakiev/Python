

def rounding_numbers(numbers):
    rounded_numbers = []
    for i in range(len(numbers)):
        rounded_numbers.append(round(float(numbers[i])))
    return list(map(int, rounded_numbers))


numbers_given = input().split(" ")

print(rounding_numbers(numbers_given))
