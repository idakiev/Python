
command = input()

towns = {}

while command != "Sail":
    command = command.split("||")
    if len(command) == 3:
        current_town = command[0]
        ct_people = command[1]
        ct_gold = command[2]
        if current_town not in towns.keys():
            towns[current_town] = {"people": int(ct_people), "gold": int(ct_gold)}
        else:
            towns[current_town]["people"] += int(ct_people)
            towns[current_town]["gold"] += int(ct_gold)

    command = input()

command = input()
while command != "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        current_town = command[1]
        ct_people = command[2]
        ct_gold = command[3]
        if current_town in towns.keys():
            exist_town_people = towns[current_town]["people"]
            exist_town_gold = towns[current_town]["gold"]
            if int(ct_people) >= exist_town_people or int(ct_gold) >= exist_town_gold:
                towns.pop(current_town)
                print(f"{current_town} plundered! {ct_gold} gold stolen, {ct_people} citizens killed.")
                print(f"{current_town} has been wiped off the map!")
            else:
                towns[current_town]["people"] -= int(ct_people)
                towns[current_town]["gold"] -= int(ct_gold)
                print(f"{current_town} plundered! {ct_gold} gold stolen, {ct_people} citizens killed.")

    if command[0] == "Prosper":
        current_town = command[1]
        ct_gold = command[2]
        if int(ct_gold) < 0:
            print("Gold added cannot be a negative number!")
            pass
        else:
            towns[current_town]["gold"] += int(ct_gold)
            new_total_gold = towns[current_town]["gold"]
            print(f"{ct_gold} gold added to the city treasury. {current_town} now has {new_total_gold} gold.")
    command = input()

if towns:
    towns_to_visit = len(towns)
    print(f"Ahoy, Captain! There are {towns_to_visit} wealthy settlements to go to:")
    for town, values in towns.items():
        people_value = values["people"]
        gold_value = values["gold"]
        print(f"{town} -> Population: {people_value} citizens, Gold: {gold_value} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
