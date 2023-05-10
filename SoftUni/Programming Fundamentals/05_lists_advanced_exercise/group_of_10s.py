
numbers_sequence = list(map(int, input().split(", ")))
sorted_sequence = sorted(list(numbers_sequence))
current_group = 10

while numbers_sequence:
    numbers_in_current_group = []
    copy_numbers_sequence = list(numbers_sequence)
    for i in copy_numbers_sequence:
        if i <= current_group:
            numbers_in_current_group.append(int(i))
            sorted_sequence.remove(i)
            numbers_sequence.remove(i)
    print(f"Group of {current_group}'s: {numbers_in_current_group}")
    current_group += 10
    copy_numbers_sequence = numbers_sequence

# from math import ceil
#
# numbers_sequence = list(map(int, input().split(", ")))
# sorted_sequence = sorted(list(numbers_sequence))
#
# while numbers_sequence:
#
#     current_group = ceil(int(sorted_sequence[0]) / 10)*10
#     numbers_in_current_group = []
#     copy_numbers_sequence = list(numbers_sequence)
#     for i in copy_numbers_sequence:
#         if i <= current_group:
#             numbers_in_current_group.append(int(i))
#             sorted_sequence.remove(i)
#             numbers_sequence.remove(i)
#     print(f"Group of {current_group}'s: {numbers_in_current_group}")
#     copy_numbers_sequence = numbers_sequence
