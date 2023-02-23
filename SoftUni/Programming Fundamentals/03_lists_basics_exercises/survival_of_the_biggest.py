list_of_numbers = input().split(" ")
remove_count = int(input())

list_as_digits = []
for i in range(len(list_of_numbers)):
    list_as_digits.append(int(list_of_numbers[i]))

# list_as_digits.sort(reverse=True)

for k in range(remove_count):
    current_min = min(list_as_digits)
    list_as_digits.remove(current_min)

# for number in list_as_digits:
#     print(f"{number}, ", end="")

print(*list_as_digits, sep=", ")

# print(", ".join(str(list_as_digits)))
# print(', '.join(map(str, list_as_digits)))
# print(", ".join(list_of_numbers))
