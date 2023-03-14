

def data_types(command1, command2):
    if command1 == "int":
        return int(command2) * 2
    elif command1 == "real":
        return f"{(float(command2) * 1.5):.2f}"
    elif command1 == "string":
        return f"${command2}$"


first_command = input()
second_command = input()

print(data_types(first_command, second_command))
