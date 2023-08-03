
command = input()

message = []
while command != "end":
    command = command.split(" ")
    if command[0] == "Chat":
        message.append(command[1])
    elif command[0] == "Delete":
        if command[1] in message:
            message.remove(command[1])
    elif command[0] == "Edit":
        if command[1] in message:
            msg_index = message.index(command[1])
            message.pop(msg_index)
            message.insert(msg_index, command[2])
    elif command[0] == "Pin":
        if command[1] in message:
            msg_index = message.index(command[1])
            message.pop(msg_index)
            message.append(command[1])
    elif command[0] == "Spam":
        new_command = command[1::]
        for i in new_command:
            message.append(i)
    command = input()
for k in message:
    current_word = k
    print(current_word)
