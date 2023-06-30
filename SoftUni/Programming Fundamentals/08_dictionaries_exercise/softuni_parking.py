
number_of_commands = int(input())

users_database = {}

while number_of_commands != 0:
    command = input().split()
    if command[0] == "register":
        username = command[1]
        plate_number = command[2]
        if username not in users_database.keys():
            users_database[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif command[0] == "unregister":
        username = command[1]
        if username in users_database.keys():
            users_database.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

    number_of_commands -= 1

for keys, values in users_database.items():
    print(f"{keys} => {values}")
