
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

cars_in_garage = set()

for i in range(int(input())):
    command = input().split(", ")
    if command[0] == COMMAND_IN:
        cars_in_garage.add(command[1])
    elif command[0] == COMMAND_OUT:
        if command[1] in cars_in_garage:
            cars_in_garage.remove(command[1])

if cars_in_garage:
    for cars in cars_in_garage:
        print(cars)
else:
    print(f"Parking Lot is Empty")
