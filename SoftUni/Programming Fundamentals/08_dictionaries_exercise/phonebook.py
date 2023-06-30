
command = input()

phonebook = {}

while "-" in command:
    command = command.split("-")
    current_key = command[0]
    current_value = command[1]
    phonebook[current_key] = current_value
    command = input()

for i in range(1, int(command) + 1):
    new_command = input()
    if new_command in phonebook.keys():
        current_number = phonebook[new_command]
        print(f"{new_command} -> {current_number}")
    else:
        print(f"Contact {new_command} does not exist.")
