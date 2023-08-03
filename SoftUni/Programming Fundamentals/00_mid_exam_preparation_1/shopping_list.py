initial_shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split(" ")
    if command[0] == "Urgent":
        if command[1] not in initial_shopping_list:
            current_product = command[1]
            initial_shopping_list.insert(0, current_product)

    elif command[0] == "Unnecessary":
        if command[1] in initial_shopping_list:
            current_product = command[1]
            initial_shopping_list.remove(current_product)

    elif command[0] == "Correct":
        if command[1] in initial_shopping_list:
            new_product = command[2]
            old_product_index = initial_shopping_list.index(command[1])
            initial_shopping_list.insert(old_product_index, new_product)
            initial_shopping_list.remove(command[1])

    elif command[0] == "Rearrange":
        if command[1] in initial_shopping_list:
            current_product = command[1]
            initial_shopping_list.remove(current_product)
            initial_shopping_list.append(current_product)
    command = input()

final_list = ", ".join(initial_shopping_list)

print(final_list)
