
command = input()

resources_dict = {}


while command != "stop":
    key = command
    if key not in resources_dict.keys():
        resources_dict[key] = 0
    command = input()
    value = command
    resources_dict[key] += int(value)
    command = input()

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
