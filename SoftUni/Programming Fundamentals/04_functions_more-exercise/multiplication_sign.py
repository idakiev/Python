first_number = int(input())
second_number = int(input())
third_number = int(input())

list_numbers = [first_number, second_number, third_number]

negative_numbers = 0
is_zero = False

for i in list_numbers:
    if i < 0:
        negative_numbers += 1

    else:
        continue

if 0 in list_numbers:
    is_zero = True
if is_zero:
    print("zero")
else:
    if not negative_numbers or negative_numbers == 2:
        print("positive")
    else:
        print("negative")
