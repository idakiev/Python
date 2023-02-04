number_divisor = int(input())
number_boundary = int(input())

largest_number = 0

for i in range(number_boundary, 1, - 1):
    if i % number_divisor == 0 and number_boundary >= i > 0:
        largest_number = i
        break
    else:
        continue

print(f"{largest_number}")
