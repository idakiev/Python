import re

commands_count = int(input())

attacked_planets = []
destroyed_planets = []

for i in range(commands_count):
    current_command = input()
    first_pattern = r"[s,t,a,r]"
    first_match = re.findall(first_pattern, current_command, re.I)
    if first_match:
        remove_count = len(first_match)
    else:
        remove_count = 0

    new_command = ""
    for digit in current_command:
        new_digit = chr(ord(digit) - remove_count)
        new_command += new_digit

    second_pattern = r"@([a-zA-Z]+)[^\@\:\!\-\>]*:([0-9]+)[^\@\:\!\-\>]*!([A,D])![^\@\:\!\-\>]*->([0-9]+)"
    result = re.search(second_pattern, new_command)
    if result:
        if result.group(3) == "A":
            attacked_planets.append(result.group(1))
        elif result.group(3) == "D":
            destroyed_planets.append(result.group(1))
if attacked_planets:
    print(f"Attacked planets: {len(attacked_planets)}")
    for attacked in sorted(attacked_planets):
        print(f"-> {attacked}")
else:
    print(f"Attacked planets: 0")
if destroyed_planets:
    print(f"Destroyed planets: {len(destroyed_planets)}")
    for destroyed in sorted(destroyed_planets):
        print(f"-> {destroyed}")
else:
    print(f"Destroyed planets: 0")
