count = int(input())

even_numbers = set()
odd_numbers = set()
sum_of_chars = 0

for i in range(1, count + 1):
    current_name = input()

    for x in current_name:
        sum_of_chars += ord(x)

    sum_of_chars = sum_of_chars // i
    if sum_of_chars % 2 == 0:
        even_numbers.add(sum_of_chars)
    else:
        odd_numbers.add(sum_of_chars)

    sum_of_chars = 0

if sum(even_numbers) == sum(odd_numbers):
    print(*odd_numbers.union(even_numbers), sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
elif sum(odd_numbers) < sum(even_numbers):
    print(*odd_numbers.symmetric_difference(even_numbers), sep=", ")
