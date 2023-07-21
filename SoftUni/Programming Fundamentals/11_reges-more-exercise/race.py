import re

list_of_racers = input().split(", ")

pattern_names = r"([a-zA-Z])"
pattern_distance = r"(\d)"

dict_of_racers = {}

command = input()

while command != "end of race":
    current_name = ''.join(re.findall(pattern_names, command))
    current_distance = re.findall(pattern_distance, command)
    current_distance_total = sum(int(x) for x in current_distance)
    if current_name in list_of_racers:
        if current_name in dict_of_racers.keys():
            previous_distance = dict_of_racers[current_name]
            dict_of_racers[current_name] += current_distance_total
        else:
            dict_of_racers[current_name] = current_distance_total

    command = input()

winners = {player: distance for player, distance in sorted(dict_of_racers.items(),
                                                           reverse=True, key=lambda item: item[1])}
winners_list = []
for key in winners.keys():
    winners_list.append(key)

print(f"1st place: {winners_list[0]}")
print(f"2nd place: {winners_list[1]}")
print(f"3rd place: {winners_list[2]}")
