pirate_ship_status = input().split(">")
warship_status = input().split(">")
max_section_capacity = int(input())

command = input()
is_stalemate = True

while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        if int(command[1]) >= 0:
            if int(command[1]) < len(warship_status):
                current_section = warship_status[int(command[1])]
                if int(current_section) > int(command[2]):
                    new_health = int(current_section) - int(command[2])
                    warship_status[int(command[1])] = str(new_health)
                else:
                    print("You won! The enemy ship has sunken.")
                    is_stalemate = False
                    break
        elif int(command[1]) < 0:
            if abs(int(command[1])) <= len(warship_status):
                current_section = warship_status[int(command[1])]
                if int(current_section) > int(command[2]):
                    new_health = int(current_section) - int(command[2])
                    warship_status[int(command[1])] = str(new_health)
                else:
                    print("You won! The enemy ship has sunken.")
                    is_stalemate = False
                    break
    elif command[0] == "Defend":
        if int(command[1]) >= 0:
            if int(command[1]) < len(pirate_ship_status):
                if int(command[2]) >= 0:
                    if int(command[2]) < len(pirate_ship_status):
                        for i in range(int(command[1]), int(command[2]) + 1):
                            current_section = pirate_ship_status[i]
                            if int(current_section) > int(command[3]):
                                new_health = int(current_section) - int(command[3])
                                pirate_ship_status[i] = str(new_health)
                            else:
                                print("You lost! The pirate ship has sunken.")
                                is_stalemate = False
                                break
                elif int(command[2]) < 0:
                    if abs(int(command[2])) <= len(pirate_ship_status):
                        for i in range(int(command[1]), int(command[2])):
                            current_section = pirate_ship_status[i]
                            if int(current_section) > int(command[3]):
                                new_health = int(current_section) - int(command[3])
                                pirate_ship_status[i] = str(new_health)
                            else:
                                print("You lost! The pirate ship has sunken.")
                                is_stalemate = False
                                break
        elif int(command[1]) < 0:
            if abs(int(command[1])) <= len(pirate_ship_status):
                if int(command[2]) >= 0:
                    if int(command[2]) < len(pirate_ship_status):
                        for i in range(int(command[1]), int(command[2]) + 1):
                            current_section = pirate_ship_status[i]
                            if int(current_section) > int(command[3]):
                                new_health = int(current_section) - int(command[3])
                                pirate_ship_status[i] = str(new_health)
                            else:
                                print("You lost! The pirate ship has sunken.")
                                is_stalemate = False
                                break
                elif int(command[2]) < 0:
                    if abs(int(command[2])) <= len(pirate_ship_status):
                        for i in range(int(command[1]), int(command[2])):
                            current_section = pirate_ship_status[i]
                            if int(current_section) > int(command[3]):
                                new_health = int(current_section) - int(command[3])
                                pirate_ship_status[i] = str(new_health)
                            else:
                                print("You lost! The pirate ship has sunken.")
                                is_stalemate = False
                                break

    elif command[0] == "Repair":
        if int(command[1]) >= 0:
            if int(command[1]) < len(pirate_ship_status):
                current_section = pirate_ship_status[int(command[1])]
                if (int(current_section) + int(command[2])) >= max_section_capacity:
                    new_health = max_section_capacity
                    pirate_ship_status[int(command[1])] = str(new_health)
                else:
                    new_health = int(current_section) + int(command[2])
                    pirate_ship_status[int(command[1])] = str(new_health)
        elif int(command[1]) < 0:
            if abs(int(command[1])) <= len(pirate_ship_status):
                current_section = pirate_ship_status[int(command[1])]
                if (int(current_section) + int(command[2])) >= max_section_capacity:
                    new_health = max_section_capacity
                    pirate_ship_status[int(command[1])] = str(new_health)
                else:
                    new_health = int(current_section) + int(command[2])
                    pirate_ship_status[int(command[1])] = str(new_health)

    elif command[0] == "Status":
        sections_to_repair = 0
        for j in pirate_ship_status:
            current_health = int(j)

            if current_health < max_section_capacity * 0.2:
                sections_to_repair += 1
        if sections_to_repair > 0:
            print(f"{sections_to_repair} sections need repair.")

    if is_stalemate:
        command = input()
    else:
        break

if is_stalemate:
    pirate_ship_sum = sum(list(map(int, pirate_ship_status)))
    warship_sum = sum(list(map(int, warship_status)))

    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
