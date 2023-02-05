number = int(input())

sum_of_digits = 0

for i in range(1, number + 1):
    current_number = i
    for k in range(len(str(current_number))):
        current_digit = str(current_number)[k]
        sum_of_digits += int(current_digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
    sum_of_digits = 0
