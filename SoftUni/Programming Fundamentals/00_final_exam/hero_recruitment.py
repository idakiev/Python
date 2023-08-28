
heroes_collection = {}

command = input()

while command != "End":
    if "Enroll" or "Learn" or "Unlearn" in command:
        command = command.split(" ")
        if command[0] == "Enroll":
            current_hero = command[1]
            if current_hero not in heroes_collection:
                heroes_collection[current_hero] = []
            else:
                print(f"{current_hero} is already enrolled.")

        if command[0] == "Learn":
            current_hero = command[1]
            spell_to_learn = command[2]
            if current_hero not in heroes_collection:
                print(f"{current_hero} doesn't exist.")
            else:
                if spell_to_learn in heroes_collection[current_hero]:
                    print(f"{current_hero} has already learnt {spell_to_learn}.")
                else:
                    heroes_collection[current_hero].append(spell_to_learn)

        if command[0] == "Unlearn":
            current_hero = command[1]
            spell_to_remove = command[2]
            if current_hero not in heroes_collection:
                print(f"{current_hero} doesn't exist.")
            else:
                if spell_to_remove not in heroes_collection[current_hero]:
                    print(f"{current_hero} doesn't know {spell_to_remove}.")
                else:
                    heroes_collection[current_hero].remove(spell_to_remove)
    command = input()

if command == "End":
    print(f"Heroes:")
    for hero, spells in heroes_collection.items():
        print(f"== {hero}: ", end="")
        print(', '.join(spells))
