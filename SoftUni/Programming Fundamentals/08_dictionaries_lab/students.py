
students = {}

command = input()

while ":" in command:
    command = command.split(":")
    key_1 = command[0]
    key_2 = command[1]
    value_2 = command[2]
    students[key_1] = {key_2: value_2}
    command = input()

if "_" in command:
    current_command = command.split("_")
    new_command = f"{' '.join(current_command)}"
    for key, value in students.items():
        for nested_key, nested_value in value.items():
            if new_command == nested_value:
                print(f"{key} - {nested_key}")
else:
    new_command = command
    for key, value in students.items():
        for nested_key, nested_value in value.items():
            if new_command == nested_value:
                print(f"{key} - {nested_key}")
