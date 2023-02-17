
n = int(input())

positive_numbers_list = []
negative_number_list = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers_list.append(current_number)
    else:
        negative_number_list.append(current_number)

positive_count = len(positive_numbers_list)
negative_sum = sum(negative_number_list)

print(f"{positive_numbers_list}\n{negative_number_list}")
print(f"Count of positives: {positive_count}\nSum of negatives: {negative_sum}")
