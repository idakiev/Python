starting_number = int(input())
sum_numbers = 0

while True:
    current_number = int(input())

    if sum_numbers < starting_number:
        sum_numbers += current_number
    if sum_numbers >= starting_number:
        break

print(f"{sum_numbers}")
