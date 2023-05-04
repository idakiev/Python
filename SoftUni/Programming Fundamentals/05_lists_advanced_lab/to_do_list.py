command = input().split("-")

list_from_command = []


while command[0] != "End":
    list_from_command.append(command)
    command = input().split("-")


list_of_numbers = []
for i in list_from_command:
    list_of_numbers.append(int(i[0]))
    list_of_numbers = sorted(list_of_numbers)

final_list = []
for k in list_of_numbers:
    for j in list_from_command:
        if str(k) in j:
            final_list.append(j[1])

print(final_list)
