number = int(input())

string_is_pure = True

for i in range(number):
    command = str(input())
    for j in range(len(command)):
        if command[j] == "," or command[j] == "." or command[j] == "_":
            string_is_pure = False
            break
        else:
            continue
    if string_is_pure:
        print(f"{command} is pure.")
    else:
        print(f"{command} is not pure!")
    string_is_pure = True
