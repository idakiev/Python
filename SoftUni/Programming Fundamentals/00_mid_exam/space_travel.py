travel_route = input().split("||")
starting_fuel = int(input())
starting_ammo = int(input())

available_fuel = starting_fuel
available_ammo = starting_ammo

is_goal_reached = True
for i in travel_route:
    if i != "Titan":
        current_command = i.split(" ")
        if current_command[0] == "Travel":
            if int(current_command[1]) <= available_fuel:
                available_fuel -= int(current_command[1])
                print(f"The spaceship travelled {int(current_command[1])} light-years.")
            else:
                print(f"Mission failed.")
                is_goal_reached = False
                break

        elif current_command[0] == "Enemy":
            enemy_armour = int(current_command[1])
            if available_ammo >= enemy_armour:
                available_ammo -= enemy_armour
                print(f"An enemy with {enemy_armour} armour is defeated.")
            else:
                if available_fuel >= 2 * enemy_armour:
                    available_fuel -= 2 * enemy_armour
                    print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
                else:
                    print(f"Mission failed.")
                    is_goal_reached = False
                    break

        elif current_command[0] == "Repair":
            repair_value = int(current_command[1])
            available_fuel += repair_value
            available_ammo += 2 * repair_value
            print(f"Ammunitions added: {2 * repair_value}.")
            print(f"Fuel added: {repair_value}.")
    else:
        print(f"You have reached Titan, all passengers are safe.")
