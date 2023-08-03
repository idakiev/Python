message_string = input()

command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        left_part = message_string[:int(command[1])]
        right_part = message_string[int(command[1]):]
        message_string = right_part + left_part
    elif command[0] == "Insert":
        left_part = message_string[:int(command[1])]
        right_part = message_string[int(command[1]):]
        message_string = left_part + command[2] + right_part
    elif command[0] == "ChangeAll":
        message_string = message_string.replace(command[1], command[2])
    command = input()
print(f"The decrypted message is: {message_string}")
