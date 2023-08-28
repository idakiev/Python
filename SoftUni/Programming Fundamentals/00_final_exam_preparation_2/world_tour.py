import re

travel_stops = input()

command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        ct_index = int(command[1])
        new_string = command[2]
        if 0 <= ct_index < len(travel_stops):
            travel_stops = travel_stops[:ct_index] + new_string + travel_stops[ct_index:]
        print(travel_stops)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(travel_stops) and 0 <= end_index < len(travel_stops):
            travel_stops = travel_stops[:start_index] + travel_stops[end_index + 1:]
        print(travel_stops)
    elif command[0] == "Switch":
        old_stop = command[1]
        new_stop = command[2]
        pattern = fr"([:]*\w*[-]*\w*)({old_stop})([:]*\w*[-]*\w*)"
        result = re.findall(pattern, travel_stops)
        if result:
            travel_stops = travel_stops.replace(old_stop, new_stop)

        print(travel_stops)
    command = input()

if command == "Travel":
    print(f"Ready for world tour! Planned stops: {travel_stops}")
