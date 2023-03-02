numbers = input().split(", ")
new_list = []
zeros_count = 0

for i in range(len(numbers)):
    current_number = numbers[i]
    if current_number == "0":
        zeros_count += 1
    else:
        new_list.append(current_number)
        continue

for j in range(zeros_count):
    new_list.insert(len(numbers), "0")

int_list = list(map(int, new_list))

print(int_list)
