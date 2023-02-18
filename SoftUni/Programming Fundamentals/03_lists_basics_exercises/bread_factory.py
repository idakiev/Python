
initial_energy = 100
initial_coins = 100

command = input().split("|")

is_oven_open = True

for i in range(len(command)):
    current_command = command[i].split("-")
    if current_command[0] == "rest":
        if initial_energy + int(current_command[1]) <= 100:
            initial_energy += int(current_command[1])
            print(f"You gained {int(current_command[1])} energy.")
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100
            print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif current_command[0] == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += int(current_command[1])
            print(f"You earned {int(current_command[1])} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= int(current_command[1]):
            initial_coins -= int(current_command[1])
            print(f"You bought {current_command[0]}.")
        else:
            print(f"Closed! Cannot afford {current_command[0]}.")
            is_oven_open = False
            break

if is_oven_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
