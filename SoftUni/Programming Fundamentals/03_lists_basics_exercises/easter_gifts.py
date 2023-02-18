gifts = input().split(" ")

command = input()

while command != "No Money":

    list_of_command = command.split(" ")

    if "OutOfStock" in command:
        if list_of_command[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == list_of_command[1]:
                    gifts.remove(gifts[i])
                    gifts.insert(i, "None")
                if list_of_command[1] not in gifts:
                    break

    if "Required" in command:
        if 0 <= int(list_of_command[2]) < len(gifts):
            gifts.pop(int(list_of_command[2]))
            gifts.insert(int(list_of_command[2]), list_of_command[1])

    if "JustInCase" in command:
        gifts.pop()
        gifts.insert(len(gifts), list_of_command[1])

    command = input()

for i in range(len(gifts)):
    if gifts[i] != "None":
        print(gifts[i], end=" ")
    else:
        continue
