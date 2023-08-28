
initial_input = int(input())

cars_collection = {}

for cars in range(initial_input):
    command = input().split("|")
    current_car = command[0]
    current_car_mlg = int(command[1])
    current_car_fuel = int(command[2])
    cars_collection[current_car] = {"mileages": current_car_mlg, "fuel": current_car_fuel}

command = input()
while command != "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car_to_drive = command[1]
        distance_to_drive = int(command[2])
        fuel_to_use = int(command[3])
        if cars_collection[car_to_drive]["fuel"] < fuel_to_use:
            print(f"Not enough fuel to make that ride")
        else:
            cars_collection[car_to_drive]["fuel"] -= fuel_to_use
            cars_collection[car_to_drive]["mileages"] += distance_to_drive
            print(f"{car_to_drive} driven for {distance_to_drive} kilometers. {fuel_to_use} liters of fuel consumed.")
            if cars_collection[car_to_drive]["mileages"] >= 100000:
                del cars_collection[car_to_drive]
                print(f"Time to sell the {car_to_drive}!")
    elif command[0] == "Refuel":
        car_to_fill = command[1]
        fuel_to_fill = int(command[2])
        if (cars_collection[car_to_fill]["fuel"] + fuel_to_fill) > 75:
            diff_fuel = 75 - cars_collection[car_to_fill]["fuel"]
            print(f"{car_to_fill} refueled with {diff_fuel} liters")
            cars_collection[car_to_fill]["fuel"] = 75
        else:
            cars_collection[car_to_fill]["fuel"] += fuel_to_fill
            print(f"{car_to_fill} refueled with {fuel_to_fill} liters")
    elif command[0] == "Revert":
        car_to_revert = command[1]
        mileage_to_revert = int(command[2])
        if cars_collection[car_to_revert]["mileages"] - mileage_to_revert < 10000:
            cars_collection[car_to_revert]["mileages"] = 10000
        else:
            cars_collection[car_to_revert]["mileages"] -= mileage_to_revert
            print(f"{car_to_revert} mileage decreased by {mileage_to_revert} kilometers")

    command = input()

if command == "Stop":
    for car, values in cars_collection.items():
        mileage_value = values["mileages"]
        fuel_value = values["fuel"]
        print(f"{car} -> Mileage: {mileage_value} kms, Fuel in the tank: {fuel_value} lt.")
