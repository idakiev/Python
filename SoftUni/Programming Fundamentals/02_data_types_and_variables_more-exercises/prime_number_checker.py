
number = int(input())

is_prime_number = False

for n in range(2, number):
    if (number % n) == 0:
        is_prime_number = False
        break
    else:
        is_prime_number = True
if number == 2 or is_prime_number:
    print("True")
else:
    print("False")
