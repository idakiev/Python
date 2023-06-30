
command = input()

sides_users_dict = {}

while command != "Lumpawaroo":

    if "|" in command:
        command = command.split(" | ")
        current_side = command[0]
        current_user = command[1]
        if current_user not in \
                (inside_users for keys, users in sides_users_dict.items() for inside_users in users):
            if current_side not in sides_users_dict:
                sides_users_dict[current_side] = [current_user]
            else:
                sides_users_dict[current_side].append(current_user)

    if "->" in command:
        command = command.split(" -> ")
        new_side = command[1]
        current_user = command[0]
        if current_user in (inside_users for keys, users in sides_users_dict.items() for inside_users in users):
            if new_side in sides_users_dict.keys():
                for key, values in sides_users_dict.items():
                    for inside_values in values:
                        if current_user in inside_values:
                            if key != new_side:
                                sides_users_dict[key].remove(current_user)
                                sides_users_dict[new_side].append(current_user)
                                print(f"{current_user} joins the {new_side} side!")
                            else:
                                sides_users_dict[key].remove(current_user)
                                sides_users_dict[new_side].append(current_user)
            else:
                for key, values in sides_users_dict.items():
                    for inside_values in values:
                        if current_user in inside_values:
                            sides_users_dict[key].remove(current_user)
                sides_users_dict[new_side] = [current_user]
                print(f"{current_user} joins the {new_side} side!")
        else:
            if new_side in sides_users_dict.keys():
                sides_users_dict[new_side].append(current_user)
                print(f"{current_user} joins the {new_side} side!")
            else:
                sides_users_dict[new_side] = [current_user]
                print(f"{current_user} joins the {new_side} side!")
    command = input()

for side, jedis in sides_users_dict.items():
    if jedis:
        print(f"Side: {side}, Members: {len(jedis)}")
        for user in jedis:
            print(f"! {user}")
