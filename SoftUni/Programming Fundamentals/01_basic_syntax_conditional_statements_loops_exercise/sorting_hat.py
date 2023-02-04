
command = input()

not_voldemort = True


while command != "Welcome!":
    if command != "Voldemort":
        if len(command) < 5:
            print(f"{command} goes to Gryffindor.")
        elif len(command) == 5:
            print(f"{command} goes to Slytherin.")
        elif len(command) == 6:
            print(f"{command} goes to Ravenclaw.")
        elif len(command) > 6:
            print(f"{command} goes to Hufflepuff.")
    else:
        print("You must not speak of that name!" )
        not_voldemort = False
        break
    command = input()

if not_voldemort:
    print("Welcome to Hogwarts.")
