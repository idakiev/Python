n = int(input())

odd_number = 0
even_number = 0

for _ in range(1, n + 1,):
    current_number = int(input())
    if _ % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number

total_diff = abs(even_number - odd_number)

if even_number == odd_number:
    print(f"Yes")
    print(f"Sum = {even_number}")
else:
    print(f"No")
    print(f"Diff = {total_diff}")
